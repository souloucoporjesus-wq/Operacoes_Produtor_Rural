#!/usr/bin/env python3
"""
Conversor de KML para o formato do myFarm (Agricultura Digital > Mapas > Importar Talhão).

Uso:
    py convert_kml.py <arquivo.kml ou .kmz> <pasta_saida>        (Windows)
    python3 convert_kml.py <arquivo.kml ou .kmz> <pasta_saida>   (Mac/Linux)

Gera um .kml por talhão. Só trata como talhão o que vem desenhado como área (Polygon). Linha aberta
(LineString: linha de plantio, passada de máquina) nunca vira talhão: se o arquivo só tem linhas, o
script avisa e sai com código 2; quem estima o contorno pela área das linhas é a página do conversor.

As regras do myFarm moram aqui (REGRAS) e no bloco REGRAS da página do conversor: mudou uma, muda a outra.
Só usa a biblioteca padrão do Python.
"""

import math
import os
import re
import sys
import uuid
import zipfile
from xml.etree import ElementTree as ET
from xml.sax.saxutils import escape

REGRAS = {
    'nome_maximo': 50,                                       # a tag name precisa ter de 1 a 50 caracteres
    'casas_decimais': 7,                                     # coordenada com no máximo 7 casas
    'prefixo_sem_nome': 'TL',                                # talhão sem nome vira TL01, TL02...
    'nomes_genericos': re.compile(r'sem t[ií]tulo|untitled', re.I),  # nome padrão do Google Earth
    'limite_pontos_cruzamento': 1500,                        # acima disso a checagem de contorno cruzado é pulada
}


# ---------- leitura ----------
def local(tag):
    return tag.rsplit('}', 1)[-1] if isinstance(tag, str) else ''


def filhos(el, nome):
    return [c for c in el if local(c.tag) == nome]


def descendentes(el, nome):
    return [d for d in el.iter() if local(d.tag) == nome]


def texto(el):
    return re.sub(r'\s+', ' ', el.text or '').strip() if el is not None else ''


def abrir(caminho):
    """Devolve a raiz do XML. KMZ (KML compactado) é aberto direto."""
    if zipfile.is_zipfile(caminho):
        with zipfile.ZipFile(caminho) as z:
            kmls = [n for n in z.namelist() if n.lower().endswith('.kml')]
            if not kmls:
                raise ValueError('o KMZ não tem nenhum KML dentro')
            alvo = next((n for n in kmls if n.lower().split('/')[-1] == 'doc.kml'), kmls[0])
            return ET.fromstring(z.read(alvo))
    return ET.parse(caminho).getroot()


def ler_coordenadas(t):
    pts, altitude, casas, ilegiveis = [], False, 0, 0
    for tupla in re.sub(r'\s*,\s*', ',', t.strip()).split():
        partes = tupla.split(',')
        try:
            lon, lat = float(partes[0]), float(partes[1])
        except (ValueError, IndexError):
            ilegiveis += 1
            continue
        if len(partes) >= 3 and partes[2] != '':
            altitude = True
        for p in partes[:2]:
            if '.' in p:
                casas = max(casas, len(re.match(r'\d*', p.split('.', 1)[1]).group()))
        pts.append((round(lon, REGRAS['casas_decimais']), round(lat, REGRAS['casas_decimais'])))
    return pts, altitude, casas, ilegiveis


# ---------- geometria ----------
def shoelace(aberto):
    """Soma com x = longitude, y = latitude: positiva = sentido horário."""
    n = len(aberto)
    return sum((aberto[(i + 1) % n][0] - x) * (aberto[(i + 1) % n][1] + y) for i, (x, y) in enumerate(aberto))


def area_ha(anel):
    R, t = 6378137, 0.0
    for (x1, y1), (x2, y2) in zip(anel, anel[1:]):
        t += math.radians(x2 - x1) * (2 + math.sin(math.radians(y1)) + math.sin(math.radians(y2)))
    return abs(t * R * R / 2) / 10000


