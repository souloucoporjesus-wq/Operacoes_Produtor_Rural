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

## Reunião de churn e retenção com produto e suporte (28/09/2026, 15:04)

- Participantes na transcrição: Diego Viana, Joice Magalhaes, Gustavo Silva, Fernanda Lima,
  Patrícia e Julio. Julio apresentou a planilha de tickets (só AgriManager, extração desde
  01/01/2025, revisada à mão pelo CS pra reduzir a lista)
- Gustavo: volume de ticket e melhoria não prova risco de churn; o que pesa é sinal qualitativo de
  que o cliente vai trocar de sistema (citou HSA Agro e Santa Cândida, que estariam indo pra
  Conecter, e Morinaga, que não está na lista mas vive crítico). Objetivo lembrado: não ter baixa
  até o fim do ano, com uma lista curta acompanhada de perto
- Pouco ticket também pode ser sinal (cliente desengajado). Julio: falta um score do cliente
  cruzando uso, ticket, financeiro e QBR, provocação que o Leandro já fez
- Combinado: Julio inclui na planilha uma coluna "cliente falando de churn" (Sim/Não); alerta pro
  churn silencioso (Franciose foi saída sem aviso e depois voltou)
- Relatório de churn: o filtro myFarm/AgriManager não muda os números (erro do Julio, vai corrigir);
  pedido de separar motivo por mês e por produto e de compartilhar a planilha de base
- Fernanda (produto myFarm): mapeando bugs reabertos com os desenvolvedores (causa raiz por
  módulo), myFarm abre uns 30 bugs de cliente por mês; pediu a Julio e Joyce a lista dos clientes
  myFarm que mais abrem ou reabrem ticket, pra priorizar e devolver ao cliente o que foi corrigido
- Patrícia: falta posicionamento de produto pro AgriManager; Diego: estratégia do AGM desktop é
  sustentação e customização, inovação vai pro AGM Web
- NPS: a Track não obriga comentário; troca de plataforma de NPS em andamento; o CS faz contato
  com detrator do mês sem influenciar a nota

## Fontes

- Reunião 28/09/2026 com produto e suporte → `_memoria/reunioes/2026-09-28-churn-clientes-priorizacao-retencao-cs.md`:
  critério de risco, coluna de churn, lista myFarm pedida pela Fernanda

- Reunião 28/09/2026 com o CS → `_memoria/reunioes/2026-09-28-priorizacao-clientes-criticos-tickets-cs.md`:
  marcação de prioridade e clientes citados
- 28/09/2026 → `dados/Lista de Clientes.xlsx` e `dados/Analise de tickets abertos.xlsx`:
  arquivos brutos recebidos do Julio pra essa análise
