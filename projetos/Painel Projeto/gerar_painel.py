"""Gera o painel dos projetos de implantação hunter e abre no navegador.

Uso:
    python gerar_painel.py                 # usa a planilha .xlsx mais nova desta pasta
    python gerar_painel.py outra.xlsx      # usa uma planilha específica
    python gerar_painel.py --sem-abrir     # só gera o arquivo

Sai um HTML único (painel-projetos-hunter.html) com dados e gráficos embutidos:
abre direto do arquivo, sem servidor e sem internet.
"""
import json
import re
import sys
import webbrowser
from datetime import datetime
from pathlib import Path

import pandas as pd
from plotly.offline import get_plotlyjs

import modelo

PASTA = Path(__file__).resolve().parent
MODELO_HTML = PASTA / "painel_template.html"
SAIDA = PASTA / "painel-projetos-hunter.html"
HISTORICO = PASTA / "historico-projetos.json"   # gravado por importar_reports.py (anotações dos reports)

UFS = {"AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR",
       "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"}
PARTICULAS = {"DE", "DA", "DO", "DOS", "DAS", "E"}
SUFIXO_IMPL = re.compile(
    r"[\s\-]*(RE)?IMP(L(ANTA[CÇ][AÃ]O)?)?\.?\s*(MY\s?FARM|YFARM|AGM(\s+ESSENCIAL)?)?\s*$"
    r"|[\s\-]+REIMPLANTA[CÇ][AÃ]O\s*$|[\s\-]+(AGM|MY\s?FARM)\s*$")


def titulo(texto):
    """CAIXA ALTA do ERP em formato de leitura, mantendo UF e siglas sem vogal."""
    if not isinstance(texto, str) or not texto.strip():
        return ""
    def palavra(w, primeira):
        if w in UFS or not re.search(r"[AEIOUÁÉÍÓÚÃÕÂÊÔ]", w):
            return w
        if w in PARTICULAS and not primeira:
            return w.lower()
        return w.capitalize()
    partes = re.split(r"(\W+)", texto.strip().upper())
    out, primeira = [], True
    for p in partes:
        if re.match(r"\w", p):
            out.append(palavra(p, primeira)); primeira = False
        else:
            out.append(p)
    return "".join(out)


def nome_curto(projeto):
    s = SUFIXO_IMPL.sub("", projeto.strip())
    s = re.sub(r"\s+-\s*|\s*-\s+", " - ", s).strip(" -")
    return titulo(s) or titulo(projeto)


def _data(v):
    return None if pd.isna(v) else pd.Timestamp(v).strftime("%Y-%m-%d")


def _num(v, casas=1):
    return None if pd.isna(v) else round(float(v), casas)


def _txt(v):
    return v if isinstance(v, str) else ""


def _os(r, coluna, chave):
    """Número, etapa, consultor, horas e modalidade de uma OS (a última executada ou a próxima)."""
    numero = getattr(r, coluna)
    return {chave: None if pd.isna(numero) else int(numero),
            chave + "_etapa": _txt(getattr(r, coluna + "_ETAPA")),
            chave + "_consultor": titulo(getattr(r, coluna + "_CONSULTOR")),
            chave + "_horas": _num(getattr(r, coluna + "_HORAS")),
            chave + "_execucao": _txt(getattr(r, coluna + "_EXECUCAO"))}


TIPO_NOME = {
    "IMPLANTACAO": "Implantação", "REIMPLANTACAO": "Reimplantação", "TREINAMENTO": "Treinamento",
    "CONSULTORIA": "Consultoria", "DBA": "DBA", "AGROSCORE": "Agroscore", "MOD.VERTICAL": "Módulo vertical",
    "O. SERVICOS": "Outros serviços", "PRODUTOS MOBILE": "Produtos mobile", "MODULO ADICIONAL": "Módulo adicional",
}
JANELA_REALIZADAS = 366   # dias de agendas realizadas que vão pro painel (filtro de data da aba Agendas realizadas)
JANELA_VENCIDAS = 120


def agenda_geral(m, abertos):
    """Agendas de todos os projetos (hunter e farmer) pra agenda dos consultores e as realizadas."""
    g = m.agenda_geral
    dias = lambda n: m.ref - pd.Timedelta(days=n)
    janela = ((g.SITUACAO.isin(["Realizada", "Sem fechar"]) & (g.DIA >= dias(JANELA_REALIZADAS)))
              | (g.SITUACAO == "Próxima")
              | ((g.SITUACAO == "Vencida") & (g.DIA >= dias(JANELA_VENCIDAS))))
    nomes = {}
    def nome(p):
        if p not in nomes:
            nomes[p] = nome_curto(p) if isinstance(p, str) else "Projeto sem nome"
        return nomes[p]
    return [{
        "d": _data(a.DIA), "c": titulo(a.CONSULTOR), "h": _num(a.HORAS) or 0, "os": int(a.OS), "cod": int(a.COD_PROJETO),
        "p": nome(a.PROJETO), "s": a.SISTEMA_NOME, "t": TIPO_NOME.get(a.TIPO_PROJETO, "Outro"),
        "hu": bool(a.HUNTER), "ab": int(a.COD_PROJETO) in abertos, "si": a.SITUACAO,
        "e": _txt(a.ETAPA), "x": _txt(a.EXECUCAO),
        "hi": _txt(a.INICIO), "hf": _txt(a.FIM), "hr": _txt(a.HORARIO),
    } for a in g[janela & g.DIA.notna()].itertuples()]


