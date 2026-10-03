---
name: analise_projetos
description: >-
  Atualiza e analisa o painel de acompanhamento dos projetos de implantação hunter (myFarm e
  AgriManager) a partir da exportação do CES: cruza as abas Projetos, Hr Adquirida, OS executada,
  OS planejada e Implantador, calcula horas adquiridas, usadas e saldo, dias em aberto, última e
  próxima agenda, última OS executada, fase da jornada, saúde e ordem de ataque de cada projeto, e
  gera o painel em HTML que abre direto no navegador, na página inicial (visão sintética com TMI,
  estoque de horas parado, planejado e dos suspensos, vazão da carteira, horas realizadas e carteira
  de hoje, num período à escolha) e com menu lateral para as seções Visão geral, Projetos a atacar,
  Prioridades, Projetos, Agenda dos projetos, Agenda dos consultores, Agendas realizadas e Pessoas,
  com página própria de cada projeto aberta em nova aba e botão Histórico com as anotações dos
  reports das analistas. O atualizar-painel.bat faz tudo isso sem IA. Use sempre que o usuário chamar /analise_projetos
  ou falar em painel de projetos, projetos de implantação, projetos hunter, exportação do CES,
  saldo de horas dos projetos, horas usadas, última agenda, próxima agenda, última OS, projetos
  parados, projetos por encerrar, quais projetos atacar primeiro, carteira de implantação,
  analista ou consultor de projeto, agenda dos consultores, agendas realizadas no período, horas
  por consultor, projetos a atacar, dias sem agenda, data de início do projeto, filtro por consultor
  ou por papel do consultor, report de projetos, anotações ou histórico do
  projeto, HandOff, saldo financeiro, hora entregue sem faturar, TMI, tempo médio de implantação,
  tempo até o go live, vazão, entradas e encerramentos, estoque de horas, horas paradas, horas
  planejadas, horas dos suspensos, página inicial ou visão sintética do painel, menu lateral,
  mesmo sem dizer "skill". Não confundir com /painel (pendências do sistema).
---

# /analise_projetos · painel dos projetos de implantação hunter

O painel mostra ao Julio, projeto a projeto, onde cada implantação está, quanto de hora sobra, há
quanto tempo não tem agenda, qual foi a última OS executada, o que está marcado e por onde atacar.
Tudo mora na **pasta do painel de projetos** (ver o mapa do `AGENTS.md`). O painel é um HTML único
com dados e gráficos embutidos: abre direto do arquivo, sem servidor e sem internet. Abre sempre na
**página inicial** (visão sintética, pedido do Julio em 03/10/2026) e navega pelas seções num
**menu lateral** à esquerda, no lugar das abas que ficavam no topo.

O método de análise é o da skill `analise_dados_senior`: uma pergunta por vez, resultado conferido
antes de virar conclusão, interpretação em vez de repetir número. Pergunta nova entra no notebook
acima da conclusão, e a conclusão é atualizada.

## O que tem na pasta

| arquivo | papel |
|---|---|
| `*.xlsx` (hoje `Ces-Julio_.xlsx`) | exportação do CES; o painel usa a mais nova que tenha as abas do CES (Projetos, Hr Adquirida, OS_EXECUTADA, OS PLANEJADA, STATUS_ATUALIZACAO), então os reports na pasta não atrapalham |
| `Report Projetos *.xlsx` (opcional) | reports das analistas: anotação de andamento, HandOff, analista de sucesso, horas, faturado e saldo financeiro por projeto (ver "Reports das analistas") |
| `importar_reports.py` | lê os reports e grava `historico-projetos.json`; roda com IA, fora do .bat |
| `historico-projetos.json` | o histórico acumulado das anotações; o `gerar_painel.py` lê e o .bat mantém no painel |
| `modelo.py` | regras e cálculos: filtro hunter, horas, agendas, fase, saúde, prioridade. Os limites de saúde ficam no topo |
| `gerar_painel.py` | monta os dados, embute no modelo da página e grava `painel-projetos-hunter.html`. O bloco `inicio` dos dados (todos os hunter, inclusive encerrados e cancelados, com abertura, entrega, primeira agenda, primeira agenda de go live, horas adquiridas e usadas, e as horas realizadas por dia desde 2024) alimenta a página inicial; os outros blocos não mudaram. No fim imprime os números de cabeça da página inicial (`resumo_inicio`) |
| `painel_template.html` | a página (CSS e JavaScript), com os marcadores `/*__PLOTLY__*/` e `/*__DADOS__*/`; os indicadores da página inicial são calculados aqui (`indicadoresPeriodo`, `partesEstoque`, `renderInicio`) |
| `atualizar-painel.bat` | dois cliques: acha o Python (lançador `py`, `python` do PATH ou a instalação do usuário), instala pandas, openpyxl e plotly se faltar, roda `gerar_painel.py` (repassa os argumentos: `atualizar-painel.bat --sem-abrir` só gera) e abre o painel na página inicial; a janela mostra os números de cabeça (TMI, entradas, entregues, vazão e estoque de horas total, parado, planejado e dos suspensos) e fecha em 20 segundos. Faz a análise inteira sem IA. Se der erro, avisa em português e o painel anterior fica intacto. Vai pro GitHub desde 02/10/2026 (`!*.bat` no `.gitignore`; antes ele não viajava entre as máquinas) |
| `analise-projetos-hunter.ipynb` | a análise pergunta a pergunta, com as conclusões |
| `painel-projetos-hunter.html` | o painel gerado (não editar à mão) |

