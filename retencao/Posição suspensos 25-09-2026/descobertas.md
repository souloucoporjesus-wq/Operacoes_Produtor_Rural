# Descobertas · recuperação de valores dos suspensos

Arquivo vivo. Cada planilha analisada ganha uma seção; o placar consolidado no fim soma tudo e é
atualizado a cada rodada. Tags de confiança: [Certo] está escrito na planilha, [Provável] é leitura
das observações, [Suposição] é premissa minha até alguém confirmar.

Página de apresentação gerada a partir daqui: `Recuperacao de valores 25.09.2026.html` (nesta pasta).

---

## Planilha 1 · Financeiro_VProdutores.xlsx (recebida 25/09/2026)

### Como a planilha está organizada

- 5 abas: Resumo, Geral, Inadimplencia (26 contratos), Churn (28), Em_Negociacao (10).
- Os 11 clientes informados pelo Julio estão todos na aba **Inadimplencia**. [Certo]
- Colunas que importam: `R$ Contrato` é a **mensalidade** (Paulo 1.261,92 x 2 = 2.523,84 de débito;
  Marcos 3.380,27 x 4 = 13.521,08 de represado; Tellus 2.202,97 x 10 = 22.029,70). [Certo]
  `(R$) Débito faturado` é o que foi faturado e não pago; `(R$) Valor represado` são os meses não
  faturados durante a suspensão; `Total Dívida` soma os dois. `OBS. CS` e `Obs Cobrança` trazem a
  negociação.
- Leitura conferida: os totais que calculei batem com a linha de soma da própria aba (26 contratos,
  R$ 105.157,81 faturado, R$ 223.122,45 represado, R$ 328.280,26 total, R$ 59.016,38 de mensalidade).
  [Certo]
- Erro na planilha: data de suspensão da Tellus aparece como 01/12/2002 (provavelmente 01/12/2025;
  378 dias de atraso). Não afeta valores. [Provável]

### Quanto os 11 clientes deviam na planilha?

| cliente | produto | mensalidade | faturado | represado | total na planilha |
|---|---|---:|---:|---:|---:|
| Marcos Aurelio Sinopoli | AGM | 3.380,27 | 0,00 | 13.521,08 | 13.521,08 |
| Vitor Marcio Dumoncel e outros | AGM | 4.876,60 | 0,00 | 9.753,20 | 9.753,20 |
| Luiz Moreira Rocha | myFarm | 2.500,00 | 20.862,90 | 0,00 | 20.862,90 |
| Paulo Massayoshi Mizote | AGM | 1.261,92 | 2.523,84 | 0,00 | 2.523,84 |
| Pablo Rafael Scnheider | AGM | 1.200,00 | 2.400,00 | 0,00 | 2.400,00 |
| Juarez Carlos Silva Filho | myFarm | 650,00 | 2.600,00 | 0,00 | 2.600,00 |
| Ana Paula Bandeira de Lima | myFarm | 565,00 | 2.531,68 | 0,00 | 2.531,68 |
| João Everton Paulino Ramos Alves | myFarm | 427,11 | 1.381,31 | 0,00 | 1.381,31 |
| Moacyr Brunetta | myFarm | 1.398,65 | 2.797,30 | 0,00 | 2.797,30 |
| Tellus Agropecuaria | AGM | 2.202,97 | 2.067,47 | 22.029,70 | 24.097,17 |
| Theodoro Ricardo de Andrade | myFarm | 850,00 | 1.700,00 | 4.250,00 | 5.950,00 |
| **total (n=11)** | | **19.312,52** | **38.864,50** | **49.553,98** | **88.418,48** |

### Como cada um foi negociado?

- **Paulo, Pablo, Juarez, Ana Paula, Moacyr**: pagamento integral do faturado. Juarez via pix 14/09,
  Moacyr via pix 24/09, Ana Paula via pix. Pablo pagou, mas pede a cobrança semestral que tinha sido
  combinada (foi lançada como mensal): ajuste de faturamento pendente. [Certo]
