"""Monta e executa analise-nps.ipynb. Rodar de novo quando chegar exportação nova das campanhas.
Depois deste, rodar gerar_apresentacao.py."""
from pathlib import Path
import nbformat as nbf
from nbclient import NotebookClient

AQUI = Path(__file__).parent
R = {}  # reflexões, escritas depois de ler cada resultado
if (AQUI / "reflexoes.py").exists():
    exec((AQUI / "reflexoes.py").read_text(encoding="utf-8"), R)

def ref(chave):
    return R.get(chave, "**Resultado:** (a preencher depois de ler o output)")

cells = []
md = lambda s: cells.append(nbf.v4.new_markdown_cell(s))
code = lambda s: cells.append(nbf.v4.new_code_cell(s))

md("""# NPS · produto e serviços · 2025 e 2026
Base: exportação das campanhas de NPS da Track, um arquivo por grupo e por ano (produto AgriManager,
produto myFarm e serviços), de janeiro de 2025 a setembro de 2026. A pergunta de negócio: **como está
a percepção do cliente em cada produto e serviço, se 2026 está melhor ou pior que 2025, o que puxa a
nota pra baixo e se o ano vai fechar acima de 2025**, que é a meta. Leitor final: diretoria.""")

code("""import json, re, unicodedata
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from temas_comentarios import TEMAS, MOTIVOS, IGNORAR
from motivo_real import motivo_real, do_comentario, do_marcado, MARCADO, SEM

pd.set_option("display.max_columns", None)""")

code("""GRUPOS = ["Produto AgriManager", "Produto myFarm", "Serviços"]
COR = {"Produto AgriManager": "#2a78d6", "Produto myFarm": "#eb6834", "Serviços": "#1baf7a"}
COR_SECUNDARIA = "#94A3B8"
plt.rcParams.update({
    "figure.figsize": (10, 5.5), "figure.dpi": 110, "font.size": 12,
    "axes.titlesize": 15, "axes.titleweight": "bold",
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.alpha": 0.25,
})""")

md("""## Os arquivos foram lidos certo?
Os CSVs vêm da Track com `;` e acentuação em latin-1. Conferir tamanho e contas de cada arquivo.""")

code("""ARQ = [("Produto AgriManager", 2025, "NPS AGM 2025.csv"), ("Produto AgriManager", 2026, "NPS produto - AGM.csv"),
       ("Produto myFarm", 2025, "NPS myFarm 2025.csv"), ("Produto myFarm", 2026, "NPS produto - myFarm.csv"),
       ("Serviços", 2025, "NPS Serviço 2025.csv"), ("Serviços", 2026, "NPS serviços.csv")]
bruto = {(g, a): pd.read_csv(f, sep=";", encoding="latin-1", dtype=str) for g, a, f in ARQ}
pd.DataFrame({f"{g} {a}": [d.shape[0], d.shape[1], d["Nome da Conta"].nunique()] for (g, a), d in bruto.items()},
             index=["respostas", "colunas", "contas"]).T""")

code("""bruto[("Produto AgriManager", 2026)][["Data/Hora da Opinião", "Nome da Conta", "Nota", "Comentário", "Categoria"]].head(3)""")

md("""**Leitura:** acentos legíveis, uma resposta por linha nos seis arquivos. Diferenças que a
padronização abaixo resolve: no AgriManager o motivo marcado pelo cliente vem **dentro** do
comentário, depois de `## Justificativas ##`, sem vírgula entre as opções; no myFarm não existe
motivo marcado, só a categoria da tratativa; nos serviços o motivo vem na coluna `Justificativas`.
Os arquivos de 2025 têm alguns nomes de coluna e de motivo diferentes dos de 2026 (a UF vem em
`Estado`, e serviços usa rótulos como "Execução do Projeto/Treinamento").""")

md("""## Juntar as campanhas numa base só
Uma linha por resposta, com grupo, ano, campanha, mês, nota, classe (detrator 0 a 6, neutro 7 e 8,
promotor 9 e 10), comentário, motivos e o cliente com nome padronizado.""")

code("""OPCOES_AGM = sorted([k for k in MOTIVOS if k in (
    "Aderência do ERP ao seu Negócio", "Aderência do ERP ao seu dia a dia", "Falhas durante o uso do ERP",
    "Uso/navegação das funcionalidades do ERP", "Experiência com o Suporte Aliare", "Atendimento do Suporte Aliare",
    "Recursos do Produto", "Atualização de versão do ERP", "Falta de Contato",
    "Experiência com outras áreas Aliare", "Outro")], key=len, reverse=True)

def motivos_agm(txt):
    parte = str(txt).split("## Justificativas ##")[1] if "## Justificativas ##" in str(txt) else ""
    achados = []
    for op in OPCOES_AGM:
        if op in parte:
            achados.append(op); parte = parte.replace(op, " ")
    return achados

def lista(txt):
    return [p.strip() for p in str(txt).split(",") if p.strip() and str(txt) != "nan"]

def temas_motivo(itens):
    return sorted({MOTIVOS[i] for i in itens if i in MOTIVOS})

def chave_cliente(nome, servico):
    n = str(nome).strip()
    if servico:
        n = re.sub(r"\\s*-\\s*[^-]*-\\s*[A-Z]{2}\\s*$", "", n)
        n = re.sub(r"\\s+-\\s+[A-Z]{2}\\s*$", "", n)
    n = unicodedata.normalize("NFKD", n).encode("ascii", "ignore").decode().upper()
    return re.sub(r"\\s+", " ", n).strip(" -")

CAMP = {
    "Pesquisa Siagri AgriManager": "Produto AgriManager",
    "Pesquisa MyFarm": "Produto myFarm",
    "Pesquisa CeS MyFarm (Hunter) - Projetos de Implantação": "Implantação myFarm",
    "Pesquisa CeS AGM (Hunter) - Projetos de Implantação": "Implantação AgriManager",
    "Pesquisa CeS AGM (Farmer) - Apoio Técnico e Treinamentos": "Apoio técnico e treinamento AgriManager",
    "Pesquisa CeS MyFarm (Farmer) - Apoio Técnico e Treinamentos": "Apoio técnico e treinamento myFarm",
    "Pesquisa CeS AgroScore Siagri AgriManager": "Monitoria AgroScore AgriManager",
}
LINHA = {"MYFARM": "myFarm", "SIAGRI AGRIMANAGER": "AgriManager"}""")