## As seções do painel (menu lateral)

O menu fica à esquerda, em três grupos: Carteira (Visão geral, Projetos a atacar, Prioridades,
Projetos), Agenda (Agenda dos projetos, Agenda dos consultores, Agendas realizadas) e Time
(Pessoas), com o Início no topo e a data de posição do CES no pé. "Recolher menu" deixa só os
ícones (fica lembrado no navegador). Abaixo de 1024px o menu vira gaveta, aberta pelo botão Menu da
barra do topo. O painel sempre abre no Início; `#geral`, `#prioridades` etc. no endereço abrem
direto a seção. O título da página mostra a seção atual.

| seção | o que mostra |
|---|---|
| Início (visão sintética) | o resumo para abrir o dia, com período à escolha (últimos 12 meses, este ano, ano passado, desde 2024) comparado com o período anterior: **prazo** (TMI em destaque, por sistema e com mediana; até a primeira agenda; até o go live; acima do prazo normal), gráfico do TMI mês a mês e leitura rápida em frases; **estoque de horas** hoje (total, parado, planejado, dos suspensos, sem fechar, livre) e a barra "onde está o estoque" por situação; **vazão** (entradas, entregues ao suporte, vazão, saldo da carteira, cancelados, meses para entregar a carteira); **horas realizadas e consumo** (realizadas e por mês, consumo no encerramento, horas que sobraram, horas por projeto entregue); **carteira hoje** (em aberto, idade média, sem próxima agenda, já passaram do go live, agendas nos próximos 30 dias, agendas vencidas) e os atalhos "Por onde atacar", que abrem a aba Prioridades no grupo |
| Visão geral | números da carteira, onde está cada projeto (dias sem agenda × horas usadas), saúde, fase, evolução desde 2025 |
| Projetos a atacar | o resumo de bater o olho: só os em andamento sem nada marcado, com os dias sem agenda em destaque, em duas listas (retomar a implantação e encerrar ou usar o saldo) e as faixas até 30, 31 a 90 e mais de 90 dias |
| Prioridades | a fila de ataque: início do projeto, última agenda, última OS executada, próxima agenda e saldo de cada projeto; filtros próprios de início do projeto (Todos, Últimos 90 dias, os dois anos mais recentes, "Antes de" e datas De/Até) e de consultor com o papel dele no projeto; cartões, tabela e CSV seguem os filtros |
| Projetos | a tabela completa dos hunter em aberto |
| Agenda dos projetos | próximas agendas, planejadas que venceram e OS sem fechar dos projetos hunter |
| Agenda dos consultores | grade semanal consultor × dia com todas as OS (hunter e farmer), navegação por semana; só entra quem tem agenda na semana; o mouse num bloco mostra horário de início e fim, OS, etapa e horas, e os blocos do dia seguem a ordem do horário |
| Agendas realizadas | o que aconteceu no período, com botões de 7 a 90 dias, mês e datas De/Até (até 366 dias pra trás), com o horário de cada agenda (também no CSV) |
| Pessoas | analistas e consultores: carteira, horas em 90 dias, responsável no cadastro × quem atende |