- **João Everton**: aceitou 15% de desconto; pagou R$ 1.174,11 (desconto de R$ 207,20). [Provável:
  a planilha diz "aceitou 15%" e "Pagou", não traz o valor pago]
- **Luiz Moreira Rocha**: acordo em entrada + 2 parcelas sobre R$ 20.862,90; entrada paga e
  confirmada. Considerei 3 partes iguais de R$ 6.954,30, sem desconto (a proposta de 15% era só pra
  pagamento à vista). [Suposição: confirmar valor da entrada e datas das parcelas]
- **Vitor Marcio**: novo acordo de R$ 34.629,79: entrada de R$ 10.000,00 paga em 23/09 + 3 x
  R$ 8.209,93 (25/10, 25/11, 25/12). [Certo] O acordo é maior que o represado da planilha
  (R$ 9.753,20), então ele consolida o saldo do acordo anterior (R$ 24.876,59) com o represado.
  [Provável] Na conta, a dívida tratada do Vitor é o valor do acordo.
- **Marcos Aurelio**: acordo fechado em 18/09 para as 4 parcelas represadas (06 a 09/2026,
  R$ 13.521,08); o débito faturado já estava em acordo com a Averbach e está sendo cumprido.
  A planilha não traz entrada nem parcelas. Contei os R$ 13.521,08 inteiros como "a receber".
  [Suposição: confirmar condições e se já entrou algum valor]
- **Tellus**: pagou o faturado (R$ 2.067,47), não aceitou o represado e pediu cancelamento; as notas
  do represado (R$ 22.029,70) estão sendo canceladas. [Certo]
- **Theodoro**: pagou todo o faturado em 16/09 (R$ 1.700,00), recusou o represado (R$ 4.250,00),
  cancelou e disse que vai tratar o restante na Justiça. Motivo declarado: cobrança do período em
  que ficou com o acesso bloqueado. [Certo]

### Quanto voltou, e em que forma?

| | valor |
|---|---:|
| dívida tratada (planilha, com o acordo consolidado do Vitor) | 113.295,07 |
| **recuperado (pago + acordado)** | **86.808,17** (76,6%) |
| · já em caixa | 34.748,70 (40% do recuperado) |
| · a receber em acordo (Vitor, Luiz, Marcos) | 52.059,47 |
| represado baixado (Tellus e Theodoro) | 26.279,70 |
| desconto concedido (João Everton) | 207,20 |

Conferência: recuperado + baixado + desconto = dívida tratada, cliente a cliente. [Certo, dado o
modelo acima]

**Leitura:** três quartos do que foi tratado voltou, mas só 40% disso está em caixa. O resto depende
de três acordos que vão até dezembro, dois deles com clientes de risco financeiro alto na própria
planilha (Marcos "recorrente em renegociações não cumpridas", Vitor com R$ 28,75 milhões em
anotações negativas). O valor em caixa é o número firme pra diretoria; o acordado precisa de
acompanhamento parcela a parcela. [Provável]

### Onde está a perda?

A perda está toda no represado de dois clientes que cancelaram. Desconto praticamente não foi usado
(um cliente, R$ 207,20). [Certo]

### O represado é o que separa quem fica de quem sai?

- 7 clientes deviam só faturado: os 7 pagaram ou fecharam acordo (5 integral, 1 com 15%, 1 parcelado).
- 4 deviam represado: 2 fecharam acordo (Marcos e Vitor, os dois AGM e já com histórico de
  renegociação), 2 recusaram o represado e cancelaram (Tellus e Theodoro).

**Leitura:** base pequena (n=4 com represado), então não é tendência, mas é coerente com o achado de
11/09 e 17/09: o represado cobrado depois, fora do acordo do escritório, gera contestação e empurra
o cliente pra saída. O Theodoro disse isso textualmente. [Provável]

### Quanta receita mensal fica na base?