code("""partes = []
for (grupo, ano), d in bruto.items():
    serv = grupo == "Serviços"
    x = pd.DataFrame({
        "id": d["#"], "grupo": grupo, "ano": ano, "campanha": d["Campanha"].map(CAMP),
        "data": pd.to_datetime(d["Data/Hora da Opinião"], format="%d/%m/%y %H:%M"),
        "nota": d["Nota"].astype(int),
        "nota_anterior": pd.to_numeric(d["Nota Anterior"], errors="coerce"),
        "conta": d["Nome da Conta"].str.strip(),
        "respondente": d["Nome"].str.strip().str.title(),
        "uf": d["Estado"] if "Estado" in d.columns else d["UF"],
        "status": d["Status"],
    })
    if grupo == "Produto AgriManager":
        x["comentario"] = d["Comentário"].str.split("## Justificativas ##").str[0].str.strip(" .")
        cliente = d["Comentário"].map(motivos_agm)
    elif serv:
        x["comentario"] = d["Comentário"].str.strip()
        cliente = d["Justificativas"].map(lista)
    else:
        x["comentario"] = d["Comentário"].str.strip()
        cliente = pd.Series([[]] * len(d), index=d.index)
    cs = d["Categoria"].map(lista).map(lambda l: [i for i in l if i not in IGNORAR])
    x["motivos"] = [temas_motivo(a + b) for a, b in zip(cliente, cs)]
    x["marcado_cliente"] = list(cliente)
    x["marcados"] = [list(dict.fromkeys(a + b)) for a, b in zip(cliente, cs)]
    x["linha"] = d["Linha Produto"].map(LINHA) if serv else ("AgriManager" if grupo == "Produto AgriManager" else "myFarm")
    x["cliente"] = [chave_cliente(n, serv) for n in d["Nome da Conta"]]
    partes.append(x)

nps = pd.concat(partes, ignore_index=True)
nps["comentario"] = nps["comentario"].where(nps["comentario"].str.len() > 3)
nps["classe"] = pd.cut(nps["nota"], [-1, 6, 8, 10], labels=["Detrator", "Neutro", "Promotor"]).astype(str)
nps["mes"] = nps["data"].dt.to_period("M")
nps["temas_coment"] = [TEMAS.get(i, ["Sem conteúdo"] if isinstance(c, str) else []) for i, c in zip(nps["id"], nps["comentario"])]
nps["tem_texto"] = nps["comentario"].notna() & nps["temas_coment"].map(lambda t: t != ["Sem conteúdo"])
nps["motivo_real"] = [motivo_real(i, t, m, c, g) for i, t, m, c, g in zip(nps["id"], nps["temas_coment"], nps["marcados"], nps["classe"], nps["grupo"])]
nps[["grupo", "ano", "campanha", "linha", "mes", "nota", "classe", "cliente", "marcados", "temas_coment", "motivo_real"]].sample(6, random_state=1)""")

code("""pd.DataFrame({"respostas": nps.groupby(["grupo", "ano"]).size(),
              "sem campanha mapeada": nps[nps["campanha"].isna()].groupby(["grupo", "ano"]).size(),
              "sem linha": nps[nps["linha"].isna()].groupby(["grupo", "ano"]).size(),
              "com motivo": nps[nps["motivos"].str.len() > 0].groupby(["grupo", "ano"]).size(),
              "com comentário": nps[nps["comentario"].notna()].groupby(["grupo", "ano"]).size()}).fillna(0).astype(int)""")

code("""sem = nps[nps["temas_coment"].map(lambda t: t == ["Sem conteúdo"])]
sem[["ano", "grupo", "nota", "comentario"]]""")

md(ref("leitura_base"))

md("""# Parte 1 · 2026 até setembro
As perguntas desta parte olham só 2026 (janeiro a setembro).""")

code("""n26 = nps[nps["ano"] == 2026].copy()
n25 = nps[nps["ano"] == 2025].copy()
len(n26), len(n25)""")

md("""## Qual é o NPS de cada produto e serviço no acumulado de 2026?
NPS = % de promotores menos % de detratores. Sempre com o número de respostas ao lado.""")

code("""def calc_nps(g):
    n = len(g)
    return pd.Series({"respostas": n,
                      "promotores %": round(100 * (g["classe"] == "Promotor").mean(), 1),
                      "neutros %": round(100 * (g["classe"] == "Neutro").mean(), 1),
                      "detratores %": round(100 * (g["classe"] == "Detrator").mean(), 1),
                      "NPS": round(100 * ((g["classe"] == "Promotor").mean() - (g["classe"] == "Detrator").mean()), 1)})

n26.groupby("grupo")[["classe"]].apply(calc_nps)""")

