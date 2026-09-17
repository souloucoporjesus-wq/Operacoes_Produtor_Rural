"""Gera painel/index.html a partir do agora.md, dos andamento.md dos projetos e do decisoes.md.

Uso, da raiz do sistema:  python painel/gerar.py
Só lê os arquivos de contexto. Escreve apenas painel/index.html.
"""
import json
import re
import sys
from datetime import datetime
from pathlib import Path

PASTA = Path(__file__).resolve().parent
RAIZ = PASTA.parent
MODELO = PASTA / "modelo.html"
SAIDA = PASTA / "index.html"
EU = "Julio"

ARQ_AGORA = RAIZ / "_contexto" / "agora.md"
ARQ_DECISOES = RAIZ / "_memoria" / "decisoes.md"
PASTAS_PROJETO = ["projetos", "clientes", "retencao", "equipe"]

DATA = r"(\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{4})"
RE_PRAZO = re.compile(r"\s+[—–-]\s*(até|ate|desde|a partir de|em)?\s*" + DATA + r"\s*$", re.I)
RE_RECORRENTE = re.compile(
    r"\s+[—–-]\s*(toda semana|semanal|toda segunda|toda sexta|todo mês|mensal|todo dia|diário)\s*$", re.I
)
RE_TAG = re.compile(r"\s*\[([^\]]+)\]\s*$")
RE_BULLET = re.compile(r"^\s*[-*]\s*(?:\[( |x|X)\])?\s*")
RE_DONO = re.compile(r"^([^:—–\[\]`()]{2,40}?):\s+(.+)$")
RE_DECISAO = re.compile(
    r"^\*\*(\d{4}-\d{2}-\d{2})\*\*\s*\(([^)]*)\)\s*(?:\[([^\]]*)\])?\s*:\s*(.*)$", re.S
)

avisos = []


def ler(caminho):
    return caminho.read_text(encoding="utf-8")


def iso(data):
    if "/" in data:
        d, m, a = data.split("/")
        return f"{a}-{int(m):02d}-{int(d):02d}"
    return data


def secoes(md):
    """Título de '## ' -> linhas do corpo."""
    atual, out = None, {}
    for linha in md.splitlines():
        if linha.startswith("## "):
            atual = linha[3:].strip()
            out[atual] = []
        elif atual is not None:
            out[atual].append(linha)
    return out


def secao(mapa, prefixo):
    for titulo, linhas in mapa.items():
        if titulo.lower().startswith(prefixo.lower()):
            return titulo, linhas
    return None, []


def bullets(linhas):
    """Junta cada bullet com suas linhas de continuação (indentadas)."""
    res = []
    for l in linhas:
        if re.match(r"^\s*[-*]\s", l):
            res.append(l.rstrip())
        elif l.strip() and res and l[:1] in (" ", "\t"):
            res[-1] += " " + l.strip()
    return res


def paragrafos(linhas):
    texto, out = [], []
    for l in linhas:
        if l.strip():
            texto.append(l.strip())
        elif texto:
            out.append(" ".join(texto))
            texto = []
    if texto:
        out.append(" ".join(texto))
    return out


RE_NOME = re.compile(r"^[A-ZÀ-Ý][\wÀ-ÿ.\-]*$")


def dono_valido(prefixo):
    """'Julio', 'Lucas e Guilherme', 'Amanda, Andresa e Ana' valem; 'Etapa 2 do XML' não."""
    tokens = prefixo.replace(",", " ").split()
    if not tokens or len(tokens) > 5:
        return False
    return all(RE_NOME.match(t) or t == "e" for t in tokens)


def parse_pendencia(bruto, origem):
    m = RE_BULLET.match(bruto)
    concluida = bool(m and m.group(1) and m.group(1).lower() == "x")
    texto = bruto[m.end():].strip() if m else bruto.strip()

    tag = None
    t = RE_TAG.search(texto)
    if t:
        tag = t.group(1).strip()
        texto = texto[: t.start()].rstrip()

    prazo = desde = recorrente = None
    r = RE_RECORRENTE.search(texto)
    if r:
        recorrente = r.group(1).lower()
        texto = texto[: r.start()].rstrip()
    else:
        p = RE_PRAZO.search(texto)
        if p:
            tipo = (p.group(1) or "até").lower()
            if tipo in ("desde", "a partir de"):
                desde = iso(p.group(2))
            else:
                prazo = iso(p.group(2))
            texto = texto[: p.start()].rstrip()

    quem = None
    d = RE_DONO.match(texto)
    if d and dono_valido(d.group(1)):
        quem = d.group(1).strip()
        texto = d.group(2).strip()

    if quem is None:
        quem = EU
        avisos.append(f"sem dono ({origem or 'agora.md'}): {texto[:70]}")

    return {
        "texto": texto,
        "quem": quem,
        "prazo": prazo,
        "desde": desde,
        "recorrente": recorrente,
        "tag": tag,
        "decisao": bool(re.match(r"^(decidir|decisão|decisao)\b", texto, re.I)),
        "concluida": concluida,
        "origem": origem,
    }


