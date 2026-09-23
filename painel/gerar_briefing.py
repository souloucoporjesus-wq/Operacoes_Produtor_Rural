"""Gera painel/briefing.html e briefing/AAAA-MM-DD.md a partir de briefing/AAAA-MM-DD.json.

Uso: python painel/gerar_briefing.py [AAAA-MM-DD]   (sem data: o briefing mais recente)
"""
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PASTA = RAIZ / "briefing"
MODELO = RAIZ / "painel" / "briefing-modelo.html"
SAIDA = RAIZ / "painel" / "briefing.html"
CONF = {"certo": "[Certo]", "provavel": "[Provável]", "suposicao": "[Suposição]"}


def escolher(data):
    if data:
        caminho = PASTA / f"{data}.json"
        if not caminho.exists():
            sys.exit(f"Não achei briefing/{data}.json.")
        return caminho
    todos = sorted(PASTA.glob("????-??-??.json"))
    if not todos:
        sys.exit("Ainda não tem nenhum briefing em briefing/.")
    return todos[-1]


def normalizar(dados):
    if "data" not in dados:
        sys.exit("O briefing não tem o campo 'data'.")
    for i, p in enumerate(dados.get("pendencias") or [], 1):
        p.setdefault("id", f"p{i}")
    return dados


def conf(x):
    return CONF.get(x.get("confianca") or "", "")


def texto_md(d):
    linhas = [f"# Briefing · {d['data']}", ""]
    j = d.get("janela") or {}
    if j:
        linhas += [f"Janela: {j.get('inicio', '')} a {j.get('fim', '')}", ""]
    f = d.get("fontes") or {}
    if f:
        linhas += ["Fontes: " + ", ".join(f"{k} {v}" for k, v in f.items()), ""]

    def secao(titulo, itens, formato):
        if not itens:
            return
        linhas.extend([f"## {titulo}", ""])
        linhas.extend(formato(x) for x in itens)
        linhas.append("")

    secao("Resumo executivo", d.get("resumo"), lambda r: f"1. {r}")

    def pend(p):
        marcas = [p.get("prioridade", ""), "parada" if p.get("status") == "parada" else "", "Leandro" if p.get("chefe") else ""]
        quando = f"prazo {p['prazo']}" if p.get("prazo") else (f"desde {p['desde']}" if p.get("desde") else "")
        partes = [x for x in [", ".join(m for m in marcas if m), p.get("quem", ""), quando, p.get("origem", ""), p.get("ref", "")] if x]
        corpo = f"- **{p['titulo']}** · " + " · ".join(partes)
        return corpo + (f"\n  {p['detalhe']}" if p.get("detalhe") else "")

    secao("Pendências", d.get("pendencias"), pend)
    secao("Com o Leandro", d.get("chefe"), lambda c: f"- {conf(c)} **{c['titulo']}**" + (f": {c['detalhe']}" if c.get("detalhe") else ""))
    secao("Sinais do time", d.get("time"), lambda t: f"- {conf(t)} **{t['pessoa']}** ({t.get('gravidade', '')}): {t['sinal']}" + (f" Sugestão: {t['sugestao']}" if t.get("sugestao") else ""))
    secao("Padrões", d.get("padroes"), lambda p: f"- {conf(p)} **{p['padrao']}**" + (f" {p['implicacao']}" if p.get("implicacao") else ""))
    secao("Fora do normal", d.get("anomalias"), lambda a: f"- {conf(a)} **{a['titulo']}**" + (f": {a['detalhe']}" if a.get("detalhe") else ""))
    secao("Pra você ajustar", d.get("correcoes"), lambda c: f"- {conf(c)} **{c['tema']}**: {c['observacao']}" + (f" Faria assim: {c['sugestao']}" if c.get("sugestao") else ""))
    secao("O que aprendi (a confirmar)", d.get("aprendizados"), lambda a: f"- {conf(a)} **{a.get('sobre', 'Aprendizado')}**: {a['texto']}")
    linhas.append("_Gerado por painel/gerar_briefing.py a partir do JSON do dia; não editar na mão._")
    return "\n".join(linhas) + "\n"


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    origem = escolher(sys.argv[1] if len(sys.argv) > 1 else None)
    dados = normalizar(json.loads(origem.read_text(encoding="utf-8")))
    modelo = MODELO.read_text(encoding="utf-8")
    bloco = json.dumps(dados, ensure_ascii=False).replace("</", "<\\/")
    SAIDA.write_text(modelo.replace("__DADOS_JSON__", bloco), encoding="utf-8")
    origem.with_suffix(".md").write_text(texto_md(dados), encoding="utf-8")

    pend = dados.get("pendencias") or []
    print(
        f"Briefing de {dados['data']}: {len(pend)} pendências "
        f"({sum(p.get('prioridade') == 'critica' for p in pend)} críticas, "
        f"{sum(p.get('status') == 'parada' for p in pend)} paradas), "
        f"{len(dados.get('chefe') or [])} com o Leandro, {len(dados.get('time') or [])} sinais do time, "
        f"{len(dados.get('correcoes') or [])} ajustes pra você."
    )
    print(f"Página: {SAIDA.relative_to(RAIZ)} · texto: {origem.with_suffix('.md').relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