code("""n26.groupby(["grupo", "campanha"])[["classe"]].apply(calc_nps).sort_values("respostas", ascending=False)""")

md(ref("q1"))

md("""## Como o NPS de cada mês se comportou?
Linha por produto e serviço, só com as respostas de cada mês. O número de respostas vai junto,
porque mês com poucas respostas balança muito.""")

code("""mensal = n26.groupby(["grupo", "mes"])[["classe"]].apply(calc_nps).reset_index()
mensal.pivot(index="mes", columns="grupo", values=["NPS", "respostas"])""")

code("""fig, ax = plt.subplots()
for g, d in mensal.groupby("grupo"):
    ok = d["respostas"] >= 10
    ax.plot(d["mes"].astype(str), d["NPS"], color=COR[g], lw=2, label=g)
    ax.scatter(d.loc[ok, "mes"].astype(str), d.loc[ok, "NPS"], color=COR[g], s=40, zorder=3)
    ax.scatter(d.loc[~ok, "mes"].astype(str), d.loc[~ok, "NPS"], facecolor="white", edgecolor=COR[g], s=40, zorder=3)
ax.axhline(0, color=COR_SECUNDARIA, lw=1)
ax.set_title("NPS de cada mês por produto e serviço (ponto vazio: menos de 10 respostas)")
ax.legend(frameon=False); plt.show()""")

md(ref("q2"))

md("""## Como o NPS acumulado do ano andou mês a mês?
É a conta que a Track mostra no painel: todas as respostas de janeiro até o fim de cada mês.
Ao lado, quanto o acumulado subiu ou desceu em relação ao mês anterior.""")

code("""def acumulado(df):
    linhas = []
    for (g, a), d in df.groupby(["grupo", "ano"]):
        ultimo = d["data"].dt.month.max()
        for m in range(1, ultimo + 1):
            c = calc_nps(d[d["data"].dt.month <= m])
            linhas.append({"grupo": g, "ano": a, "mes": m, "NPS": c["NPS"], "respostas": c["respostas"]})
    return pd.DataFrame(linhas)

acum = acumulado(nps)
a26 = acum[acum["ano"] == 2026].pivot(index="mes", columns="grupo", values="NPS")
a26.join(a26.diff().round(1).add_suffix(" · variação"))""")

md(ref("q_acum"))

md("""## Por trimestre, a tendência se sustenta?
Agrupar em trimestres dá base maior a cada ponto e mostra se a queda ou a subida é real.""")

code("""n26["tri"] = "T" + n26["data"].dt.quarter.astype(str)
n26.groupby(["grupo", "tri"])[["classe"]].apply(calc_nps)[["respostas", "NPS"]].unstack("tri")""")

md(ref("q3"))

md("""## Que motivos aparecem entre os detratores de cada produto?
Taxa sobre as respostas de detrator **que têm motivo**. Uma resposta pode ter mais de um motivo.""")

code("""det = n26[(n26["classe"] == "Detrator") & (n26["motivos"].str.len() > 0)].explode("motivos")
base = n26[(n26["classe"] == "Detrator") & (n26["motivos"].str.len() > 0)].groupby("grupo").size()
tab = det.groupby(["grupo", "motivos"]).size().unstack("grupo").fillna(0).astype(int)
(tab / base * 100).round(0).assign(**{f"n {g}": tab[g] for g in tab.columns}).sort_values("Produto AgriManager", ascending=False)""")

code("""base.to_frame("detratores com motivo").join(n26[n26["classe"] == "Detrator"].groupby("grupo").size().to_frame("detratores"))""")

md(ref("q4"))

md("""## Do que falam os comentários escritos?
Cada comentário foi lido e recebeu um ou mais assuntos (o de dentro do texto, não o marcado).
Comentário de teste ("hdbdhbfkbiuf", "SEM COMENTÁRIO") fica de fora.""")

code("""com = n26[n26["comentario"].notna()].explode("temas_coment")
com = com[com["temas_coment"] != "Sem conteúdo"]
com.groupby(["temas_coment", "grupo"]).size().unstack("grupo").fillna(0).astype(int).sort_values("Produto myFarm", ascending=False)""")

code("""com[com["classe"] == "Detrator"].groupby(["grupo", "temas_coment"]).size().sort_values(ascending=False).head(12).to_frame("detratores")""")

md(ref("q5"))

md("""## O detrator recebeu retorno?
Status da tratativa de cada resposta de detrator em 2026.""")

code("""st = n26[n26["classe"] == "Detrator"].groupby(["grupo", "status"]).size().unstack("grupo").fillna(0).astype(int)
st.assign(total=st.sum(axis=1)).sort_values("total", ascending=False)""")

md(ref("q6"))

md("""**Ajuste confirmado pelo Julio em 29/09/2026:** os detratores de 2026 que aparecem como
pendentes na Track (atuação interna, atuação do time de produto ou aguardando cliente) já foram
tratados pelo CS; a Track não atualizou o status dos loops. Na apresentação eles contam como
tratados. A coluna `status` continua com o valor original da Track; a apresentação usa
`status_painel`.""")

