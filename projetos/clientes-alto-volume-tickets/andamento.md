# Andamento · Clientes com alto volume de tickets

## Onde está

Análise concluída em 28/09/2026. Notebook em `analise-tickets.ipynb` (raciocínio completo). A
planilha entregue fica em `retencao/usuarios-por-produto-2026-09-24/Analise Clientes - Volumetria
de Tickets.xlsx` (gerada por `gerar_planilha.py`; textos das notas de cada coluna em
`definicoes_planilha.py`): score por cliente, urgência, categoria em destaque e uma aba por
categoria de ticket, com coluna "Prioridade CS" pra marcação humana (34 clientes marcados em
28/09). Regerar a planilha mantém as marcações de Prioridade CS.

## Pendências

- [ ] Julio: levar a planilha "Analise Clientes - Volumetria de Tickets" ao time de dev e alinhar os próximos passos
      (rotinas do sistema que mais geram erro de produto) — desde 2026-09-28
- [ ] CS: usar a aba "Fila de atendimento" e marcar "Sim" em "Prioridade CS" nos clientes que a
      análise humana decidir priorizar — desde 2026-09-28
- [ ] Julio: montar a versão myFarm do levantamento, cruzando os tickets do Movidesk por email do
      cliente (lá não há grupo econômico pra todos) — desde 2026-09-28

## Feito
- 2026-09-28: planilha apresentada ao CS, que passou a marcar a Prioridade CS