def se_cruza(anel):
    n = len(anel) - 1
    if n > REGRAS['limite_pontos_cruzamento']:
        return False

    def lado(p, q, r):
        v = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
        return (v > 0) - (v < 0)

    for i in range(n):
        a, b = anel[i], anel[i + 1]
        for j in range(i + 2, n):
            if i == 0 and j == n - 1:
                continue
            c, d = anel[j], anel[j + 1]
            if lado(a, b, c) * lado(a, b, d) < 0 and lado(c, d, a) * lado(c, d, b) < 0:
                return True
    return False


def limpar(it, coords_texto):
    pts, altitude, casas, ilegiveis = ler_coordenadas(coords_texto)
    if ilegiveis:
        it['avisos'].append(f'{ilegiveis} ponto(s) ilegível(is) ignorado(s)')
    if any(abs(x) > 180 or abs(y) > 90 for x, y in pts):
        it['erro'] = 'coordenada fora do mapa (longitude e latitude podem estar trocadas)'
        return
    if altitude:
        it['ajustes'].append('altitude removida')
    if casas > REGRAS['casas_decimais']:
        it['ajustes'].append(f'casas decimais reduzidas para {REGRAS["casas_decimais"]}')
    sem_rep = []
    for p in pts:
        if not sem_rep or sem_rep[-1] != p:
            sem_rep.append(p)
    if len(pts) > len(sem_rep):
        it['ajustes'].append(f'{len(pts) - len(sem_rep)} ponto(s) repetido(s) removido(s)')
    fechado = len(sem_rep) > 1 and sem_rep[0] == sem_rep[-1]
    aberto = sem_rep[:-1] if fechado else sem_rep
    if len(set(aberto)) < 3:
        it['erro'] = 'menos de 3 pontos: não forma uma área'
        return
    soma = shoelace(aberto)
    if soma == 0:
        it['erro'] = 'área zero: os pontos estão todos em linha'
        return
    if not fechado:
        it['ajustes'].append('contorno fechado')
    if soma < 0:
        aberto = aberto[::-1]
        it['ajustes'].append('sentido virado para horário')
    it['anel'] = aberto + [aberto[0]]
    it['chave'] = frozenset(aberto)
    it['area'] = area_ha(it['anel'])
    if se_cruza(it['anel']):
        it['avisos'].append('o contorno se cruza: confira o desenho, o myFarm pode recusar ou calcular a área errada')


# ---------- extração ----------
def extrair(caminho):
    raiz = abrir(caminho)
    pai = {c: p for p in raiz.iter() for c in p}
    itens, ignorados = [], []
    for pm in descendentes(raiz, 'Placemark'):
        n = filhos(pm, 'name')
        nome = texto(n[0]) if n else ''
        pastas, a = [], pai.get(pm)
        while a is not None:  # qualquer nível de pasta
            if local(a.tag) == 'Folder':
                fn = filhos(a, 'name')
                pastas.insert(0, texto(fn[0]) if fn and texto(fn[0]) else 'pasta sem nome')
            a = pai.get(a)
        poligonos = descendentes(pm, 'Polygon')
        if not poligonos:  # ponto e linha não são talhão: nunca fechar uma linha aberta para virar área
            if descendentes(pm, 'Point'):
                motivo = 'ponto'
            elif descendentes(pm, 'LineString') or descendentes(pm, 'LinearRing'):
                motivo = 'linha'
            else:
                motivo = 'sem desenho de área'
            ignorados.append({'nome': nome or '(sem nome)', 'pastas': pastas, 'motivo': motivo})
            continue
        for k, pg in enumerate(poligonos, 1):
            it = {'nome_original': nome, 'pastas': pastas, 'parte': k if len(poligonos) > 1 else 0,
                  'ajustes': [], 'avisos': [], 'erro': None, 'anel': None, 'chave': None, 'area': 0}
            if it['parte']:
                it['avisos'].append(f'área {k} de {len(poligonos)} do mesmo talhão: virou arquivo separado')
            if descendentes(pg, 'innerBoundaryIs'):
                it['avisos'].append('recorte interno descartado: o arquivo do myFarm leva só o contorno externo')
            contorno = descendentes(pg, 'outerBoundaryIs')
            coords = descendentes(contorno[0] if contorno else pg, 'coordinates')
            if not coords or not (coords[0].text or '').strip():
                it['erro'] = 'o talhão não tem coordenadas'
            else:
                limpar(it, coords[0].text)
            itens.append(it)
    return itens, ignorados