- 9 contratos seguem na base: R$ 16.259,55 de mensalidade (reativação depende de cumprir o acordo
  no caso do Marcos e do Vitor). [Certo quanto ao valor; Provável quanto à reativação]
- 2 saem: R$ 3.052,97 de mensalidade (Tellus e Theodoro).

**Leitura:** o objetivo combinado em 16/09 era a continuidade do cliente, não só o caixa. Nesse
recorte, 9 de 11 ficaram. [Certo]

### Por produto

- AgriManager: 5 contratos, R$ 55.142,18 recuperados (puxado pelos acordos do Vitor e do Marcos).
- myFarm: 6 contratos, R$ 31.665,99 (puxado pelo Luiz, R$ 20.862,90).

### Quanto do pacote de inadimplência isso representa?

- 11 de 26 contratos (42%) com desfecho.
- Na dívida da planilha: R$ 88.418,48 de R$ 328.280,26 (27%).
- Seguem em tratativa 15 contratos com R$ 239.861,78, concentrados em Petras de Lima Telles
  (R$ 58.075,29, sem retorno), Alzir Pimentel (R$ 43.792,20, reunião 25/09 às 15h) e Pedro Fadel
  (R$ 35.736,48, proposta em análise). Os três somam 57% do que falta. [Certo]

### Pontos a confirmar antes do número final

1. Marcos Aurelio: condições do acordo de 18/09 e quanto já entrou.
2. Luiz Moreira Rocha: valor da entrada e datas das 2 parcelas.
3. Vitor Marcio: se o acordo de R$ 34.629,79 inclui mesmo o saldo do acordo anterior.
4. João Everton: valor efetivamente pago (R$ 1.174,11 com 15%).
5. Pablo Rafael: ajuste da cobrança para semestral.

### Pagamentos na planilha que não estão na lista do Julio (candidatos pra próxima rodada)

- **Anderson Peixoto** (aba Inadimplencia, linha 30, sem contrato nem valor): "Pgto realizado.
  Cliente da central de cobrança".
- **Marcelo Benedito Lara** (R$ 4.476,00 na Inadimplencia): a Relatorio_Inadimplentes diz "Débitos
  foram quitados integralmente. Agora tratar renovação".
- **Lucival Portilho Arantes** (aba Churn): "Cliente pagou hoje dia 16/09 15mil reais".
- **Beatriz Costa Franco** (aba Churn): "valor negociado em 2x de R$ 1000", repassado ao contas a
  receber.
- **João Batista Consentini Filho**: "Cumprindo acordo" com represado de R$ 10.688,86 fora do acordo.

---

### Correção: as cores das linhas (25/09)

Na primeira leitura eu disse que só o cabeçalho tinha cor. Estava errado: o script olhava só cor
em RGB e ignorava as cores do tema do Excel. [Certo]
- Financeiro_VProdutores, aba Inadimplencia: linhas **verdes** (tema accent6, clara) são exatamente
  os 9 que pagaram (linhas 5, 7, 10, 12, 13, 14, 15, 17, 29). Tellus, Falcon, Roni e Luiz Espindula
  têm preenchimento branco explícito (sem significado aparente).