Todas as tabelas ordenam clicando no título da coluna. Clicar num projeto hunter em aberto abre a
**página do projeto numa nova aba** (pedido do Julio em 02/10/2026): é o mesmo arquivo do painel com
`#p<código>` no endereço, então funciona offline e não gera um arquivo por projeto. A página traz:
cabeçalho com cliente, grupo econômico, local, manutenção, analista, consultor responsável,
vendedor e posição na fila; o que pede ação; abertura, horas adquiridas, usadas, saldo, última e
próxima agenda; **ritmo do projeto** comparado aos hunter concluídos do mesmo sistema (primeira
agenda, agendas que aconteceram, maior pausa entre agendas, parado agora em vezes a maior pausa
típica); jornada por fase; gráficos (evolução do consumo, para onde vão as horas adquiridas, horas
por mês, horas por fase deste projeto × concluídos, linha do tempo das agendas por fase e
situação); quem atendeu; pacotes de horas; histórico dos reports; e a tabela de agendas com
horário. Quando há histórico importado, as listas de Projetos a atacar, Prioridades e Projetos
mostram o botão "Histórico" (abre só as anotações, sem sair do painel) e a marca "report:
encerramento" ou "report: cancelado" quando o report diverge do CES; os Destaques contam os
projetos em encerramento no report e a hora entregue sem faturar. Atalhos de endereço:
`#p<código>` abre a página do projeto e `#h<código>` abre o histórico.

## Regras combinadas com o Julio (02/10/2026)

- **Hunter** = tipo implantação ou reimplantação, nos departamentos CES Implantação AgriManager e
  CES Implantação myFarm. Farmer (treinamento, consultoria, DBA, horas avulsas) fica para depois.
- **Em aberto** = em andamento e suspenso (não iniciado e pendência entram se aparecerem).
- **Hora usada** = só OS fechada, validada ou acertada (concluída, no sistema antigo). Agenda
  confirmada que já passou sem OS fechada aparece à parte, como "sem fechar".
- **Analista de projeto** = coluna GERENTE. **Consultor responsável** = coluna RESPONSAVEL. Quem de
  fato atendeu vem das OS.
- **Encerramento formal** = `DT_ENTREGA_SUPORTE` (entrega pro suporte). `DT_FINAL` é só o fim da
  execução. A referência de "tempo normal" usa os hunter concluídos desde 2024, por sistema.
- **Saúde:** Crítico (parado antes do go live há mais de 30 dias sem nada marcado, 90% das horas sem
  go live, ou horas estouradas); Encerrar (go live feito e mais de 30 dias sem agenda e sem nada
  marcado); Atenção (15 a 30 dias sem agenda, 75% das horas sem go live, agenda vencida, OS sem
  fechar, aberto além do normal); Em dia; Suspenso.
- **Prioridade (ordem de ataque):** Crítico sem agenda, depois Sem agenda marcada (ainda
  implantando), depois Encerrar, depois Com agenda marcada, por último Suspenso; dentro do grupo,
  saúde mais grave e mais dias sem agenda primeiro.
- **Agenda dos consultores e agendas realizadas** usam todas as OS da exportação (hunter e farmer:
  treinamento, consultoria, DBA e outros), com o botão "Só hunter". Horas contam realizada, sem fechar
  e marcada; planejada que passou sem execução aparece riscada e não soma.
- **Cores fixas:** myFarm laranja, AgriManager verde (pedido do Julio em 02/10/2026). No tema claro
  `#f08c3c` e `#1a7f4b`, no escuro `#d9782c` e `#187542`: são as variações que passam no teste de
  daltonismo (o laranja e o verde "puros" ficam iguais pra quem não distingue vermelho e verde).
  Entradas e encerramentos usam azul e magenta. Saúde usa as cores de status, sempre com ícone e
  rótulo.
