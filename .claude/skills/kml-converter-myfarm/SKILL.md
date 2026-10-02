---
name: kml-converter-myfarm
description: >
  Conversor de arquivos KML para o formato aceito pelo MyFarm ERP.
  Use SEMPRE que o usuário enviar um arquivo KML para importar talhões no MyFarm,
  mencionar problemas na importação de KML, pedir para "converter KML",
  "arrumar KML", "ajustar arquivo de talhão", "importar talhão", ou qualquer
  variação que envolva preparar arquivos KML para o sistema MyFarm.
  Também acione quando o usuário mencionar erros como "Nenhum talhão válido",
  "tag name deve ter entre 1 e 50 caracteres", ou erros genéricos na importação
  de talhões via arquivo.
---

# Conversor KML para MyFarm

Você converte arquivos KML (exportados do Google Earth, Google MyMaps ou outras plataformas) para o formato específico aceito pelo MyFarm ERP.

## Por que essa skill existe

O MyFarm possui um parser KML restritivo que rejeita arquivos exportados diretamente do Google Earth ou MyMaps. As restrições não são documentadas para o usuário, e as mensagens de erro são genéricas ("Nenhum talhão válido no documento"). Esta skill aplica todas as transformações necessárias automaticamente.

## Restrições do parser KML do MyFarm

O MyFarm aceita **apenas** KMLs que sigam **todas** estas regras simultaneamente:

| Regra | O que o MyFarm exige | O que o Google Earth exporta |
|---|---|---|
| Namespaces | Nenhum `xmlns` na tag `<kml>` | Inclui `xmlns` e `gx` |
| Document ID | `<Document id="featureCollection">` | `<Document>` com nome |
| Placemark ID | `<Placemark id="UUID">` (UUID v4) | `<Placemark>` sem ID ou com ID diferente |
| MultiGeometry | `<Polygon>` dentro de `<MultiGeometry>` | `<Polygon>` direto |
| Coordenadas | Apenas `longitude,latitude` (2 valores) | `longitude,latitude,altitude` (3 valores) |
| Precisão | Máximo 7 casas decimais, sem artefatos float | Até 15 casas, com artefatos (ex: `9999999`) |
| Sentido do polígono | Sentido horário (CW) | Sentido anti-horário (CCW) |
| Tag name | Entre 1 e 50 caracteres | Pode exceder 50 |
| Minificação | XML em uma linha, sem indentação | Indentado e formatado |
| Placemarks por arquivo | 1 Placemark por arquivo | Pode ter múltiplos |

## Fluxo de conversão

### Passo 1: Ler e analisar o KML de entrada

```python
from xml.etree import ElementTree as ET

ns = {'kml': 'http://www.opengis.net/kml/2.2'}
tree = ET.parse('arquivo_entrada.kml')
root = tree.getroot()
```

Identificar todos os Placemarks com polígonos. Podem estar:
- Soltos no Document
- Dentro de Folders
- Duplicados (mesmo polígono em Folder e solto)

**Regra de deduplicação:** se um Placemark solto no Document tem coordenadas idênticas a um dentro de uma Folder, descartar o solto.

### Passo 2: Extrair e limpar coordenadas

Para cada Placemark:

1. Extrair texto da tag `<coordinates>`
2. Fazer split por whitespace para obter pares
3. Para cada par, fazer split por vírgula
4. Descartar o terceiro valor (altitude) se existir
5. Converter para float e arredondar para 7 casas decimais
6. Montar como `"{lon},{lat}"`

```python
pairs = coords_raw.split()
clean = []
for p in pairs:
    parts = p.split(',')
    if len(parts) >= 2:
        lon = round(float(parts[0]), 7)
        lat = round(float(parts[1]), 7)
        clean.append((lon, lat))
```

### Passo 3: Garantir sentido horário (CW)

Usar a fórmula da Shoelace para verificar a orientação:

```python
def is_clockwise(coords):
    """Retorna True se o polígono está em sentido horário."""
    total = 0
    n = len(coords)
    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % n]
        total += (x2 - x1) * (y2 + y1)
    return total > 0

if not is_clockwise(coords):
    coords = list(reversed(coords))
```

Alternativamente, usar Shapely:

```python
from shapely.geometry import Polygon
poly = Polygon(coords)
if poly.exterior.is_ccw:
    coords = list(reversed(coords))
```

**Instalar Shapely:** `pip install shapely --break-system-packages`

### Passo 4: Garantir fechamento do polígono

```python
if coords[0] != coords[-1]:
    coords.append(coords[0])
```

### Passo 5: Validar nome

- Se o nome original tiver mais de 50 caracteres, truncar ou usar o nome da Folder/Placemark mais curto
- Se não houver nome, gerar como "TL" + sequência numérica (ex: TL01, TL02)
- Informar ao usuário os nomes que foram ajustados

### Passo 6: Gerar KML no formato MyFarm

Cada Placemark vira um arquivo separado. Formato exato:

```python
import uuid

pm_id = str(uuid.uuid4())
coords_str = ' '.join(f"{c[0]},{c[1]}" for c in coords)

kml_out = (
    f'<?xml version="1.0" encoding="UTF-8"?>'
    f'<kml><Document id="featureCollection">'
    f'<Placemark id="{pm_id}">'
    f'<name>{nome_talhao}</name>'
    f'<MultiGeometry><Polygon><outerBoundaryIs><LinearRing>'
    f'<coordinates>{coords_str}</coordinates>'
    f'</LinearRing></outerBoundaryIs></Polygon></MultiGeometry>'
    f'</Placemark></Document></kml>'
)
```

### Passo 7: Salvar e entregar

- Um arquivo `.kml` por talhão
- Nome do arquivo: nome do talhão com caracteres especiais substituídos por `_`
- Salvar em `/mnt/user-data/outputs/`
- Usar `present_files` para entregar ao usuário

## Script completo de referência

Consulte `references/convert_kml.py` para o script completo e testado.

## Comunicação com o usuário

Ao entregar os arquivos, informar:
1. Quantos talhões foram encontrados no arquivo original
2. Quantos foram convertidos com sucesso
3. Se algum nome foi truncado ou ajustado (e qual era o original)
4. Se algum Placemark duplicado foi descartado
5. Instrução: importar cada arquivo individualmente em Agricultura Digital > Mapas > Importar Talhão

## Troubleshooting

| Erro no MyFarm | Causa provável | Verificação |
|---|---|---|
| "Nenhum talhão válido no documento" | Polígono em sentido anti-horário (CCW) | Verificar com Shapely: `poly.exterior.is_ccw` deve ser `False` |
| "Nenhum talhão válido no documento" | Coordenadas com altitude (3 valores) | Verificar se há 3 valores por par |
| "Nenhum talhão válido no documento" | Artefatos de ponto flutuante | Verificar coordenadas com mais de 7 decimais |
| "A tag 'name' deve ter entre 1 e 50 caracteres" | Nome do talhão muito longo | Verificar `len(name) > 50` |
| Erro genérico sem mensagem clara | Combinação de múltiplos problemas | Aplicar todas as transformações acima |
