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

## Apresentação ao CS (28/09/2026)

- O CS marca "Prioridade CS" nos clientes que precisam de atenção de produto, independente do
  volume de tickets; a marcação joga o cliente pro topo como crítico
- Citados na reunião: Sementes Vitória (entrar na lista), Rise (Rio Verde, carteira da Andrezza),
  3 Coqueiros (89 tickets de erro de produto), AgroJem e Agromantova (formadores de opinião;
  Agromantova com 216 tickets, muitos de dúvida, pede treinamento), grupo Mistos (prioridade);
  Walker saiu da base, não priorizar
- Ideia vinda do CS: o suporte travar atendimento de dúvida e forçar treinamento
- Só AgriManager por enquanto. MyFarm pede outro caminho: cruzar por email no Movidesk, porque lá
  não há código de grupo econômico pra todos os clientes
- Julio leva a lista pro time de dev no mesmo dia

## Fontes

- Reunião 28/09/2026 com o CS → `_memoria/reunioes/2026-09-28-priorizacao-clientes-criticos-tickets-cs.md`:
  marcação de prioridade e clientes citados
- 28/09/2026 → `dados/Lista de Clientes.xlsx` e `dados/Analise de tickets abertos.xlsx`:
  arquivos brutos recebidos do Julio pra essa análise