- **Horário da agenda:** na OS executada vem de PRIMEIRA/SEGUNDA ENTRADA e SAÍDA DIURNO e ENTRADA/SAÍDA
  NOTURNO; na OS planejada, de HORA_INICIO/FIM da manhã e da tarde. 00:00 é campo vazio. Início é o
  primeiro horário do dia e fim o último; com dois períodos, o painel mostra os dois ("Das 08:00 às
  18:00 (08:00 às 12:00 e 13:00 às 18:00)"). Em 01/10/2026 o horário vinha em 100% das agendas que
  aconteceram, batia com as horas lançadas, e faltava em 5% das marcadas ("horário não informado no
  CES").
- **Régua de ritmo da página do projeto:** vem dos hunter concluídos desde 2024, por sistema
  (`_referencia` e `_fases_referencia` em `modelo.py`). Em 02/10/2026: primeira agenda em 10 a 13
  dias depois da abertura; maior pausa entre agendas de 56 dias (myFarm) e 104 (AgriManager);
  treinamento e simulação com cerca de um terço das horas e parametrização com 20% a 28%. Parar não
  separa quem conclui; ficar parado sim (críticos e por encerrar estavam parados há 139 a 223 dias).
- **Fase** = a mais avançada entre as agendas que aconteceram; as etapas das duas metodologias são
  traduzidas para sete fases em `fase_da_etapa` (`modelo.py`).
- **Filtros da aba Prioridades** (pedido do Julio em 02/10/2026): **início do projeto** = data de
  abertura no CES (`DT_INICIAL`, a mesma "abertura" da página do projeto), com botões e datas De/Até
  (dá para usar só uma das pontas). **Consultor** é o mesmo filtro do topo (escolher num muda o
  outro), e a aba acrescenta o **papel**: em qualquer papel, responsável no cadastro, atendeu o
  projeto, atendeu por último (consultor da última OS executada) ou tem a próxima agenda. O filtro de
  consultor do topo vale em qualquer papel, e passou a incluir quem tem a próxima agenda. "Limpar
  filtros da aba" zera início, papel, consultor e o cartão escolhido; "Limpar filtros" do topo também
  zera os da aba. Em 02/10/2026: 49 abertos em 2026, 28 em 2025 e 6 antes (todos suspensos).

## Indicadores da página inicial (pedido do Julio em 03/10/2026)

Nenhuma métrica das outras seções mudou: os blocos de dados antigos saem idênticos (conferido em
03/10/2026, aba por aba, contra o painel anterior). As contas abaixo estão em `painel_template.html`
e repetidas em Python no notebook (pergunta "Quanto tempo leva uma implantação (TMI)") e no
`resumo_inicio` do `gerar_painel.py`; mudou uma, mudar as três e conferir que batem.

- **Recorte:** prazo, vazão e horas realizadas usam todos os hunter (inclusive encerrados e
  cancelados) e seguem só o filtro de sistema. Estoque de horas e carteira hoje são os projetos em
  aberto e seguem todos os filtros do topo.
- **Período:** últimos 12 meses (padrão), este ano, ano passado ou desde 2024, sempre até a data de
  posição do CES. Comparação: 12 meses anteriores, mesmo período do ano anterior, o ano antes do ano
  passado; "desde 2024" não compara. A seta é vermelha quando piorou e verde quando melhorou.
- **TMI (tempo médio de implantação):** média de dias da abertura (`DT_INICIAL`) até a entrega pro
  suporte (`DT_ENCERRAMENTO`, a mesma data dos encerramentos da Visão geral), dos hunter concluídos
  com entrega no período. Mostra também a mediana e o TMI de cada sistema. Atenção: quando a fila de
  encerramento anda, entram projetos antigos e o TMI sobe; ler junto com "abertos há mais de 1 ano".
- **TMI mês a mês:** cada ponto é o TMI dos entregues nos 12 meses até o fim daquele mês, desde
  jan/2025; com menos de 3 entregues o ponto fica vazio.
- **Até a primeira agenda:** mediana de dias da abertura à primeira agenda que aconteceu, dos
  abertos no período (sem cancelados) que já tiveram agenda. **Até o go live:** mediana de dias da
  abertura à primeira agenda de go live, dos projetos (sem cancelados) com go live no período. Só
  63% dos concluídos desde 2024 têm agenda de go live registrada.
- **Acima do prazo normal:** em andamento abertos há mais tempo que 75% dos concluídos do mesmo
  sistema (a mesma régua da saúde Atenção).
- **Entradas:** abertos no período sem os cancelados (o mesmo número do gráfico de entradas da Visão
  geral). **Entregues ao suporte:** concluídos com entrega no período. **Vazão:** entregues ÷
  entradas (acima de 100% a carteira diminui). **Cancelados:** entre os abertos no período (o CES não
  tem data de cancelamento, então a conta é pela safra de abertura). **Meses para entregar a
  carteira:** em andamento hoje ÷ entregues por mês no período.
- **Horas realizadas:** OS fechadas, validadas e acertadas no período, sem os projetos cancelados (o
  mesmo número do gráfico mensal da Visão geral). **Consumo no encerramento:** horas usadas ÷
  adquiridas dos entregues no período. **Horas que sobraram:** adquiridas e não usadas pelos
  entregues. **Horas por projeto entregue:** média de horas usadas.
- **Estoque de horas:** total = soma do saldo dos abertos (o mesmo "Saldo de horas" da Visão geral).
  **Parado** = saldo dos em andamento há mais de 30 dias sem agenda e sem nada marcado (o mesmo corte
  de "Parados há +30 dias"). **Planejado** = horas das próximas agendas marcadas. **Dos suspensos** =
  saldo dos suspensos. **Sem fechar** e **livre** como na página do projeto. A barra "onde está o
  estoque" separa o saldo positivo em cinco situações: com agenda marcada, sem nada marcado até 30
  dias, parado antes do go live (bate com "Crítico sem agenda"), parado depois do go live (bate com
  "Encerrar") e suspensos; projeto com saldo negativo fica fora da barra e é citado no texto.
- **Números de 03/10/2026** (posição de 01/10/2026, últimos 12 meses): TMI de 330 dias (mediana de
  341; 12 meses anteriores: 252), myFarm 317 e AgriManager 376; 26 entregues para 71 entradas, vazão
  de 37% (era 151%); 34 meses para entregar os 73 em andamento; primeira agenda em 8 dias e go live
  em 51; estoque de 1.764h, com 526h paradas (382h depois do go live), 663h planejadas e 378h nos
  suspensos; 2.342h realizadas (2.707h antes).

## Passo 1. Receber a exportação

O Julio exporta do CES a planilha com as abas Projetos, Hr Adquirida, OS_EXECUTADA, OS PLANEJADA,
IMPLANTADOR e STATUS_ATUALIZACAO e salva na pasta. A data de posição do painel vem de
STATUS_ATUALIZACAO. Cada aba tem duas linhas de título antes do cabeçalho e colunas no formato
`Tabela[COLUNA]` (o `modelo.py` já trata isso).

## Passo 2. Atualizar o painel (sem IA)

Dois cliques em `atualizar-painel.bat`, ou `python gerar_painel.py` na pasta. Se o Python sumir da
máquina (já aconteceu), reinstalar com `winget install Python.Python.3.12 --scope user` (o .bat
mostra esse comando quando não acha o Python); o .bat instala pandas, openpyxl e plotly sozinho.
O .bat faz a análise inteira sem IA: a página inicial, as seções e a página de cada projeto saem do
`gerar_painel.py`, e a janela mostra os números de cabeça da página inicial pra conferir de relance.
Mexeu no `.bat`: manter as linhas com quebra CRLF e testar com dois cliques (ou `cmd /c` com o
caminho inteiro) antes de entregar. Rodado sem console (`cmd /c` de dentro de outro programa), o
`timeout` do fim avisa "não há suporte para o redirecionamento de entrada": é só o teste, nos dois
cliques ele espera os 20 segundos.

## Reports das analistas (quando houver `Report Projetos *.xlsx` na pasta)

Os reports não têm padrão fixo (pedido do Julio em 02/10/2026: não entram no .bat). Quando chegar
um report novo ou atualizado:

1. Abrir cada arquivo e conferir o formato: uma linha por projeto com o código do CES em COD; no
   fim vêm linhas de "Total" e "Filtros aplicados" (descartar tudo que não tem COD numérico).
2. Conferir se `importar_reports.py` reconhece as colunas: anotação (título começando com
   "Andamento"), HandOff (coluna "HandOff"; no report do AgriManager de 02/10/2026 veio sem título,
   reconhecida pelo conteúdo), "Analista de sucesso", STATUS e os números HR ADQ, PLANEJADO,
   REALIZADO, ESTOQUE DE HR, FINANCEIRO, FATURADO. Coluna nova ou com outro nome: ajustar o script.
3. Rodar `python importar_reports.py`. A data da anotação é a data em que o arquivo foi salvo; o
   histórico acumula (report novo vira mais uma anotação no projeto; reimportar o mesmo arquivo no
   mesmo dia substitui só as linhas dele).
4. Regerar o painel e analisar no notebook (perguntas já feitas, acima da conclusão): cobertura
   report × painel, status do report × CES × saúde, horas do report × CES, hora entregue sem
   faturar. Responder ao Julio com as divergências.

O que já se sabe dos reports (02/10/2026): 97 projetos, cobrem os 72 em andamento do painel (os
suspensos ficaram fora do filtro). Cancelado e concluído batem com o CES; "Encerramento" é um estado
que só existe no report (30 projetos ainda em andamento no CES, 25 deles marcados Encerrar pelo
painel). HR ADQ do report é o previsto vendido (sem bonificação e transferência), por isso o
estoque do report pode ficar abaixo do saldo do painel; o realizado difere quando há OS sem fechar
(o report conta) ou agenda depois do report. FINANCEIRO = faturado menos realizado (negativo é hora
entregue sem faturar: 12 projetos e 367h em 02/10/2026). Para hora e saldo vale o CES; o report
vale pela anotação e pelo financeiro.

## Passo 3. Analisar (com IA, quando o Julio pedir leitura ou algo novo)

1. Conferir a leitura uma vez: tamanho de cada aba, tipos e amostra (`modelo.ler_planilha`).
2. Reexecutar o notebook e ler os números novos. As reflexões têm números escritos no texto; o que
   mudou precisa ser reescrito, não só reexecutado.
3. Pergunta nova: célula markdown com a pergunta, código curto, executar, conferir (n visível,
   share × taxa, outra explicação), reflexão; sempre acima da conclusão, e atualizar a conclusão.
4. Mudança de regra ou de tela: mexer em `modelo.py` (regras) ou `painel_template.html` (tela),
   regenerar e conferir no navegador antes de entregar, inclusive tema escuro, menu recolhido e
   largura de celular (menu em gaveta). Seção nova entra no menu lateral (`#sideNav`) e no `SECOES`
   do JavaScript, com o mesmo `data-tab` do `id="tab-..."`.
5. Responder ao Julio com o que mudou na fila de ataque (críticos, sem agenda, a encerrar) e com
   as tags [Certo] / [Provável] / [Suposição].

## Armadilhas conhecidas

- A aba Projetos traz uns 320 projetos repetidos (muda só grupo econômico e manutenção); o modelo
  fica com uma linha por projeto, senão as horas contam em dobro.
- `OS EXECUTADA1` é cópia da `OS_EXECUTADA` sem a coluna de status: não usar.
- O CES às vezes parte o mesmo dia de uma OS planejada em duas linhas (ex.: 14h às 17h e 17h às
  18h); o modelo soma as horas e junta os horários desse dia.
- Uma linha de OS executada é um dia de agenda; OS planejada sem execução tem a data na OS
  PLANEJADA (ou a data de início da OS).
- No terminal do Windows os acentos aparecem quebrados; os dados estão certos. Rodar Python com
  `PYTHONIOENCODING=utf-8`.
- A exportação do CES não traz a agenda inteira de todos os consultores (em 01/10/2026 o Fábio, com
  agenda cheia até dezembro, aparecia com só 20h marcadas): na agenda dos consultores, "livre" quer
  dizer "sem OS nesta planilha".
- O cadastro de analista e de consultor responsável no CES estava desatualizado em 01/10/2026
  (54 de 83 projetos no nome de quem não está mais no time de projetos): ler "analista" como o que
  está no cadastro, não como quem cuida de fato.
- Para testar o painel em navegador sem tela, o Edge não desce de uns 500px de largura; testar o
  celular dentro de um iframe de 390px. Para testar filtro e clique, copiar o painel com um
  `<script>` no fim que clica nos botões e escreve o resultado num `<pre>`, abrir com o Chrome
  `--headless=new --dump-dom` e conferir os números contra os dados embutidos (`const D = ...`).
- O `.gitignore` do sistema bloqueava `.bat` até 02/10/2026: o `atualizar-painel.bat` existia só na
  máquina onde foi criado, e na `pc-aliare` o Python estava sem plotly (o .bat recriado instalou).
- O painel gerado vai pro GitHub e as duas máquinas geram: em 03/10/2026 o merge `1f52571` deixou
  marcas de conflito (`<<<<<<<`) dentro do `painel-projetos-hunter.html` e a página não carregava.
  Conflito no painel nunca se resolve na mão: regerar com o `.bat` (ou `gerar_painel.py`) e subir o
  arquivo gerado. Conflito no `painel_template.html`, no `modelo.py` ou no `gerar_painel.py`, sim,
  se resolve na mão.
- O navegador embutido do Claude não abre o painel por `file://`; para olhar, servir a pasta com
  `py -3 -m http.server 8765 --directory "projetos/Painel Projeto"`. Com a janela minimizada a página
  não desenha quadro (`requestAnimationFrame` não roda): os gráficos da página do projeto ficam vazios
  no teste, não no uso.