code("""PENDENTES = ["Pendente Atuacao", "Pendente Atuacao Siagri", "Pendente Aguardando Cliente"]
CONFIRMADO_ATE = pd.Timestamp("2026-09-29 23:59")  # data da confirmação do Julio; pendente novo precisa de confirmação nova
nps["status_painel"] = np.where((nps["ano"] == 2026) & (nps["data"] <= CONFIRMADO_ATE) & nps["status"].isin(PENDENTES),
                                "Tratado pelo CS (loop sem atualizar na Track)", nps["status"])
n26["status_painel"] = nps.loc[n26.index, "status_painel"]
TRATADO = ["Resolvido Satisfeito", "Esclarecimentos efetuados", "Nao Satisfeito com os esclarecimentos", "Resolvido Insatisfeito",
           "Tratado pelo CS (loop sem atualizar na Track)"]
dt = n26[n26["classe"] == "Detrator"]
pd.DataFrame({"tratados pelo CS": dt[dt["status_painel"].isin(TRATADO)].groupby("grupo").size(),
              "cliente não atendeu o contato": dt[dt["status_painel"] == "Encerrado sem sucesso nos contatos"].groupby("grupo").size(),
              "em andamento": dt[dt["status_painel"] == "Acoes em andamento"].groupby("grupo").size(),
              "detratores": dt.groupby("grupo").size()}).fillna(0).astype(int)""")

md(ref("q6b"))

md("""## Quem respondeu mais de uma vez em 2026: a nota subiu ou caiu?
Por cliente e grupo, compara a primeira e a última resposta do ano. Só entra quem tem pelo menos
duas respostas em datas diferentes.""")

code("""ordem = n26.sort_values("data")
evo = ordem.groupby(["grupo", "cliente"]).agg(respostas=("nota", "size"), primeira=("nota", "first"),
                                               ultima=("nota", "last"), media=("nota", "mean"),
                                               dias=("data", lambda s: (s.max() - s.min()).days))
evo = evo[(evo["respostas"] >= 2) & (evo["dias"] > 0)]
evo["movimento"] = pd.cut(evo["ultima"] - evo["primeira"], [-11, -2, 1, 11], labels=["Caiu", "Estável", "Subiu"])
evo.groupby("grupo")["movimento"].value_counts().unstack().assign(clientes=lambda t: t.sum(axis=1))""")

code("""evo.sort_values(["ultima", "respostas"]).head(10)""")

md(ref("q7"))

md("""# Parte 2 · 2026 contra 2025
A meta combinada é **fechar 2026 acima do NPS de 2025 em cada grupo**.""")

md("""## Quanto cada grupo fechou em 2025, e onde estava em setembro de 2025?
O fechamento de 2025 é a meta. O acumulado de setembro de 2025 é a comparação justa com hoje.""")

code("""META = n25.groupby("grupo")[["classe"]].apply(calc_nps)
set25 = n25[n25["data"].dt.month <= 9].groupby("grupo")[["classe"]].apply(calc_nps)
hoje = n26.groupby("grupo")[["classe"]].apply(calc_nps)
pd.DataFrame({"2025 fechado": META["NPS"], "respostas 2025": META["respostas"],
              "set/25 acumulado": set25["NPS"], "set/26 acumulado": hoje["NPS"],
              "diferença no mesmo ponto": (hoje["NPS"] - set25["NPS"]).round(1)})""")

md(ref("q_meta"))

md("""## Mês a mês, 2026 está à frente ou atrás de 2025?
Acumulado do ano em cada mês, nos dois anos, e a diferença.""")

code("""comp = acum.pivot_table(index="mes", columns=["grupo", "ano"], values="NPS")
difs = pd.DataFrame({g: (comp[(g, 2026)] - comp[(g, 2025)]).round(1) for g in GRUPOS})
difs.add_prefix("2026 menos 2025 · ")""")

code("""fig, axs = plt.subplots(1, 3, figsize=(15, 4.6), sharey=True)
for ax, g in zip(axs, GRUPOS):
    for a, estilo in ((2025, dict(color=COR_SECUNDARIA, lw=2)), (2026, dict(color=COR[g], lw=2.5))):
        d = acum[(acum["grupo"] == g) & (acum["ano"] == a)]
        ax.plot(d["mes"], d["NPS"], label=str(a), **estilo)
    ax.set_title(g); ax.set_xticks(range(1, 13)); ax.axhline(0, color=COR_SECUNDARIA, lw=0.8)
axs[0].legend(frameon=False); fig.suptitle("NPS acumulado no ano: 2025 (cinza) e 2026"); plt.show()""")

md(ref("q_comp"))

md("""## A queda do myFarm começou em 2026 ou já vinha de antes?
Mês a mês, o myFarm de 2025 teve um meio de ano muito forte e um fim de ano fraco. Juntar os meses
em blocos mostra em que momento o patamar mudou.""")

code("""mf = nps[nps["grupo"] == "Produto myFarm"].copy()
blocos = [("jan a mar/25", "2025-01", "2025-03"), ("abr a ago/25", "2025-04", "2025-08"),
          ("set a dez/25", "2025-09", "2025-12"), ("jan a mar/26", "2026-01", "2026-03"), ("abr a set/26", "2026-04", "2026-09")]
pd.DataFrame({nome: calc_nps(mf[(mf["mes"].astype(str) >= a) & (mf["mes"].astype(str) <= b)]) for nome, a, b in blocos}).T[["respostas", "promotores %", "detratores %", "NPS"]]""")

md(ref("q_mf_patamar"))

md("""## O volume de respostas mudou de um ano para o outro?
Menos respostas deixam o acumulado mais sensível a cada nota nova.""")

code("""vol = nps[nps["data"].dt.month <= 9].groupby(["grupo", "ano"]).size().unstack("ano")
vol.assign(variação=lambda t: (100 * (t[2026] / t[2025] - 1)).round(0).astype(int).astype(str) + "%")""")

md(ref("q_vol"))