def deduplicar(itens):
    """Mesmo desenho duas vezes: fica um só, de preferência o que está dentro de pasta."""
    por_chave, descartados = {}, []
    for it in itens:
        if it['erro']:
            continue
        ja = por_chave.get(it['chave'])
        if ja is None:
            por_chave[it['chave']] = it
        elif it['pastas'] and not ja['pastas']:
            por_chave[it['chave']] = it
            descartados.append(ja)
        else:
            descartados.append(it)
    mantidos = [it for it in itens if it['erro'] or por_chave.get(it['chave']) is it]
    return mantidos, descartados


# ---------- nomes ----------
def trocar_caracteres(n):
    n = n.replace('&', ' e ')
    n = re.sub(r'[<>"\x00-\x1f]', '', n)
    return re.sub(r'\s+', ' ', n).strip()


def cortar(s, maximo):
    return s if len(s) <= maximo else s[:maximo].rstrip()


def nomear(itens):
    m = REGRAS['nome_maximo']
    bases = []
    for it in itens:
        avisos = []
        n = re.sub(r'\s+', ' ', it['nome_original'] or '').strip()
        if not n or REGRAS['nomes_genericos'].search(n):
            n = ''
        else:
            t = trocar_caracteres(n)
            if t != n:
                avisos.append('caractere especial trocado no nome (&, <, > ou aspas)')
            n = t
        bases.append((n, avisos))
    ocupados = {b.lower() for b, _ in bases if b}
    usados, tl = set(), 0
    for it, (base, avisos) in zip(itens, bases):
        if it['erro']:
            it['nome'], it['avisos_nome'] = base or it['nome_original'] or '(sem nome)', []
            continue
        if not base:
            while True:
                tl += 1
                nome = f"{REGRAS['prefixo_sem_nome']}{tl:02d}"
                if nome.lower() not in ocupados and nome.lower() not in usados:
                    break
            avisos.append(f'nome genérico ("{it["nome_original"]}"): recebeu {nome}' if it['nome_original']
                          else f'sem nome no arquivo: recebeu {nome}')
        else:
            suf = f" - parte {it['parte']}" if it['parte'] else ''
            nome = cortar(base, m - len(suf)) + suf
            if len(base) + len(suf) > m:
                avisos.append(f'nome cortado em {m} caracteres (era "{base}")')
        if nome.lower() in usados:
            k = 2
            while True:
                suf = f' ({k})'
                novo = cortar(nome, m - len(suf)) + suf
                k += 1
                if novo.lower() not in usados:
                    break
            avisos.append(f'nome repetido no arquivo: virou "{novo}"')
            nome = novo
        usados.add(nome.lower())
        it['nome'], it['avisos_nome'] = nome, avisos


# ---------- saída ----------
def fmt(x):
    s = f'{x:.{REGRAS["casas_decimais"]}f}'.rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s


def gerar_kml(nome, anel):
    coords = ' '.join(f'{fmt(x)},{fmt(y)}' for x, y in anel)
    return ('<?xml version="1.0" encoding="UTF-8"?>'
            '<kml><Document id="featureCollection">'
            f'<Placemark id="{uuid.uuid4()}">'
            f'<name>{escape(nome, {chr(34): "&quot;", chr(39): "&apos;"})}</name>'
            '<MultiGeometry><Polygon><outerBoundaryIs><LinearRing>'
            f'<coordinates>{coords}</coordinates>'
            '</LinearRing></outerBoundaryIs></Polygon></MultiGeometry>'
            '</Placemark></Document></kml>')


