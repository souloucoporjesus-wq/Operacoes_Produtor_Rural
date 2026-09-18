# Contexto · Grupo Bocchi

## Quem é quem
- **Cristiano**: contato do cliente, decide sobre o painel
- **Fabiane**: financeiro do cliente, entra nas validações de fluxo de caixa
- **Moisés** (~76 anos): usuário final do painel no dia a dia; hoje usa planilha de Excel e só
  mexe no celular, não no computador — ponto de atenção pra usabilidade mobile
- **Cicilio Manfroi**: lidera a demo e o desenvolvimento do painel (lado Aliare)
- **Andrezza Perroni**: organiza agenda com o cliente e libera acesso ao Vista BI
- **Julio**: participou da reunião, fez a provocação sobre financiamentos bancários

## Por que existe
Numa agenda anterior o cliente pediu uma visão de fluxo de caixa dentro do sistema (hoje controla
isso em planilha Excel). A Aliare montou um protótipo do painel Vista BI e apresentou em
18/09/2026 pra validar se faz sentido antes de mandar pra esteira de desenvolvimento.

## O que foi combinado (reunião 18/09/2026)
- Protótipo mostrado: painel de fluxo de caixa com saldo atual, entradas e saídas previstas,
  estoque disponível, saldo projetado, gráfico de colunas, contas a pagar/receber (vencidas e a
  vencer) e quadro de alertas (ex.: falta de recurso pra pagar uma conta por venda ainda não
  programada)
- Visão mensal e diária, com colunas de previsão e orçamento vindas do AgriManager (dá pra
  ligar/desligar cada uma na visualização)
- Aba de simulação: permite lançar safra futura ainda não plantada, vendas futuras e provisões de
  entrada/saída sem precisar cadastrar tudo no AgriManager primeiro; o Vista cruza com o que já
  foi vendido/plantado de fato pra não duplicar a previsão
- Pontos que o cliente pediu pra incluir:
  - Dólar (cotação manual ou puxada automaticamente; aba de "descasamento de moeda")
  - Detalhamento geral por dia/mês com entradas e saídas juntas (hoje vem separado)
  - Financiamentos bancários com detalhamento: contrato, parcelas, vencimentos, taxa de juros e
    valor da parcela (provocação do Julio)
  - Operações na bolsa/BMF (venda a termo, trava de dólar futuro) pra casar com o físico depois
- Em aberto: como o painel vai funcionar no celular pro Moisés (76 anos, só usa celular). Solução
  provisória enquanto não desenvolve versão mobile: agendar ou disparar pelo Vista BI o envio de
  imagem/PDF estático do painel
- Cicilio já vai liberar acesso ao Vista BI pro Cristiano e pra Fabiane, pra eles explorarem os
  painéis existentes e compararem com as planilhas que usam hoje
- Andrezza vai organizar nova agenda (cliente sugeriu semana de 21/09/2026) pra mostrar a evolução
  do protótipo com os pontos incluídos

## Fontes
- Reunião 18/09/2026, protótipo de painel de fluxo de caixa, com Cristiano e Fabiane →
  `reunioes/2026-09-18-prototipo-bi-fluxo-caixa.md`: tudo acima