- Relatorio_Inadimplentes: a única linha verde é a do Marcelo Benedito Lara ("débitos quitados
  integralmente").

### Novas evidências sobre os pontos a confirmar (varredura de 25/09)

Varri as duas planilhas (inclusive colunas ocultas J, K, L), a posição de 16/09, as 11 reuniões de
retenção, as 45 do Granola, diário, decisões, briefing e resumo do Teams. Cada achado foi conferido
por um segundo agente. Teams, Outlook e Granola não estavam conectados nesta sessão.
- **Marcos Aurelio**: nenhuma fonte traz entrada, parcelas ou datas do acordo de 18/09. A coluna
  oculta L ainda diz que o represado de R$ 13.521,08 está "fora acordo", então nem é certo que o
  acordo cubra o represado. [Suposição mantida por decisão do Julio em 25/09: "deixei dessa forma
  por hora"]
- **Luiz Moreira Rocha**: reunião de 17/09 com a Amanda (`retencao/reunioes/2026-09-17-clientes-
  suspensos-cobranca-negociacao-amanda.md`): cliente myFarm de cerca de R$ 20 mil ia pagar à vista,
  a cobrança propôs parcelamento no mesmo minuto e a cliente pagou só a entrada: "deixamos de
  receber 20 mil para receber 2.500". Se for ele, a entrada foi R$ 2.500, não R$ 6.954,30, e o
  caixa cai R$ 4.454,30. [Provável] Julio pediu para manter a estimativa por enquanto (25/09).
- **Vitor**: o acordo de R$ 34.629,79 não aparece em nenhuma fonte além da planilha de 25/09; em
  16/09 havia só promessa de pagamento para 21/09. A leitura "consolida o saldo do acordo anterior"
  segue [Provável].

---

## Plano Safra · o que ficou para 30/03 (25/09)

### Como a regra foi combinada [Certo, transcrições]

- 10/09: Julio passa ao CS a primeira versão: para valores muito altos, jogar para 30/04/2027 com
  confissão de dívida; para AgriManager muito alto, até duas datas (30/04 e 30/08).
  (`retencao/reunioes/2026-09-10-...`, l. 100 a 102)
- 11/09 com o financeiro: nota do represado emitida agora, boleto em 30/03 "com coeficiente de
  juros", confissão de dívida, out/nov/dez podem ir no mesmo boleto, mensalidade volta a faturar no
  mês seguinte. O financeiro pediu entrada mais um "balão" antes da virada do ano. Por que 30/03:
  colheita da soja começa por volta de 20/02 e os insumos vencem em 30/04, então a Aliare recebe
  antes. O financeiro contestou que 15% e Plano Safra estivessem combinados; o Leandro exigiu
  autonomia. (`2026-09-11-negociacao-inadimplentes-estrutura-debito.md`, l. 418 a 484)
- Entrada: "talvez 10%" dita como sugestão pelo Julio em 11/09 (`2026-09-11-cobranca-...-maicon.md`,
  l. 99). A planilha do financeiro fala em **20%** ("Flexibilizar para 2027, com entrada de 20%").
  Divergência não resolvida.
- 17/09: CEO dá autonomia a Leandro e Julio para tratar cada cliente (decisoes.md). Não cita o
  Plano Safra.
- 17/09 com a Amanda: Julio volta a falar em "30 do 4" e, quando ela lembra que a planilha diz para
  não oferecer, responde "esquece, isso já caiu". O `retencao/contexto.md` registrou "Opção 30 do 4
  cancelada", o que contradiz a regra de 11/09. [Provável] Caiu a proibição, não a opção.
- 23/09 (reunião Evoluto): Julio conta aos consultores que os clientes estão aceitando o plano
  safra com confissão de dívida e pagamento em 30/03.

### Quem está no Plano Safra [Certo, planilhas]

| cliente | situação | valor |
|---|---|---:|
| Marcos Aurelio Sinopoli | **acordo fechado** em 18/09 (planilha 3): represado para 30/03/2027, mensalidades e acordo anterior seguem | 13.521,08 |
| Pedro Henrique Pinto Fadel | **proposta** em análise: 5 x R$ 3.573,64 até fevereiro + R$ 17.868,28 em 30/03/2027 (cada parcela é 10% do débito) | 35.736,48 |
| Alzir Pimentel Aguiar Neto | candidato; reunião 25/09 15h; represado fora do acordo de 10x do escritório | 43.792,20 |
| Petras de Lima Telles | candidato previsto (sugestão do Julio em 17/09); cliente sem retorno | 58.075,29 |
| Nova Fronteira | financeiro indica "flexibilizar para 2027, entrada de 20%"; sem retorno | 4.955,97 |

Até a planilha 3, nenhum acordo fechado aparecia. Com ela, o Marcos é o primeiro, e o calendário da
página passou a ter março/2027. A recomendação do financeiro ("Não propor Flexibilização 2027") também
valia para o Marcos. [Certo]

**Ponto para o Julio, fora da página:** a coluna Y do financeiro diz "Não propor Flexibilização
2027" para Alzir, Marcos, João Batista, Vitor, Petras e Pedro Fadel (os 6 com risco alto na
análise de crédito). Essa recomendação já estava na planilha de 16/09. A proposta enviada ao Pedro
Fadel vai contra ela. Vale alinhar com o financeiro antes de fechar. [Certo]

---

## Planilha 2 · Relatorio_Inadimplentes.xlsx (recebida 25/09/2026)

### Como a planilha está organizada e se foi lida certo?

- 2 abas: Clientes_Inadimplentes (25 linhas) e CHURN (36 linhas), 61 linhas, **52 contratos
  únicos**. [Certo]
- Clientes_Inadimplentes: `DÉBITOS C JUROS` (a coluna `SEM JUROS` está vazia em todas), `STATUS`
  (NEGOCIAÇÃO COMERCIAL 4, CHURN 8, vazio 13) e `OBS CS`. CHURN: data da solicitação, receita mensal
  (`MRR`), analista do CS e observação. [Certo]
- Os valores de Petras, Alzir e Pedro Fadel estão formatados como data no Excel (ex.: 58.075,29
  aparece como 31/12/2058). O número gravado está certo. [Certo]
- Bug meu, corrigido: o script dos dossiês converteu em data todo número acima de 30.000. Os
  valores da página foram recalculados direto das planilhas, não dos dossiês. [Certo]

### Quem está repetido?

- **Dentro da Relatorio**, 9 contratos estão nas duas abas: Roni, Geraldo Mossignato, Ivan, Theodoro,
  Augusto, COAP, Falcon, Agro Aliança, Luiz Espindula. [Certo]
- **Entre as duas planilhas**: 49 dos 52 contratos da Relatorio também estão na Financeiro. Só na
  Relatorio: Marino Bortolas, Rogerio Ferrari (contrato cedido) e Nativa Agricultura. Só na
  Financeiro: os 9 que pagaram e mais 6 (Gemiro Carafini, Alvorada, Liseu Scherer, Leandro Gai,
  Knap e o 2º contrato do Lucival, Aliare Cloud). [Certo]
- **Leitura:** a Relatorio é a lista do que ainda está pendente. Os 9 que pagaram saíram dela; o
  Marcelo Lara ficou, pintado de verde.
- União das duas: **67 contratos distintos**, mais a linha sem contrato do Anderson Peixoto.

### Como cada contrato foi classificado?

Classificação feita por agentes, contrato a contrato, lendo todas as linhas das duas planilhas.
Cada lote passou por um verificador, e eu revisei o resultado. Mudei dois casos:
- **COAP**: a aba CHURN diz "contrato encerrado", mas a aba de inadimplentes diz "negociação
  comercial, não cobrar", o financeiro diz renovação anual 08/2026, e a COAP tem demanda ativa de
  produto (André, 24/09). Ficou em negociação comercial. [Provável]
- **Agropecuária Alvorada**: migrou do AgriManager para o myFarm (contexto 16/09). Ficou em
  negociação comercial, como migração, e não em churn. A mensalidade de R$ 1.859,64 ficou de fora
  da página porque o contexto de 16/09 diz que esse valor está errado. [Provável]

| grupo | contratos | valor |
|---|---:|---|
| Recuperação (aba 1) | 9 que ficam + Tellus e Theodoro | R$ 86.808,17 recuperados |
| Em aberto (carteira interna) | 5 | R$ 153.248,80 de dívida, 97% represado |
| Negociação comercial / migração | 8 | R$ 9.222,22 de mensalidade (sem Alvorada) |
| Escritório de cobrança | 6 + 1 quitado | R$ 57.599,67 de dívida |
| Churn | 37 (36 clientes; inclui Tellus e Theodoro) | R$ 52.990,61 de receita mensal |
| Sem pendência | 1 (Rogerio Ferrari, cedido) | · |

### Churn: onde está parado?

| etapa | contratos | receita mensal |
|---|---:|---:|
| Pagamento ou acordo feito | 6 | 9.501,21 |
| Distrato em assinatura | 6 | 8.678,19 |
| Aguardando pagamento de boletos | 6 | 7.421,36 |
| Sem etapa registrada | 6 | 2.595,27 |
| Multa em discussão com o cliente | 5 | 10.120,06 |
| Aguardando pagamento da multa | 4 | 7.973,65 |
| Aguardando retorno de contratos | 4 | 6.700,87 |

- **21 de 37** aguardam o cliente (multa, boletos ou assinatura). **4** aguardam contratos. [Certo]
- **4 pedidos com mais de 5 meses** sem distrato: Fernando Lunardi (10/10/2025), Fabio Carrapateira
  (01/12/2025), Pedro Bertuol (01/04/2026), Augusto Maia (08/04/2026). Só 14 dos 37 têm data do
  pedido. [Certo]
- **Motivo registrado em 8 de 37**; 3 deles citam falhas ou limitações do sistema (Augusto, Agro
  Aliança, Luiz Espindula). Base pequena, não é tendência. [Certo quanto aos números]
- **Débitos a acertar** no encerramento: R$ 37.249,31 em 4 contratos (Roni 1.678,29, Falcon
  13.859,02, Luiz Espindula 9.000,00, Augusto 12.712,00 com juros). [Certo]
- **Receita mensal do Lucival**: a Relatorio mostra R$ 5.896,12, que é a soma dos 2 contratos dele
  (AgriManager 4.248,62 + Aliare Cloud 1.647,50). Usei os valores por contrato. [Certo]
- Por produto: AgriManager 10 contratos (R$ 24.842,30), myFarm 25 (R$ 25.299,19), Aliare Cloud 2
  (R$ 2.849,12).

### Escritório de cobrança

- **Confirmados** (as duas planilhas dizem escritório): Fyllipe 15.927,50, Silvano 15.000,00, José
  Rosa 7.345,86. Total R$ 38.273,36. [Certo]
- **A confirmar** (o CS diz escritório, o financeiro diz carteira interna): Christopher 16.658,51,
  Henrique Reges 1.966,40, Marcia Coradini 701,40. Total R$ 19.326,31. [Certo]
- **Quitado pelo escritório**: Marcelo Benedito Lara, dívida registrada R$ 4.476,00. Valor pago não
  informado. [Certo]
- Todos são myFarm, e nenhum pediu cancelamento. [Certo]
- Em 3 casos o "com juros" do CS é igual ao "sem juros" do financeiro (juros não aplicados?). O
  Henrique tem 5 parcelas no CS e 4 no financeiro. [Provável]
- O escritório também conduz o **faturado** do Alzir (acordo de 10x) e do Petras (regularizado). O
  represado dos dois ficou fora e está em Em aberto. [Certo]

### Em aberto (carteira interna)

- 5 contratos, todos AgriManager, R$ 153.248,80. Represado R$ 148.292,83 (97%). [Certo]
- Petras, Alzir e Pedro Fadel somam R$ 137.603,97 (90%). [Certo]
- João Batista: cumpre acordo antigo, represado de R$ 10.688,86 fora. Nova Fronteira: só faturado,
  R$ 4.955,97, sem retorno. [Certo]

### Conflitos entre as planilhas (para o Julio, fora da página)

- Roni, Falcon e Luiz Espindula: churn no CS, inadimplência na carteira interna no financeiro.
- Waldyrene: churn na aba do CS, mas o financeiro registra que ela não quer cancelar (pausa de
  implantação). Ficou em negociação comercial.
- William Cardoso e Fernando Vieira Peres: churn no CS, "em negociação" no financeiro.
- Agro Aliança: data do pedido 28/05/2026 no CS, mas a observação cita email de 20/08/2026.
- Tellus: o CS diz que não há represado a cobrar, mas o financeiro ainda soma R$ 24.097,17 de dívida.
- Pedro Bertuol: o CS parou na retenção, e o financeiro já espera a assinatura do distrato (pedido de
  01/04/2026).

---

## Planilha 3 · Recuperacao_Mensal_Cobranca_2026-09.xlsx (recebida 25/09/2026)

### Como a planilha está organizada e se foi lida certo?

- 6 abas: Resumo, Clientes Recuperados (15 linhas, 25 colunas), Histórico Consolidado (52 eventos
  dos mesmos 15 clientes), Por CS-Agente, Por Produto, Evolução Mensal. Sem cores nas linhas. [Certo]
- É o relatório da central de cobrança: clientes cujo caso foi encerrado como **reativado** em
  setembro. A coluna `MRR Recuperado` é a mensalidade do cadastro do cliente, não o valor da dívida.
  [Certo, pela aba Resumo]
- Leitura conferida: a soma das 15 linhas bate com o Resumo (R$ 34.052,84, 15 clientes). [Certo]

### Quanto de MRR voltou, com o anual dividido por 12?

- A planilha soma os contratos **anuais** pelo valor cheio: Neimar Walker R$ 8.000,00 e Bruno Marques
  Guidi R$ 1.765,17. Divididos por 12: R$ 666,67 e R$ 147,10. [Certo]
- **MRR recuperado em setembro: R$ 25.101,44 por mês** (R$ 34.052,84 na planilha, sem dividir).
  Em 12 meses: R$ 301.217,28. [Certo]
- Da carteira de cobrança (11 contratos): R$ 21.210,26. **Extras** (4 contratos): R$ 3.891,18.
- 12 de 15 seguem ativos (R$ 17.245,53 por mês). Voltaram para a central: Luiz Moreira Rocha (tem
  parcelas de acordo), Anderson Peixoto (vencimento em 16/10) e Moacyr Brunetta (pagou em 24/09 e
  aparece em cobrança desde 25/09). [Certo quanto ao registro; Provável quanto ao motivo]
- Tempo mediano na central até a reativação: 23 dias. 9 reativações automáticas (o contrato voltou
  a ativo) e 6 registradas pela central. Nenhum passou pelo escritório. [Certo]

### Quem é extra (não estava nas planilhas anteriores)?

Cruzei os 15 pelo número do contrato e pelo nome com os 67 contratos das duas planilhas. [Certo]
- **Extras (4):** Neimar Walker (30002492, myFarm, anual), Agropecuária Mano Velho (30004920,
  AgriManager), Bruno Marques Guidi (30004903, myFarm, anual), Sandro Sia e Outros (30007323, myFarm).
- **Já estavam, pelo nome:** Anderson Peixoto Cordeiro (a linha 30 sem contrato da Financeiro) e
  Agropecuária Alvorada (que aparecia pelo contrato AgriManager 30004481 e agora voltou pelo contrato
  myFarm 30007726, depois da migração).
- **Já estavam, pelo contrato (9):** Luiz, Vitor, Marcos, Moacyr, Pablo, Knap, Juarez, Ana Paula,
  João Everton.
- **Paulo Massayoshi Mizote** pagou (planilha 1), mas não aparece na central. Fica sem MRR na página.

### O que a planilha 3 resolveu

- **Marcos Aurelio**: "os débitos represados o pagamento ficou para 30/03, Plano Safra"; o cliente
  segue pagando as mensalidades e o acordo anterior. É o **primeiro acordo fechado no Plano Safra**
  (R$ 13.521,08 para 30/03/2027). [Certo]
- **Luiz Moreira Rocha**: entrada de R$ 6.258,78 e duas parcelas de R$ 7.301,91 (14/10 e 14/11),
  total de R$ 20.862,60, sem desconto. A planilha escreve "entrada paga dia 16/10", mas a entrada
  vem antes da parcela de 14/10, e a posição de 16/09 já dava a entrada como paga: usei 16/09/2026.
  A diferença de R$ 0,30 para o débito de R$ 20.862,90 ficou como arredondamento. [Certo quanto aos
  valores; Provável quanto à data]
- A pista da reunião de 17/09 ("receber 2.500") não era o Luiz, ou era outro valor: descartada.

### Diferenças entre o MRR da central e a mensalidade da planilha 1

- Luiz Moreira Rocha: R$ 5.000,00 na central e R$ 2.500,00 na Financeiro.
- Marcos Aurelio: R$ 3.529,65 na central e R$ 3.380,27 na Financeiro.
- A página usa o valor da central para o MRR e o da Financeiro para a mensalidade da dívida. [Certo]

### Regra de não repetir cliente entre as abas (25/09)

- Tellus e Theodoro ficam só em **Recuperação** (pagaram o faturado), fora da lista de Churn. O texto
  do Churn cita os dois.
- Alvorada e Knap saem de negociação comercial e passam para **Recuperação**.
- Lucival Portilho (2 contratos, AgriManager e Aliare Cloud) virou **uma linha** no Churn, com
  R$ 5.896,12 de receita mensal. Nos totais por produto, cada contrato continua no seu produto.
- Resultado: 71 clientes, 72 contratos, e nenhum nome repetido nas listas (conferido na página).

### Outros dados da planilha que ficaram fora da página

- Evolução mensal da central: jun R$ 23.152,58 (6), jul R$ 28.853,17 (18), ago R$ 59.696,89 (23),
  set R$ 34.052,84 (15). Os meses anteriores não têm detalhe por cliente, então não dá para dividir o
  anual e comparar com setembro. [Certo]
- Taxa de recuperação do mês: 23% (15 de 64 que passaram pela central). Em cobrança hoje: 49
  clientes, R$ 89.602,79 de MRR.
- Por analista (para uso interno, não entrou na página): Amanda 7 clientes (R$ 15.204,93), Andrezza
  3 (R$ 11.163,82, inclui o anual cheio do Neimar), Giovanna 4 (R$ 6.226,83), Ana Flávia 1
  (R$ 1.457,26).

---

## Placar consolidado (atualizar a cada planilha)

**Dívida recuperada** (planilha 1, com os acordos confirmados pela planilha 3)

| fonte | contratos | recuperado | em caixa | a receber | não recuperado |
|---|---:|---:|---:|---:|---:|
| Financeiro_VProdutores, 11 clientes da lista (25/09) | 11 | 86.807,87 | 34.053,18 | 52.754,69 | 26.487,20 |

Mudou em 25/09 com a planilha 3: a entrada do Luiz é R$ 6.258,78 (antes estimada em R$ 6.954,30).
O a receber inclui R$ 13.521,08 do Marcos no Plano Safra (30/03/2027).

**MRR recuperado** (planilha 3, anual dividido por 12)

| origem | contratos | MRR por mês |
|---|---:|---:|
| Da carteira de cobrança | 11 | 21.210,26 |
| Extra, fora das planilhas | 4 | 3.891,18 |
| **total** | **15** | **25.101,44** |

**Candidatos a somar, aguardando decisão do Julio** (aparecem nas abas, fora do total):

| cliente | onde | o que a fonte diz | valor |
|---|---|---|---:|
| Lucival Portilho Arantes | churn | "pagou hoje dia 16/09 15mil reais" | 15.000,00 em caixa |
| Beatriz Costa Franco | churn | "negociado em 2x de R$ 1000", repassado ao contas a receber | 2.000,00 a receber |
| Marcelo Benedito Lara | escritório | "débitos foram quitados integralmente" | até 4.476,00 (valor pago não informado) |
| Anderson Peixoto | Financeiro, linha 30 | "Pgto realizado. Cliente da central de cobrança" | sem valor |
| Geraldo Mossignato | churn | valor em aberto e pix enviados; comprovante pendente | sem valor |