def nome_arquivo(nome):
    s = re.sub(r'[\\/:*?"<>|\x00-\x1f]', '', nome)
    s = re.sub(r'\s+', '_', s).rstrip('._')
    if not s or re.fullmatch(r'(con|prn|aux|nul|com\d|lpt\d)', s, re.I):
        s = 'talhao_' + s
    return s


def situacao(it):
    if it['erro']:
        return 'erro'
    return 'confira' if it['avisos'] or it['avisos_nome'] else 'pronto'


def converter(entrada, pasta_saida):
    itens, ignorados = extrair(entrada)
    itens, descartados = deduplicar(itens)
    nomear(itens)
    rel = {'entrada': entrada, 'pasta': pasta_saida, 'itens': itens, 'descartados': descartados,
           'ignorados': ignorados, 'gerados': []}
    validos = [it for it in itens if not it['erro']]
    if not validos:
        return rel
    os.makedirs(pasta_saida, exist_ok=True)
    usados = {}
    for it in validos:
        base = nome_arquivo(it['nome'])
        k = usados.get(base.lower(), 0)
        usados[base.lower()] = k + 1
        if k:
            base += f'_{k + 1}'
        caminho = os.path.join(pasta_saida, base + '.kml')
        with open(caminho, 'w', encoding='utf-8', newline='') as f:
            f.write(gerar_kml(it['nome'], it['anel']))
        rel['gerados'].append(caminho)
        it['arquivo'] = caminho
    return rel


def imprimir_relatorio(rel):
    itens, ign = rel['itens'], rel['ignorados']
    conta = {s: sum(1 for it in itens if situacao(it) == s) for s in ('pronto', 'confira', 'erro')}
    linhas = sum(1 for g in ign if g['motivo'] == 'linha')
    pontos = sum(1 for g in ign if g['motivo'] == 'ponto')
    print('=' * 60)
    print('Conversão de KML para o myFarm')
    print('=' * 60)
    print(f"Arquivo: {rel['entrada']}")
    print(f'Talhões encontrados: {len(itens)}  (prontos {conta["pronto"]}, confira antes {conta["confira"]}, com erro {conta["erro"]})')
    print(f"Repetidos descartados: {len(rel['descartados'])}")
    print(f'Ignorados por não serem área: {len(ign)}  ({linhas} linhas, {pontos} pontos)')
    if not itens and linhas:
        print()
        print(f'O arquivo não tem contorno de talhão: só {linhas} linhas abertas (linhas de plantio ou passadas de máquina).')
        print('Linha não vira talhão aqui. Para estimar o contorno pela área que as linhas cobrem, use a página do conversor.')
    for it in itens:
        marcas = ([it['erro']] if it['erro'] else []) + it['avisos_nome'] + it['avisos'] + it['ajustes']
        area = f", {it['area']:.2f} ha" if it['anel'] else ''
        pontos_it = f"{len(it['anel'])} pontos" if it['anel'] else 'sem desenho'
        print(f"\n- {it['nome']} [{situacao(it)}] ({pontos_it}{area})")
        print(f"  origem: {' > '.join(it['pastas']) or 'fora de pasta'}")
        for mk in marcas:
            print(f'  · {mk}')
    for d in rel['descartados']:
        print(f"\nRepetido descartado: {d['nome_original'] or '(sem nome)'} ({' > '.join(d['pastas']) or 'fora de pasta'})")
    if rel['gerados']:
        print(f"\n{len(rel['gerados'])} arquivo(s) em {rel['pasta']}")
        print('Importar um por vez em Agricultura Digital > Mapas > Importar Talhão.')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Uso: py convert_kml.py <arquivo.kml ou .kmz> <pasta_saida>')
        sys.exit(1)
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    relatorio = converter(sys.argv[1], sys.argv[2])
    imprimir_relatorio(relatorio)
    sys.exit(0 if relatorio['gerados'] else 2)