md("""## Os motivos do detrator mudam entre produto e serviço, e de um ano para o outro?
Mesma conta dos motivos acima, agora por grupo e por ano (janeiro a setembro nos dois anos, pra
comparar o mesmo período).""")

code("""jas = nps[nps["data"].dt.month <= 9]
dm = jas[(jas["classe"] == "Detrator") & (jas["motivos"].str.len() > 0)]
base_dm = dm.groupby(["grupo", "ano"]).size()
mot = (dm.explode("motivos").groupby(["motivos", "grupo", "ano"]).size() / base_dm * 100).round(0).unstack(["grupo", "ano"]).fillna(0)
mot.loc[mot.sum(axis=1).sort_values(ascending=False).index]""")

code("""base_dm.unstack("ano").rename(columns=lambda a: f"detratores com motivo {a}")""")

code("""cd = jas[jas["classe"] == "Detrator"].explode("temas_coment")
cd = cd[cd["temas_coment"].notna() & (cd["temas_coment"] != "Sem conteúdo")]
cd.groupby(["temas_coment", "grupo", "ano"]).size().unstack(["grupo", "ano"]).fillna(0).astype(int)""")

md(ref("q_motivos"))

md("""## Onde o acumulado de 2026 deve fechar em dezembro, e supera 2025?
Três cenários para outubro a dezembro, todos com o volume de respostas do 3º trimestre de 2026:
o mesmo NPS do 3º trimestre de 2026 (ritmo atual), o NPS do 4º trimestre de 2025 (o que o fim do
ano costuma trazer) e o melhor trimestre de 2026. Ao lado, o NPS que o 4º trimestre precisaria ter
para o ano fechar acima de 2025.""")

code("""def projecao(g):
    d26 = n26[n26["grupo"] == g]; d25 = n25[n25["grupo"] == g]
    n0 = len(d26); liq0 = (d26["classe"] == "Promotor").sum() - (d26["classe"] == "Detrator").sum()
    q3 = d26[d26["data"].dt.quarter == 3]; resto = len(q3)
    cen = {"ritmo do 3º tri/26": calc_nps(q3)["NPS"],
           "repete o 4º tri/25": calc_nps(d25[d25["data"].dt.quarter == 4])["NPS"],
           "melhor tri de 2026": max(calc_nps(d26[d26["data"].dt.quarter == q])["NPS"] for q in (1, 2, 3))}
    fim = {f"dez · {k}": round(100 * (liq0 + s / 100 * resto) / (n0 + resto), 1) for k, s in cen.items()}
    alvo = META.loc[g, "NPS"]
    precisa = round(100 * (alvo / 100 * (n0 + resto) - liq0) / resto, 1)
    return pd.Series({"set/26": round(100 * liq0 / n0, 1), "meta (2025)": alvo, "respostas out a dez": resto,
                      **{f"NPS do cenário · {k}": s for k, s in cen.items()}, **fim, "4º tri precisaria": precisa})

proj = pd.DataFrame({g: projecao(g) for g in GRUPOS}).T
proj""")

md("""Quanta incerteza cabe nisso? Simulação com o ritmo do 3º trimestre de 2026: o volume de
outubro a dezembro varia em torno do volume do 3º trimestre, e a divisão entre promotores, neutros
e detratores varia em torno da divisão observada no 3º trimestre.""")

code("""rng = np.random.default_rng(2026)

def simula(g, sims=20000):
    d26 = n26[n26["grupo"] == g]; q3 = d26[d26["data"].dt.quarter == 3]
    n0 = len(d26); liq0 = (d26["classe"] == "Promotor").sum() - (d26["classe"] == "Detrator").sum()
    cont = np.array([(q3["classe"] == c).sum() for c in ("Promotor", "Neutro", "Detrator")]) + 1
    vol = rng.poisson(len(q3), sims)
    x = np.array([rng.multinomial(v, p) for v, p in zip(vol, rng.dirichlet(cont, sims))])
    final = 100 * (liq0 + x[:, 0] - x[:, 2]) / (n0 + vol)
    return pd.Series({"chance de superar 2025 %": round(100 * (final > META.loc[g, "NPS"]).mean(), 1),
                      "dez · 10% pior": round(np.percentile(final, 10), 1),
                      "dez · mediana": round(np.percentile(final, 50), 1),
                      "dez · 10% melhor": round(np.percentile(final, 90), 1)})

sim = pd.DataFrame({g: simula(g) for g in GRUPOS}).T
sim""")

md(ref("q_proj"))

md("""# Parte 3 · Qual é o motivo real de cada nota?
As colunas de motivo e o comentário contam partes diferentes da história. Esta parte olha as duas
fontes e define um **motivo principal por resposta**: o comentário manda quando diz o porquê; sem
comentário útil, vale o motivo marcado (na ordem de prioridade do grupo e da classe); "Outro"
sozinho não conta como motivo. A regra completa está em `motivo_real.py`.""")

md("""## As opções de motivo mudam conforme a nota?
No AgriManager, o cliente escolhe o motivo numa lista. Contar cada opção por classe mostra se a
lista é a mesma para todo mundo.""")

code("""agm_op = nps[nps["grupo"] == "Produto AgriManager"].explode("marcado_cliente").dropna(subset=["marcado_cliente"]).reset_index(drop=True)
pd.crosstab(agm_op["marcado_cliente"], agm_op["classe"])""")

md(ref("q_menu"))

md("""## Quando o cliente marca motivo e também escreve, as duas coisas contam a mesma história?
Só entram as respostas que têm as duas coisas: um comentário que diz o porquê e um motivo marcado
diferente de "Outro".""")