def carregar_historico():
    """Anotações dos reports por projeto, da mais nova para a mais antiga (vazio se não houver)."""
    if not HISTORICO.exists():
        return {}, {}
    dados = json.loads(HISTORICO.read_text(encoding="utf-8"))
    por = {}
    for e in dados.get("entradas", []):
        por.setdefault(int(e["cod"]), []).append(e)
    for lista in por.values():
        lista.sort(key=lambda e: (e["data"], e["arquivo"]), reverse=True)
    arquivos = sorted({(e["arquivo"], e["data"]) for e in dados.get("entradas", [])})
    return por, {"atualizado_em": dados.get("atualizado_em"), "arquivos": [{"arquivo": a, "data": d} for a, d in arquivos]}


def montar_dados(m, arquivo):
    ab = m.abertos
    historico, info_historico = carregar_historico()
    projetos = []
    for r in ab.itertuples():
        projetos.append({
            "cod": int(r.COD), "nome": nome_curto(r.PROJETO), "projeto": r.PROJETO,
            "cliente": titulo(r.CLIENTE), "grupo_economico": titulo(r.GRUPO_CONOMICO), "uf": r.UF,
            "municipio": titulo(r.MUNICIPIO), "curva": r.CURVA, "manutencao": _num(r.MANUTENCAO_TOTAL_DO_GRUPO, 2),
            "sistema": r.SISTEMA_NOME, "tipo": "Reimplantação" if r.TIPO_PROJETO == "REIMPLANTACAO" else "Implantação",
            "status": r.STATUS.capitalize().replace("Nao ", "Não ").replace("Pendencia", "Pendência"),
            "analista": titulo(r.GERENTE), "responsavel": titulo(r.RESPONSAVEL), "vendedor": titulo(r.VENDEDOR),
            "abertura": _data(r.DT_INICIAL), "dias_aberto": int(r.DIAS_EM_ABERTO),
            "previsto": _num(r.PREVISTO), "adquiridas": _num(r.ADQUIRIDAS), "contratadas": _num(r.HORAS_CONTRATADAS),
            "bonificadas": _num(r.HORAS_BONIFICADAS), "transferidas": _num(r.HORAS_TRANSFERIDAS),
            "credito": _num(r.HORAS_CREDITO_FINANCEIRO), "utilizadas": _num(r.UTILIZADAS),
            "sem_fechar": _num(r.HORAS_SEM_FECHAR), "agendadas": _num(r.HORAS_AGENDADAS),
            "saldo": _num(r.SALDO), "saldo_livre": _num(r.SALDO_LIVRE), "pct": _num(r.PCT_CONSUMO, 4),
            "n_agendas": int(r.AGENDAS_REALIZADAS), "primeira": _data(r.PRIMEIRA_AGENDA),
            "ultima": _data(r.ULTIMA_AGENDA), "proxima": _data(r.PROXIMA_AGENDA),
            "dias_sem_agenda": int(r.DIAS_SEM_AGENDA), "nunca_agenda": bool(r.NUNCA_TEVE_AGENDA),
            "vencidas": int(r.AGENDAS_VENCIDAS), "futuras": int(r.AGENDAS_FUTURAS),
            "fase": int(r.FASE_ATUAL), "fase_nome": r.FASE_NOME, "presencial": _num(r.HORAS_PRESENCIAL),
            "consultores": [{"nome": titulo(c["nome"]), "horas": c["horas"]} for c in r.CONSULTORES],
            "saude": r.SAUDE, "motivos": list(r.MOTIVOS),
            "prioridade": int(r.PRIORIDADE), "grupo": r.PRIORIDADE_GRUPO,
            **_os(r, "ULTIMA_OS", "ultima_os"), "ultima_os_situacao": _txt(r.ULTIMA_OS_SITUACAO),
            **_os(r, "PROXIMA_OS", "proxima_os"),
            "historico": historico.get(int(r.COD), []),
        })

    ag = m.agendas[m.agendas.COD_PROJETO.isin(ab.COD)]
    agendas = [{
        "cod": int(a.COD_PROJETO), "os": int(a.OS), "dia": _data(a.DIA), "consultor": titulo(a.CONSULTOR),
        "horas": _num(a.HORAS), "execucao": a.EXECUCAO if isinstance(a.EXECUCAO, str) else "",
        "etapa": a.ETAPA if isinstance(a.ETAPA, str) else "", "fase": int(a.FASE), "situacao": a.SITUACAO,
        "pacote": None if pd.isna(a.COD_HORA_ADQUIRIDA) else int(a.COD_HORA_ADQUIRIDA),
        "hi": _txt(a.INICIO), "hf": _txt(a.FIM), "hr": _txt(a.HORARIO),
    } for a in ag.itertuples()]

    hr = m.horas[m.horas.PROJETO.isin(ab.COD)]
    pacotes = [{
        "cod": int(h.PROJETO), "codigo": int(h.CODIGO), "data": _data(h.DT_HORAS_ADQUIRIDAS),
        "tipo": titulo(h.TIPO_HORA_ADQ), "grupo": h.GRUPO, "modelo": titulo(h.MODELO),
        "qtde": _num(h.QTDE, 2), "valor_hora": _num(h.VLR_HORAS_ADQUIRIDAS, 2),
    } for h in hr.itertuples()]

    return {
        "meta": {
            "atualizado_em": m.atualizado_em.strftime("%Y-%m-%d %H:%M"),
            "ref": m.ref.strftime("%Y-%m-%d"),
            "gerado_em": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "arquivo": Path(arquivo).name,
            "janela_realizadas": JANELA_REALIZADAS,
            "historico": info_historico,
            "limites": {"sem_agenda_atencao": modelo.DIAS_SEM_AGENDA_ATENCAO,
                        "sem_agenda_critico": modelo.DIAS_SEM_AGENDA_CRITICO,
                        "consumo_atencao": modelo.CONSUMO_ATENCAO, "consumo_critico": modelo.CONSUMO_CRITICO},
        },
        "fases": modelo.FASES,
        "grupos": modelo.GRUPOS_PRIORIDADE,
        "fases_referencia": m.fases_referencia,
        "referencia": {s: {k: _num(v, 0) for k, v in linha.items()} for s, linha in m.referencia.to_dict("index").items()},
        "evolucao": evolucao(m),
        "projetos": projetos, "agendas": agendas, "pacotes": pacotes,
        "agenda_geral": agenda_geral(m, set(int(c) for c in ab.COD)),
    }


