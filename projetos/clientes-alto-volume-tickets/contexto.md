# Contexto · Clientes com alto volume de tickets

## Por que existe

A equipe de dev pediu um levantamento dos clientes que abrem muitos tickets, pra priorizar
atenção de desenvolvimento a eles.

## Dados disponíveis (`dados/`)

- **`Lista de Clientes.xlsx`** (796 linhas): carteira de contratos — código e nome do cliente,
  grupo econômico, valor do contrato, cidade/estado, gerente de conta, agente de
  relacionamento, data do contrato, periodicidade, produto, segmento e situação do contrato
  (ativo, suspenso etc.)
- **`Analise de tickets abertos.xlsx`** (20.587 linhas): histórico de tickets — número,
  prioridade, produto, squad, tipo, datas de abertura/resolução/fechamento, SLA, grupo
  econômico, vertical, status, departamento, agente, categoria, motivo, causa, avaliação,
  níveis de serviço e assunto

A chave de cruzamento entre as duas planilhas é o grupo econômico / cliente (conferir nome
exato da coluna em cada uma antes de cruzar: "NOME_GRUPO"/"COD_CLIENTE" na lista de clientes,
"Grupo Econônomico"/"ID Grupo Econômico" na de tickets).

## Fontes

- 28/09/2026 → `dados/Lista de Clientes.xlsx` e `dados/Analise de tickets abertos.xlsx`:
  arquivos brutos recebidos do Julio pra essa análise
