---
name: kml-converter-myfarm
description: >
  Prepara arquivo KML ou KMZ de talhões para o Importar Talhão do myFarm ERP.
  Use SEMPRE que o usuário enviar um arquivo KML ou KMZ para importar talhões no myFarm,
  mencionar problemas na importação de KML, pedir para "converter KML", "arrumar KML",
  "ajustar arquivo de talhão", "importar talhão", falar de arquivo de linhas de plantio ou de
  passadas de máquina para virar talhão, ou citar erros como "Nenhum talhão válido",
  "tag name deve ter entre 1 e 50 caracteres" ou erro genérico na importação de talhões por arquivo.
---

# Conversor de KML para o myFarm

O leitor de KML do myFarm é restritivo e não diz por que recusa ("Nenhum talhão válido no documento").
Esta skill deixa o arquivo no formato que ele aceita: um talhão por arquivo, pronto para
Agricultura Digital > Mapas > Importar Talhão.

## Duas ferramentas, as mesmas regras

| ferramenta | quem usa | quando |
|---|---|---|
| **a página do conversor** (caminho no mapa do `AGENTS.md`) | qualquer pessoa do time, sem o agente: abre o HTML no navegador, arrasta o arquivo, confere no mapa e baixa. Funciona sem internet e o arquivo não sai do computador | uso do dia a dia, e o **único** caminho quando o arquivo só tem linhas de plantio (ela estima o contorno) |
| **o script `convert_kml.py`** (nesta pasta da skill) | o agente, quando o arquivo chega na conversa | arquivo com os talhões desenhados como área |

As regras do myFarm moram nos dois lugares: o bloco `REGRAS` da página e o `REGRAS` do script.
Mudou uma, muda a outra, e depois abre a página com `#teste` no fim do endereço para rodar os testes dela.

## Passo a passo (agente)

1. Rodar o script: `py convert_kml.py <arquivo.kml ou .kmz> <pasta de saída>` (Windows; no Mac,
   `python3`). Só usa a biblioteca padrão. A saída vai para a pasta do cliente ou do projeto (mapa do
   `AGENTS.md`), em `talhoes-myfarm/AAAA-MM-DD/`; sem pasta do cliente, perguntar onde salvar.
2. Ler o relatório que o script imprime e repassar como diz "O que dizer ao entregar".
3. Código de saída 2 quer dizer que nada foi gerado. Se o relatório diz "só linhas abertas", o arquivo é
   de linhas de plantio ou de passadas de máquina e não tem o contorno do talhão. Dizer isso e indicar a
   página do conversor, que estima o contorno pela área que as linhas cobrem (cada talhão sai marcado
   "Confira", com as linhas desenhadas por baixo para comparar com o mapa do cliente). A outra saída é
   pedir ao cliente o arquivo com o contorno.

## Regras que não mudam

- **Só polígono vira talhão.** Linha aberta e ponto são ignorados e listados no relatório. Nunca fechar
  uma linha para virar área: num arquivo de linhas de plantio (02/10/2026), isso gerou 1.163 talhões
  falsos, somando 8.659 ha numa área de uns 240 ha.
- Talhão em qualquer nível de pasta conta.
- Talhão com várias áreas no mesmo item vira um arquivo por área ("- parte 1", "- parte 2").
- Mesmo desenho duas vezes: fica um só, de preferência o que está dentro de pasta.
- Recorte interno sai, com aviso: o formato do myFarm só leva o contorno externo.
- KMZ (KML compactado) é aberto direto.

## O que o myFarm exige

| regra | o myFarm exige | o Google Earth costuma exportar |
|---|---|---|
| namespaces | nenhum `xmlns` na tag `<kml>` | `xmlns` e `gx` |
| documento | `<Document id="featureCollection">` | `<Document>` com nome |
| talhão | `<Placemark id="UUID">` (UUID v4) | sem id ou com outro formato |
| agrupamento | `<Polygon>` dentro de `<MultiGeometry>` | `<Polygon>` direto |
| coordenadas | só longitude e latitude | longitude, latitude e altitude |
| precisão | no máximo 7 casas decimais | até 15, com sobras de arredondamento |
| sentido | horário | muitas vezes anti-horário |
| nome | de 1 a 50 caracteres | pode passar de 50 |
| formato | XML numa linha só | com quebras e recuos |
| talhões por arquivo | um | vários |

Nome: acima de 50 caracteres é cortado; sem nome ou com o nome padrão ("Polígono sem título") vira TL01,
TL02...; `&` vira "e" e `<`, `>` e aspas saem; nome repetido ganha (2), (3).

## O que dizer ao entregar

1. quantos talhões o arquivo tinha e quantos foram convertidos
2. nomes ajustados (cortado, TL01, caractere trocado, repetido), com o nome original
3. repetidos descartados e itens ignorados (linhas, pontos)
4. o que conferir antes de importar (contorno que se cruza, recorte interno, várias áreas)
5. importar um arquivo por vez em Agricultura Digital > Mapas > Importar Talhão

## Se o myFarm recusar

| mensagem do myFarm | causa provável | o que fazer |
|---|---|---|
| "Nenhum talhão válido no documento" | contorno anti-horário, altitude ou casas demais | passar o arquivo original pelo script ou pela página |
| "A tag name deve ter entre 1 e 50 caracteres" | nome vazio ou longo demais | ajustar o nome (a página deixa trocar antes de baixar) |
| erro sem mensagem clara | vários problemas juntos | passar o arquivo original pelo script ou pela página |
| recusou um arquivo que saiu daqui | regra do myFarm que ainda não está aqui, ou contorno que se cruza | guardar o original e o print do erro, descobrir a regra e ajustar o `REGRAS` nos dois lugares |