def ler_agora():
    mapa = secoes(ler(ARQ_AGORA))
    _, onde = secao(mapa, "Onde paramos")
    _, pend = secao(mapa, "Pendências")
    _, quente = secao(mapa, "Quente agora")
    pendencias = [parse_pendencia(b, None) for b in bullets(pend)]
    quente_itens = [RE_BULLET.sub("", b).strip() for b in bullets(quente)]
    return paragrafos(onde), pendencias, quente_itens


def ler_projetos():
    projetos = []
    for pasta in PASTAS_PROJETO:
        base = RAIZ / pasta
        if not base.is_dir():
            continue
        for arq in sorted(base.glob("*/andamento.md")):
            md = ler(arq)
            primeira = md.splitlines()[0] if md.splitlines() else ""
            nome = re.sub(r"^#\s*(Andamento\s*[·\-:]\s*)?", "", primeira).strip() or arq.parent.name
            mapa = secoes(md)
            titulo_onde, onde = secao(mapa, "Onde est")
            data_onde = None
            if titulo_onde:
                m = re.search(DATA, titulo_onde)
                data_onde = iso(m.group(1)) if m else None
            _, pend = secao(mapa, "Pendências")
            _, feito = secao(mapa, "Feito")
            projetos.append({
                "nome": nome,
                "pasta": str(arq.parent.relative_to(RAIZ)).replace("\\", "/"),
                "onde_esta": paragrafos(onde),
                "onde_esta_data": data_onde,
                "pendencias": [parse_pendencia(b, nome) for b in bullets(pend)],
                "feito": [RE_BULLET.sub("", b).strip() for b in bullets(feito)][-3:],
            })
    return projetos


def ler_decisoes():
    if not ARQ_DECISOES.exists():
        return []
    md = ler(ARQ_DECISOES)
    corpo = md.split("<!-- as decisões entram abaixo", 1)[-1]
    out = []
    for b in bullets(corpo.splitlines()):
        texto = RE_BULLET.sub("", b).strip()
        m = RE_DECISAO.match(texto)
        if not m:
            avisos.append(f"decisão fora do formato: {texto[:70]}")
            continue
        resto = m.group(4).strip()
        porque = substitui = None
        s = re.search(r"\s*Substitui:\s*(.*)$", resto)
        if s:
            substitui = s.group(1).strip()
            resto = resto[: s.start()].rstrip()
        p = re.search(r"\s*Por qu[eê]:\s*", resto)
        if p:
            porque = resto[p.end():].strip()
            resto = resto[: p.start()].rstrip()
        out.append({
            "data": m.group(1),
            "quem": m.group(2).strip(),
            "projeto": (m.group(3) or "").strip() or None,
            "texto": resto,
            "porque": porque,
            "substitui": substitui,
        })
    return out


def main():
    onde, pendencias, quente = ler_agora()
    projetos = ler_projetos()
    decisoes = ler_decisoes()

    dados = {
        "gerado_em": datetime.now().strftime("%Y-%m-%dT%H:%M"),
        "eu": EU,
        "onde_paramos": onde,
        "quente": quente,
        "pendencias": pendencias,
        "projetos": projetos,
        "decisoes": decisoes,
        "avisos": avisos,
    }

    modelo = ler(MODELO)
    if "__DADOS_JSON__" not in modelo:
        sys.exit("modelo.html sem o marcador __DADOS_JSON__")
    js = json.dumps(dados, ensure_ascii=False).replace("</", "<\\/")
    SAIDA.write_text(modelo.replace("__DADOS_JSON__", js), encoding="utf-8")

    todas = pendencias + [p for pr in projetos for p in pr["pendencias"]]
    abertas = [p for p in todas if not p["concluida"]]
    hoje = datetime.now().strftime("%Y-%m-%d")
    atrasadas = [p for p in abertas if p["prazo"] and p["prazo"] < hoje]
    cobrar = [p for p in abertas if p["quem"] not in (EU, "Agente")]
    print(f"painel/index.html gerado ({SAIDA.stat().st_size // 1024} KB)")
    print(f"{len(abertas)} pendências abertas · {len(atrasadas)} atrasadas · "
          f"{len(cobrar)} pra cobrar · {len(projetos)} projetos · {len(decisoes)} decisões")
    if avisos:
        print(f"{len(avisos)} linha(s) fora do formato (o painel mostra mesmo assim):")
        for a in avisos:
            print("  - " + a)


if __name__ == "__main__":
    main()
