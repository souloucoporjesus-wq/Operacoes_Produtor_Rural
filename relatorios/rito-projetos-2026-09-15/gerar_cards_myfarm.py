import re
import pandas as pd

RITO_DIR = "Ritos - Projetos/Rito dia 15 de Setembro de 2026"
myfarm = pd.read_excel(f"{RITO_DIR}/Report Projetos Myfarm 2025-2026.xlsx")
myfarm = myfarm[myfarm["COD"].apply(lambda v: str(v).replace(".0", "").isdigit())].copy()

col_obs_candidates = [c for c in myfarm.columns if "impediment" in c.lower()]
myfarm["OBS"] = myfarm[col_obs_candidates].bfill(axis=1).iloc[:, 0].fillna("").str.strip()

SUFFIXES = [
    r"\s*-?\s*IMPL[A-Z]*\.?\s*MY\s*FARM$",
    r"\s*-?\s*IMPL[A-Z]*\.?\s*MYFAR[M]?$",
    r"\s*-?\s*REIMPL[A-Z]*\.?\s*MYFARM$",
    r"\s*-?\s*TREINAMENTO\s*MYFARM$",
    r"\s*-?\s*IMP\s*MYFARM$",
]

def clean_name(raw):
    name = raw.strip()
    for pat in SUFFIXES:
        name = re.sub(pat, "", name, flags=re.IGNORECASE)
    return name.strip(" -")

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

def status_badge(status, obs):
    if status == "CANCELADO":
        return '<span class="badge status cancel">Cancelado</span>'
    if re.search("inadimpl", obs, re.IGNORECASE):
        return '<span class="badge status">Inadimplente</span>'
    if re.search("conforme cronograma", obs, re.IGNORECASE):
        return '<span class="badge status ok">Em dia</span>'
    return ""

cards = []
for _, row in myfarm.iterrows():
    name = esc(clean_name(str(row["PROJETO"])))
    obs = esc(str(row["OBS"]).strip()) or "Sem observação registrada no report."
    badge = status_badge(row["STATUS"], str(row["OBS"]))
    cards.append(
        f'    <div class="client myfarm">\n'
        f'      <div class="client-head"><span class="name">{name}</span>'
        f'<span class="badge myfarm">myFarm</span>{badge}</div>\n'
        f'      <p>{obs}</p>\n'
        f'    </div>'
    )

print(f"<!-- {len(cards)} cards -->")
print("\n\n".join(cards))
