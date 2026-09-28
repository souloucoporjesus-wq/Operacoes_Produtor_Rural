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

## O que o cliente mostrou (reunião 24/09/2026)
- Planilha de fluxo diário até 31/12 com previsto e realizado juntos (venda prevista de feijão e
  milho, provisão de combustível, folha, parcela do armazém), saldo por banco atualizado a cada 1 ou
  2 dias. Contas de matriz e filial separadas: querem **dois fluxos** (Mato Grosso e Paraná, por empresa)
- **Dólar**: aba só com o que têm a pagar e receber em dólar (custeio e Finame em moeda estrangeira
  até 2029) pra ver se as operações estão casadas. Cicilio vai fazer uma aba própria de dólar e um
  filtro de moeda no detalhamento diário
- Vendas por safra (soja e milho 26 e 27): o comprometido reduz o estoque disponível; o previsto vai
  sendo consumido pelo realizado até fechar a colheita
- **Pedido novo: alerta de contrato** com saldo a entregar ou receber no prazo. Caso real: 36 t de
  adubo (perto de US$ 30 mil) chegaram 90 dias depois sem conferência. Julio: dá pra fazer o alerta no
  Vista já (pedido ou ordem de compra contra a nota: data, valor, quantidade, produto) como solução
  imediata; Cicilio vai ver os alertas de programação de compras do AgriManager Web
- **Venda em papel** (bolsa, NDF) é contrato com banco, só financeiro, sem volume físico: lançar no
  próprio Vista, como a simulação de venda, e não no ERP
- Princípio acertado: lançar a informação uma vez só (a planilha deles repete o mesmo dado em várias abas)
- Próximo passo: quando houver protótipo real, ele sobe no Vista do cliente; Andrezza atualiza e agenda
- Previsão dada pelo Julio a outro cliente (João Osório, 24/09): painel de fluxo de caixa disponível
  no Vista até 15/10/2026

## Conversa interna depois da reunião (24/09/2026)
- O "descasamento de moeda" do cliente não é o padrão de mercado, mas está próximo
- Risco técnico: o Vista pode não ter filtro de sim ou não (informação do Alisson); o Diego vai
  procurar recurso. Julio sugeriu chamar o Gabriel (Sampaio), do Vista, pra revisar o painel
- Intenção do Cicilio: o painel sair sem custo pro cliente; vendo valor, o cliente passa a alimentar
  o AgriManager (e contrata horas de CS pra isso)

## Fontes
- Reunião 18/09/2026, protótipo de painel de fluxo de caixa, com Cristiano e Fabiane →
  `reunioes/2026-09-18-prototipo-bi-fluxo-caixa.md`: tudo acima
- Reunião 24/09/2026 com Cristiano, Fabiane e Carmen →
  `_memoria/reunioes/2026-09-24-grupo-bocchi-vistra-fluxo-caixa-dolar-alertas.md`: planilhas, dólar,
  alerta de contrato, venda em papel
- Conversa 24/09/2026, Julio e Cicilio → `_memoria/reunioes/2026-09-24-grupo-bocchi-vistra-filtros-cicilio.md`:
  filtros do Vista e intenção de entregar sem custo