def evolucao(m):
    """Séries mensais desde 2025 com todos os projetos hunter (inclusive já encerrados)."""
    hu = m.hunter[m.hunter.STATUS != "CANCELADO"]
    meses = pd.period_range("2025-01", m.ref.to_period("M"), freq="M")
    concl = hu[hu.STATUS == "CONCLUIDO"]
    base = hu[hu.STATUS.isin(["EM ANDAMENTO", "CONCLUIDO"])]
    realizadas = m.agendas[m.agendas.SITUACAO == "Realizada"].merge(hu[["COD", "SISTEMA_NOME"]], left_on="COD_PROJETO", right_on="COD")
    fim = meses.to_timestamp(how="end")
    out = {"meses": [str(p) for p in meses], "entradas": {}, "encerramentos": {}, "carteira": {}, "horas": {}}
    for s in ["myFarm", "AgriManager"]:
        h, c, b, r = (d[d.SISTEMA_NOME == s] for d in (hu, concl, base, realizadas))
        out["entradas"][s] = h.groupby(h.DT_INICIAL.dt.to_period("M")).size().reindex(meses, fill_value=0).tolist()
        out["encerramentos"][s] = c.groupby(c.DT_ENCERRAMENTO.dt.to_period("M")).size().reindex(meses, fill_value=0).tolist()
        out["carteira"][s] = [int(((b.DT_INICIAL <= d) & (b.DT_ENCERRAMENTO.isna() | (b.DT_ENCERRAMENTO > d))).sum()) for d in fim]
        out["horas"][s] = [round(float(x), 1) for x in r.groupby(r.DIA.dt.to_period("M")).HORAS.sum().reindex(meses, fill_value=0)]
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    xlsx = Path(args[0]) if args else modelo.planilha_mais_recente(PASTA)
    print(f"lendo {xlsx.name} ...")
    m = modelo.montar(xlsx)
    dados = json.dumps(montar_dados(m, xlsx), ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = MODELO_HTML.read_text(encoding="utf-8")
    html = html.replace("/*__PLOTLY__*/", get_plotlyjs()).replace("/*__DADOS__*/", dados)
    SAIDA.write_text(html, encoding="utf-8")
    print(f"painel gerado: {SAIDA.name} ({len(m.abertos)} projetos em aberto, posição de {m.atualizado_em:%d/%m/%Y %H:%M})")
    if "--sem-abrir" not in sys.argv:
        webbrowser.open(SAIDA.as_uri())


if __name__ == "__main__":
    main()
