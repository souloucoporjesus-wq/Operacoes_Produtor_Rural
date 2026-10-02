"""Importa os reports de projetos (planilhas "Report Projetos ...xlsx") para o histórico do painel.

Os reports são exportações filtradas do CES em que a analista anota, projeto a projeto, o andamento,
a previsão de encerramento, o status financeiro, o HandOff e o analista de sucesso. Ainda não têm
um padrão fixo, por isso a leitura reconhece as colunas pelo nome e este script NÃO roda no
atualizar-painel.bat: quando chegar um report novo, rodar com a skill analise_projetos e conferir.

Uso:
    python importar_reports.py            # lê os Report*.xlsx da pasta e grava historico-projetos.json

O histórico acumula: cada importação acrescenta as anotações do arquivo na data em que ele foi
salvo; reimportar o mesmo arquivo na mesma data substitui só aquelas linhas.
"""
import json
import re
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

PASTA = Path(__file__).resolve().parent
SAIDA = PASTA / "historico-projetos.json"
NUMEROS = {"HR ADQ": "hr_adq", "PLANEJADO": "planejado", "REALIZADO": "realizado",
           "ESTOQUE DE HR": "estoque", "FINANCEIRO": "financeiro", "FATURADO": "faturado"}


def _limpa(v):
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return ""
    return re.sub(r"[ \t\xa0]+", " ", str(v)).strip()


def _num(v):
    return None if v is None or pd.isna(v) else round(float(v), 2)


def _coluna(df, *padroes):
    for c in df.columns:
        nome = str(c).strip().lower()
        if any(re.search(p, nome) for p in padroes):
            return c
    return None


def ler_report(arquivo):
    """Uma linha por projeto do report, com as colunas normalizadas."""
    df = pd.read_excel(arquivo)
    df = df[pd.to_numeric(df.COD, errors="coerce").notna()].copy()   # tira Total e filtros do rodapé
    df["COD"] = df.COD.astype(int)
    nota = _coluna(df, r"^andamento")
    handoff = _coluna(df, r"^handoff")
    if handoff is None:   # no report do AgriManager a coluna do HandOff veio sem título
        sem_nome = [c for c in df.columns if str(c).startswith("Unnamed")]
        handoff = next((c for c in sem_nome if df[c].astype(str).str.contains("HandOff|Encerrado", case=False).any()), None)
    sucesso = _coluna(df, r"analista de sucesso")
    data = datetime.fromtimestamp(Path(arquivo).stat().st_mtime).strftime("%Y-%m-%d")
    linhas = []
    for r in df.itertuples(index=False):
        d = dict(zip(df.columns, r))
        linhas.append({
            "cod": int(d["COD"]), "arquivo": Path(arquivo).name, "data": data,
            "sistema": "myFarm" if _limpa(d.get("SISTEMA")) == "MYFARM" else "AgriManager",
            "projeto": _limpa(d.get("PROJETO")), "status": _limpa(d.get("STATUS")).capitalize(),
            "andamento": _limpa(d.get(nota)) if nota else "", "handoff": _limpa(d.get(handoff)) if handoff else "",
            "analista_sucesso": _limpa(d.get(sucesso)) if sucesso else "",
            **{chave: _num(d.get(col)) for col, chave in NUMEROS.items()},
        })
    return linhas


def ler_reports(pasta=PASTA):
    """Todos os Report*.xlsx da pasta, numa tabela (para o notebook)."""
    linhas = [l for f in sorted(Path(pasta).glob("Report*.xlsx")) if not f.name.startswith("~$") for l in ler_report(f)]
    return pd.DataFrame(linhas)


def main():
    novos = ler_reports()
    if novos.empty:
        sys.exit("nenhum Report*.xlsx na pasta")
    antigo = json.loads(SAIDA.read_text(encoding="utf-8"))["entradas"] if SAIDA.exists() else []
    chaves = set(zip(novos.arquivo, novos.data))
    mantidas = [e for e in antigo if (e["arquivo"], e["data"]) not in chaves]
    entradas = mantidas + novos.to_dict("records")
    entradas.sort(key=lambda e: (e["cod"], e["data"]))
    SAIDA.write_text(json.dumps({"atualizado_em": datetime.now().strftime("%Y-%m-%d %H:%M"), "entradas": entradas},
                                ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(novos)} anotações importadas de {len(chaves)} arquivo(s); histórico com {len(entradas)} anotações "
          f"de {len({e['cod'] for e in entradas})} projetos em {SAIDA.name}")


if __name__ == "__main__":
    main()
