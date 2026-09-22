---
name: granola
description: >
  Traz as reuniões novas do Granola pra dentro do sistema: salva a transcrição bruta numa pasta
  genérica (`_memoria/reunioes/`) e distila o essencial pro `contexto.md` do projeto certo, com
  data e caminho da fonte. Roda sozinha no primeiro comando de cada dia (gatilho da seção 4 do
  AGENTS.md), sem precisar de pedido. Use também quando o usuário chamar /granola, disser "traz as
  reuniões do granola", "importa as transcrições", "o que gravamos hoje".
---

# /granola · trazer as reuniões novas

## 1. Só roda uma vez por dia

Conferir se já existe algum arquivo de hoje em `_memoria/reunioes/` (padrão de nome, item 3). Se
já existe, não rodar de novo nesta sessão — a pasta já é o registro de que hoje foi conferido.

## 2. Ver o que é novo

Listar `_memoria/reunioes/` pra saber a reunião mais recente já importada (pelo nome do arquivo,
que leva a data). Chamar `mcp__claude_ai_Granola__list_meetings` (ou `get_meetings`) e pegar só as
reuniões depois dessa data — sem duplicar o que já foi trazido.

Sem reunião nova: não criar nada, seguir em silêncio (isso entra no resumo da sessão só se houver
algo a dizer).

## 3. Salvar a transcrição bruta

Pra cada reunião nova, `get_meeting_transcript` (a fala literal, não o resumo de IA do
`get_meetings`) e salvar em:

```
_memoria/reunioes/AAAA-MM-DD - <título da reunião>.md
```

Com um cabeçalho simples no topo do arquivo: data, participantes (se o Granola trouxer) e "fonte:
Granola — transcrição literal". Esse arquivo é o mapa primário — nunca editar depois de criado, só
ler. **É sempre o verbatim, nunca o resumo** (pedido do Julio em 22/09/2026): o resumo perde fala,
tom e detalhe que às vezes importa depois. Dia com volume grande de reuniões (ex.: primeira
importação depois de um tempo sem rodar) não é motivo pra trocar por resumo — só motivo pra ir
com calma, buscando o verbatim de cada uma mesmo que leve mais chamadas.

## 4. Descobrir de qual projeto é

Comparar o título e os participantes da reunião com as pastas de `clientes/`, `retencao/` e
`projetos/`. Confiante (nome do cliente aparece no título, ou participante já é ponto de contato
conhecido): segue pro passo 5. Sem confiança: **não inventar**. Deixar o arquivo bruto em
`_memoria/reunioes/` e listar como pendência no resumo da sessão ("reunião de tal dia, não sei de
qual projeto é — qual pasta?").

## 5. Destilar pro projeto

Seguindo o gatilho já existente do `AGENTS.md` (seção 4, "chegou material bruto"): abrir o
`contexto.md` do projeto certo e acrescentar o essencial — o que foi discutido, o que ficou
decidido, pendência nova — **com a data e o caminho do arquivo bruto como fonte** ("reunião
22/09 → `_memoria/reunioes/2026-09-22 - Nome.md`: o que fechou"). Nunca copiar a transcrição
inteira pro `contexto.md`: só o que importa pra trabalhar no projeto depois.

Se a reunião gerou decisão com motivo, ou pendência nova, isso também é candidato pra
`_memoria/decisoes.md` e pro `agora.md`/`andamento.md` — mas quem escreve isso é o `/atualizar`,
no fim da sessão. Aqui só anota (deixa registrado no `contexto.md`, que é do projeto e pode ser
escrito direto) e segue.

## 6. Fechar o dia sozinha (sem perguntar)

Diferente do resto do sistema, esta skill **não espera confirmação**: pedido do Julio em
22/09/2026, exatamente porque ela já roda sem ele precisar chamar nada. Depois do passo 5, rodar
o `/atualizar` (a skill inteira, ver mapa) **direto, sem mostrar o plano e sem esperar "aplico?"**:

- Diário do dia (dono, `_memoria/diario/AAAA-MM-DD.md`): um bloco com quantas reuniões vieram,
  quais projetos tocou, quais ficaram sem projeto identificado.
- `_contexto/agora.md`: só se alguma reunião mudou o "onde paramos" ou criou/resolveu pendência
  clara. Reunião solta sem decisão não move o agora.md.
- `_memoria/decisoes.md`: só se alguma reunião registrou decisão com motivo (não é o caso da
  maioria — a maior parte é operacional, não decisória).
- `andamento.md` do projeto, se a reunião mexeu num projeto com pendência nova ou resolvida.

Continua valendo o resto do contrato do `/atualizar`: não inventar destino (reunião sem projeto
claro segue em `_memoria/reunioes/` como pendência, nunca forçada num lugar), não duplicar linha,
data absoluta, diário sempre acrescenta.

## 7. Avisar, sem alarde

Uma resposta só, no fim: quantas reuniões vieram, de quais projetos, quais ficaram sem projeto
identificado, e o que o `/atualizar` automático escreveu (diário, e agora.md/decisões/andamento.md
só se algo mudou de fato). Sem reunião nova, não comentar nada.

## Regras

- Nunca apagar nem reescrever um arquivo de `_memoria/reunioes/` depois de criado.
- Nunca adivinhar o projeto de uma reunião só pra não deixar pendência — errar o cliente é pior
  que perguntar.
- O `/atualizar` desta skill é automático (regra acima), mas só nesta skill. Em qualquer outra
  situação da sessão, `/atualizar` continua pedindo "aplico?" como sempre.