code("""nps["mot_coment"] = [do_comentario(i, t, c, g) for i, t, c, g in zip(nps["id"], nps["temas_coment"], nps["classe"], nps["grupo"])]
nps["mot_marcado"] = [do_marcado(m, c, g) for m, c, g in zip(nps["marcados"], nps["classe"], nps["grupo"])]
nps["cats_marcadas"] = nps["marcados"].map(lambda l: {MARCADO[m] for m in l if m in MARCADO})
ambos = nps[nps["mot_coment"].notna() & nps["mot_marcado"].notna()].copy()
ambos["bate"] = [c in s for c, s in zip(ambos["mot_coment"], ambos["cats_marcadas"])]
ambos.groupby("grupo")["bate"].agg(respostas="size", batem="sum").assign(**{"% que batem": lambda t: (100 * t["batem"] / t["respostas"]).round(0)})""")

code("""ambos[~ambos["bate"]].groupby(["mot_marcado", "mot_coment"]).size().sort_values(ascending=False).head(10).to_frame("respostas")""")

md(ref("q_bate"))

md("""## O que diz quem marca só "Outro"?""")

code("""so_outro = nps[nps["marcados"].map(lambda l: l == ["Outro"])]
so_outro.groupby(["grupo", "ano"]).agg(respostas=("id", "size"), com_comentario=("tem_texto", "sum"))""")

code("""so_outro[so_outro["mot_coment"].notna()]["mot_coment"].value_counts().to_frame("motivo lido no comentário")""")

md(ref("q_outro"))

md("""## Qual é o motivo real da nota em 2026, por grupo e classe?
Fatia sobre as respostas que informaram algum motivo; ao lado, quantas não informaram.""")

code("""def tabela_motivo(df):
    inf = df[df["motivo_real"] != SEM]
    t = (inf.groupby(["grupo", "motivo_real"]).size() / inf.groupby("grupo").size() * 100).round(0).unstack("grupo").fillna(0)
    base = pd.DataFrame({"informaram": inf.groupby("grupo").size(), "total": df.groupby("grupo").size()}).T
    return t.loc[t.sum(axis=1).sort_values(ascending=False).index], base

t_det, b_det = tabela_motivo(n26[n26["classe"] == "Detrator"])
b_det""")

code("""t_det""")

code("""t_pro, b_pro = tabela_motivo(n26[n26["classe"] == "Promotor"])
pd.concat([b_pro, t_pro])""")

md(ref("q_real"))

md("""## O motivo real do detrator mudou de 2025 para 2026?
Janeiro a setembro nos dois anos, para comparar o mesmo período.""")

code("""jas = nps[nps["data"].dt.month <= 9]
dj = jas[(jas["classe"] == "Detrator") & (jas["motivo_real"] != SEM)]
mr = (dj.groupby(["grupo", "ano", "motivo_real"]).size() / dj.groupby(["grupo", "ano"]).size() * 100).round(0).unstack(["grupo", "ano"]).fillna(0)
mr.loc[mr.sum(axis=1).sort_values(ascending=False).index]""")

code("""pd.DataFrame({"detratores": jas[jas["classe"] == "Detrator"].groupby(["grupo", "ano"]).size(),
              "informaram motivo": dj.groupby(["grupo", "ano"]).size()})""")

md(ref("q_real_ano"))

md("""# Parte 4 · O que vai bem em 2026
Pontos positivos de 2026 para a visão geral: quem melhorou a nota e o que o cliente diz do
acompanhamento.""")

md("""## Que clientes foram de detrator a promotor dentro de 2026?
Por conta, primeira e última resposta de 2026: a primeira de detrator (0 a 6) e a última de
promotor (9 ou 10).""")

code("""o26 = n26.sort_values("data")
ev26 = o26.groupby(["grupo", "cliente"]).agg(respostas=("nota", "size"), primeira=("nota", "first"), ultima=("nota", "last"),
                                              de=("data", "first"), ate=("data", "last"), conta=("conta", "last"))
viraram = ev26[(ev26["primeira"] <= 6) & (ev26["ultima"] >= 9) & (ev26["de"] < ev26["ate"])]
viraram.assign(de=viraram["de"].dt.strftime("%d/%m"), ate=viraram["ate"].dt.strftime("%d/%m")).sort_values("primeira")""")

md("""## Quantos respondentes passaram a promotores em 2026?
A Track guarda a nota anterior de quem já tinha respondido. Conta quem vinha de detrator ou neutro
e em 2026 deu 9 ou 10, e também o movimento contrário, para ter a foto inteira.""")

code("""na = n26[n26["nota_anterior"].notna()]
pd.Series({"respondentes com nota anterior": len(na),
           "passaram a promotor (vinham de detrator)": int(((na["nota"] >= 9) & (na["nota_anterior"] <= 6)).sum()),
           "passaram a promotor (vinham de neutro)": int(((na["nota"] >= 9) & na["nota_anterior"].between(7, 8)).sum()),
           "subiram a nota": int((na["nota"] > na["nota_anterior"]).sum()),
           "mantiveram": int((na["nota"] == na["nota_anterior"]).sum()),
           "baixaram": int((na["nota"] < na["nota_anterior"]).sum())}).to_frame("respondentes")""")

md("""## O que o cliente escreve sobre o acompanhamento?
Comentários de 2026 com elogio ao atendimento, ao suporte ou ao CS.""")

code("""elogio = n26[n26["tem_texto"] & n26["temas_coment"].map(lambda t: "Elogio ao atendimento" in t or "Suporte" in t) & (n26["classe"] != "Detrator")]
elogio[["grupo", "conta", "nota", "data", "comentario"]].sort_values("nota", ascending=False).head(8)""")

