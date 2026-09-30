"""Embute dados-nps.json e os números de resumo-nps.json no modelo e grava a apresentação em arquivo único.
Ordem pra atualizar: montar_notebook.py (gera os dois JSON) e depois este script."""
import json
import re
from pathlib import Path

AQUI = Path(__file__).parent
dados = (AQUI / "dados-nps.json").read_text(encoding="utf-8").replace("</", "<\\/")
resumo = json.loads((AQUI / "resumo-nps.json").read_text(encoding="utf-8"))
modelo = (AQUI / "modelo-apresentacao.html").read_text(encoding="utf-8")
assert "/*__DADOS__*/[]" in modelo

pagina = re.sub(r"\{\{(\w+)\}\}", lambda m: resumo[m.group(1)], modelo)
faltou = re.findall(r"\{\{\w+\}\}", pagina)
assert not faltou, f"marcadores sem valor: {faltou}"
(AQUI / "NPS 2026.html").write_text(pagina.replace("/*__DADOS__*/[]", dados), encoding="utf-8")
print("ok", len(dados), "marcadores preenchidos:", len(re.findall(r"\{\{\w+\}\}", modelo)))