md(ref("q_positivos"))

md("""## Exportar a base pra apresentação
A página lê este JSON embutido; os filtros de tela recalculam tudo a partir das respostas. O
`resumo-nps.json` leva os números citados no texto da visão geral.""")

code("""saida = nps.assign(data=nps["data"].dt.strftime("%Y-%m-%d"), mes=nps["mes"].astype(str))
cols = ["id", "ano", "grupo", "campanha", "linha", "data", "mes", "nota", "nota_anterior", "classe", "conta", "cliente",
        "respondente", "uf", "status_painel", "comentario", "tem_texto", "marcados", "motivo_real"]
registros = json.loads(saida[cols].to_json(orient="records", force_ascii=False))
json.dump(registros, open("dados-nps.json", "w", encoding="utf-8"), ensure_ascii=False)
len(registros)""")

code("""def f(v):
    v = int(np.floor(float(v) + 0.5))  # mesmo arredondamento da página (Math.round)
    return ("−" + str(abs(v))) if v < 0 else str(v)

tri = n26.groupby(["grupo", "tri"])[["classe"]].apply(calc_nps)["NPS"]
cls = lambda g, c: (n26[(n26["grupo"] == g)]["classe"] == c).mean() * 100
dq = lambda g, q: n26[(n26["grupo"] == g) & (n26["tri"] == q)]
pq = lambda g, q, c: (dq(g, q)["classe"] == c).mean() * 100
detm = n26[(n26["classe"] == "Detrator") & (n26["motivos"].str.len() > 0)]
share = lambda g, m: 100 * detm[detm["grupo"] == g]["motivos"].map(lambda l: m in l).mean()
com26 = n26[n26["comentario"].notna() & n26["temas_coment"].map(lambda t: t != ["Sem conteúdo"])]
detr = n26[n26["classe"] == "Detrator"]
resumo = {
    "agm_hoje": f(hoje.loc["Produto AgriManager", "NPS"]), "mf_hoje": f(hoje.loc["Produto myFarm", "NPS"]),
    "sv_hoje": f(hoje.loc["Serviços", "NPS"]),
    "agm_set25": f(set25.loc["Produto AgriManager", "NPS"]), "mf_set25": f(set25.loc["Produto myFarm", "NPS"]),
    "sv_set25": f(set25.loc["Serviços", "NPS"]),
    "mf_t1": f(tri[("Produto myFarm", "T1")]), "mf_t2": f(tri[("Produto myFarm", "T2")]), "mf_t3": f(tri[("Produto myFarm", "T3")]),
    "mf_queda_tri": f(tri[("Produto myFarm", "T1")] - tri[("Produto myFarm", "T3")]),
    "mf_pro_t1": f(pq("Produto myFarm", "T1", "Promotor")), "mf_pro_t3": f(pq("Produto myFarm", "T3", "Promotor")),
    "mf_det_t1": f(pq("Produto myFarm", "T1", "Detrator")), "mf_det_t3": f(pq("Produto myFarm", "T3", "Detrator")),
    "mf_det_coment": str(len(com26[(com26["grupo"] == "Produto myFarm") & (com26["classe"] == "Detrator")])),
    "mf_det_lentidao": str(com26[(com26["grupo"] == "Produto myFarm") & (com26["classe"] == "Detrator")]["temas_coment"].map(lambda t: "Lentidão e travamento" in t).sum()),
    "agm_t1": f(tri[("Produto AgriManager", "T1")]), "agm_t2": f(tri[("Produto AgriManager", "T2")]), "agm_t3": f(tri[("Produto AgriManager", "T3")]),
    "agm_det_pct": f(cls("Produto AgriManager", "Detrator")),
    "agm_falhas": f(share("Produto AgriManager", "Falhas e estabilidade")), "agm_recursos": f(share("Produto AgriManager", "Recursos do produto")),
    "sv_coment": str(len(com26[com26["grupo"] == "Serviços"])),
    "sv_elogio": str(com26[com26["grupo"] == "Serviços"]["temas_coment"].map(lambda t: "Elogio ao atendimento" in t).sum()),
    "det_total": str(len(detr)),
    "det_semcontato": str((detr["status"] == "Encerrado sem sucesso nos contatos").sum()),
    "det_pendente": str(detr["status"].isin(["Pendente Atuacao", "Pendente Atuacao Siagri", "Pendente Aguardando Cliente"]).sum()),
    "det_resolvido": str((detr["status"] == "Resolvido Satisfeito").sum()),
    **{f"{k}_chance": f(sim.loc[g, "chance de superar 2025 %"]) for k, g in (("agm", "Produto AgriManager"), ("mf", "Produto myFarm"), ("sv", "Serviços"))},
    **{f"{k}_precisa": f(proj.loc[g, "4º tri precisaria"]) for k, g in (("agm", "Produto AgriManager"), ("mf", "Produto myFarm"), ("sv", "Serviços"))},
    **{f"{k}_meta": f"{META.loc[g, 'NPS']:.1f}".replace(".", ",") for k, g in (("agm", "Produto AgriManager"), ("mf", "Produto myFarm"), ("sv", "Serviços"))},
}
resumo["det_semretorno"] = str(int(resumo["det_semcontato"]) + int(resumo["det_pendente"]))
for k, g in (("agm", "Produto AgriManager"), ("mf", "Produto myFarm"), ("sv", "Serviços")):
    resumo[f"{k}_dif"] = f(abs(hoje.loc[g, "NPS"] - set25.loc[g, "NPS"]))
    resumo[f"{k}_vol"] = f(abs(100 * (vol.loc[g, 2026] / vol.loc[g, 2025] - 1)))
blk = {nome: calc_nps(mf[(mf["mes"].astype(str) >= a) & (mf["mes"].astype(str) <= b)])["NPS"] for nome, a, b in blocos}
resumo.update({"mf_b2": f(blk["abr a ago/25"]), "mf_b3": f(blk["set a dez/25"]), "mf_b4": f(blk["jan a mar/26"]), "mf_b5": f(blk["abr a set/26"])})
resumo["mf_det_lentidao25"] = str(cd[(cd["grupo"] == "Produto myFarm") & (cd["ano"] == 2025) & (cd["temas_coment"] == "Lentidão e travamento")].shape[0])
# motivo real do detrator, janeiro a setembro de cada ano
cont_mr = dj.groupby(["grupo", "ano", "motivo_real"]).size()
inf_mr = dj.groupby(["grupo", "ano"]).size()
pct_mr = lambda g, a, m: 100 * cont_mr.get((g, a, m), 0) / inf_mr.get((g, a), 1)
resumo.update({
    "agm_mr_falhas26": f(pct_mr("Produto AgriManager", 2026, "Erros e falhas do sistema")),
    "agm_mr_recursos26": f(pct_mr("Produto AgriManager", 2026, "Recursos e relatórios")),
    "agm_mr_falhas25": f(pct_mr("Produto AgriManager", 2025, "Erros e falhas do sistema")),
    "agm_mr_recursos25": f(pct_mr("Produto AgriManager", 2025, "Recursos e relatórios")),
    "mf_det26": str(len(jas[(jas["grupo"] == "Produto myFarm") & (jas["ano"] == 2026) & (jas["classe"] == "Detrator")])),
    "mf_inf26": str(inf_mr.get(("Produto myFarm", 2026), 0)),
    "mf_lent26": str(cont_mr.get(("Produto myFarm", 2026, "Lentidão e quedas do sistema"), 0)),
    "mf_inf25": str(inf_mr.get(("Produto myFarm", 2025), 0)),
    "mf_lent25": str(cont_mr.get(("Produto myFarm", 2025, "Lentidão e quedas do sistema"), 0)),
})
# destaques positivos de 2026
NOME_MES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
mes_mf = n26[n26["grupo"] == "Produto myFarm"].groupby(n26["data"].dt.month)[["classe"]].apply(calc_nps)
mes_mf = mes_mf[mes_mf["respostas"] >= 10].sort_values("NPS", ascending=False)
pro_inf = n26[(n26["classe"] == "Promotor") & (n26["motivo_real"] != SEM)]
fatia_pro = lambda g, m: 100 * (pro_inf[pro_inf["grupo"] == g]["motivo_real"] == m).mean()
resumo.update({
    "sv_pro": f(hoje.loc["Serviços", "promotores %"]), "mf_pro": f(hoje.loc["Produto myFarm", "promotores %"]),
    "agm_pro": f(hoje.loc["Produto AgriManager", "promotores %"]),
    "mf_pro_n": str(int((n26[n26["grupo"] == "Produto myFarm"]["classe"] == "Promotor").sum())),
    "mf_n": str(int((n26["grupo"] == "Produto myFarm").sum())),
    "mf_best_mes": NOME_MES[int(mes_mf.index[0]) - 1], "mf_best": f(mes_mf.iloc[0]["NPS"]),
    "det_tratado": str(int(dt["status_painel"].isin(TRATADO).sum())),
    "agm_pro_ader": f(fatia_pro("Produto AgriManager", "Aderência ao negócio")),
    "sv_pro_cons": f(fatia_pro("Serviços", "Atendimento do consultor")),
    "promovidos": str(int(((na["nota"] >= 9) & (na["nota_anterior"] <= 8)).sum())),
    "viraram_n": str(len(viraram)),
})
import html as _html
ABREV = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
nome_bonito = lambda s: s.title() if s.isupper() else s
itens_v = viraram.reset_index().sort_values(["primeira", "ultima"], ascending=[True, False])
resumo["viraram_html"] = "".join(
    f'<li><span class="vg"><i class="sw" style="background:var(--{ {"Produto AgriManager": "s1", "Produto myFarm": "s2", "Serviços": "s3"}[r.grupo] })"></i>{_html.escape(r.grupo)}</span>'
    f'<b>{_html.escape(nome_bonito(r.conta))}</b><span class="vn">{r.primeira} → {r.ultima}</span>'
    f'<span class="vd">{ABREV[r.de.month - 1]} a {ABREV[r.ate.month - 1]}</span></li>'
    for r in itens_v.itertuples())
json.dump(resumo, open("resumo-nps.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(resumo, open("resumo-nps.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
resumo""")

md(ref("conclusao"))

nb = nbf.v4.new_notebook(cells=cells, metadata={"kernelspec": {"name": "python3", "display_name": "Python 3", "language": "python"}})
NotebookClient(nb, timeout=300, kernel_name="python3", resources={"metadata": {"path": str(AQUI)}}).execute()
nbf.write(nb, AQUI / "analise-nps.ipynb")

# resumo dos outputs pra leitura
for c in nb.cells:
    if c.cell_type == "code":
        for o in c.get("outputs", []):
            t = o.get("text") or o.get("data", {}).get("text/plain", "")
            if o.get("output_type") == "error":
                t = "\n".join(o["traceback"])
            if t:
                print("-" * 80); print(t[:5000])
