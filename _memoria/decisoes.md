<!-- quem alimenta: o /atualizar acrescenta no fim; robô nunca escreve aqui (propõe por recado). Lido quando perguntam "por quê" ou antes de mudar algo já decidido. -->
# Decisões

Uma entrada por decisão, sempre acrescentada no fim, nunca reescrita. É o arquivo mais barato do
sistema e o que mais evita retrabalho: daqui a três meses, quando alguém (inclusive você) perguntar
"por que a gente faz assim?", a resposta está aqui.

O que entra: escolheu um caminho e descartou outro, mudou de ideia, fechou um preço, definiu uma
regra de trabalho. O que não entra: tarefa feita (isso é o diário).

**Formato de cada entrada:**

```
- **AAAA-MM-DD** (quem decidiu: o nome da pessoa, ou a origem se foi um robô) [projeto, se for de projeto]: a decisão em uma frase. Por quê: o motivo em outra. Substitui: AAAA-MM-DD (só quando muda uma decisão anterior; a antiga fica onde está)
```

---

<!-- as decisões entram abaixo, a mais nova por último -->

- **2026-09-16** (Julio): remover a menção a "RatosOS" do título do `AGENTS.md`, deixando só
  "Operações - Produtor Rural". Por quê: é o nome do kit por trás do sistema, não do negócio; o
  título deve refletir a operação da Aliare, não a marca da ferramenta.
- **2026-09-16** (Julio) [rito de projetos]: centralizar email, reunião e WhatsApp de projeto
  dentro do HubSpot; bloqueio de agenda de consultor passa a exigir autorização prévia do Julio;
  ferramenta única de controle de projetos (ClickUp ou Evolution API) passa a ser obrigatória,
  não mais opcional; meta de 12 encerramentos de projetos myFarm anteriores a maio até 30/09/2026
  (6 com a Jaqueline, 6 com a Joyce). Por quê: falta de histórico único de comunicação com o
  cliente, falta de visibilidade sobre ausência de consultor, e acúmulo de projetos antigos sem
  encerramento formal represando saldo financeiro e consultores ociosos.
- **2026-09-16** (Leandro Xavier e Julio) [churn]: cliente que ficou com uma ou duas licenças por
  módulo conta como churn, mesmo registrado como downsell na base; o downsell de verdade vai em
  aba separada, só o confirmado (Procede = Sim). Por quê: redução a uma licença é saída na
  prática; separar o downsell real, que é problema de gestão de valor em conta viva.
- **2026-09-16** (Julio) [churn]: downsell sem motivo registrado é apresentado como "Redução de
  custos". Por quê: não informado; as três reduções vieram por chamado sem justificativa.
- **2026-09-17** (Julio) [churn]: análise de churn pra diretoria sai sem comparativo com
  referência de mercado. Por quê: não informado.
- **2026-09-17** (Leandro Xavier e Julio) [onboarding myFarm]: adotar a Evoluto como plataforma
  guiada de implantação e de projetos do myFarm. Por quê: cliente myFarm abandona o sistema logo
  após começar e a base perde cliente pra concorrência; a Evoluto conduz o cliente passo a passo
  (documentos, formulários, vídeos) desde o email de boas-vindas.
- **2026-09-17** (Julio) [onboarding myFarm]: Guilherme Job passa a ser o dono da gravação da trilha
  de vídeos do myFarm, no lugar do Luiz Carlos; Lucas Nogueira é o dono da importação de XML e das
  planilhas. Por quê: o Luiz foi desligado em 17/09 por corte de custos; o projeto
  precisa de um responsável por frente e de prazo real (vídeos até 15/10, XML até 22/09).
- **2026-09-17** (Julio, com observação do Guilherme) [onboarding myFarm]: cadastros de
  fornecedores, clientes e produtos extraídos do XML podem ser importados direto no myFarm;
  tributação vai pra planilha no layout de importação e só entra depois que o cliente ou a
  contabilidade valida. Por quê: a legislação mudou no período e muito cliente tributava errado no
  sistema anterior; importar às cegas coloca a percepção de qualidade em risco, e a planilha facilita
  o retorno da contabilidade.
- **2026-09-17** (Carlos, CEO, repassado por Leandro Xavier) [retenção]: Leandro e Julio têm
  autonomia pra decidir como tratar cada cliente em suspensão/negociação, sem precisar de aval de
  cobrança/financeiro; empecilho de terceiro na operação escala direto pro Leandro. Por quê: o CEO
  reconheceu, ao ouvir as dificuldades da operação, que as regras de cobrança vinham sendo aplicadas
  sem entender o contexto de cada cliente. Em troca, quer reporte semanal de posição de suspensos.
- **2026-09-18** (Julio): reunião que não aconteceu não se apaga da agenda do consultor; fica só
  sem confirmação e sem liberação pro consultor. Por quê: o sistema é da empresa, vale manter o
  histórico completo, inclusive do que não se realizou.
- **2026-09-18** (Julio) [equipe]: com o consultor Guilherme (perfil atípico, tende a esticar
  ligação por qualquer assunto), a orientação pra Jaqueline e Joyce é ter pulso firme e direcionar
  pra texto ou áudio quando não for urgência real (cliente parando, por exemplo). Por quê: ligação
  longa e recorrente consome o tempo do time sem necessidade; sem postura firme, vira prática
  recorrente com outros consultores também.
- **2026-09-22** (Julio) [email]: a subpasta "Email Pendentes" da Inbox recebe, pelas rotinas das
  9:30 e 16:30, pendência pessoal do Julio sem resposta dele e cobrança do time travada com outra
  área; em dúvida a rotina não move e pergunta. Email com alguém do time no fio, sendo dono natural
  do assunto, não é pendência dele; só vira se o time ficar 3 dias úteis sem responder (regra de
  23/09). O que se resolve fora do email sai da pasta pela mão do Julio. Por quê: ver num lugar só o
  que depende dele e o que o time espera de outras áreas, sem ser acionado pelo que o time já toca.
- **2026-09-23** (Julio) [sistema]: briefing executivo de segunda a sexta às 9:30, na nuvem (email,
  Teams, Granola e agenda); a rotina só prepara (arquivos dela e aviso) e o que vira pendência,
  decisão ou aprendizado entra com o Julio, pelo `/atualizar`. O aprendizado sobre ele e o time fica
  em `_contexto/jeito-do-julio.md` e `equipe/radar.md`. Por quê: rodar com o computador desligado,
  sem gravar memória durável sem ninguém revisar.
- **2026-09-23** (Julio) [sistema]: resumo diário do Teams na nuvem às 16:30 (seg a sex), de 16:31
  do dia útil anterior até 16:30, gravado em `resumo-teams/AAAA-MM-DD.md` pelo GitHub. Por quê:
  guardar todo dia sem depender do computador ligado; o Agendador do Windows foi descartado porque a
  trava de segurança não deixa registrar tarefa que roda o Claude sem supervisão.
- **2026-09-23** (Julio e Cecílio Manfroi) [implantação AGM]: estimativa padrão de horas:
  levantamento de requisitos 8h (com formulário prévio do cliente); parametrização 16h até 3
  empresas com o mesmo plano de contas (+8h por empresa extra, +8h se o plano for diferente);
  treinamento 40h (administrativo-financeiro 16h, armazenagem 8h, produção 8h, controladoria 8h);
  SPEDs, plano orçamentário, balança, integração bancária e afins à parte (valores a confirmar com o
  Leandro); gerenciamento de projeto bonificado. Por quê: reduzir horas em vez de baixar o valor da
  hora, pra não perder competitividade nem preço.
- **2026-09-23** (Julio e Amanda Scheffer) [retenção]: churn contado por grupo econômico; downsell
  que na prática é churn vira "churn operacional"; registra-se o valor cheio, não o já reduzido por
  downsell anterior. Por quê: a contabilidade olha contrato e os números não batiam; a controladoria
  só reconhece churn em cancelamento formal; e não mascarar o número, mesmo sendo pior pra área.
- **2026-09-23** (Julio, Leandro Xavier e Ângelo Fontella) [myFarm]: oferta "só emissão de nota
  fiscal" no myFarm a R$290 por mês, com emissão fora do horário comercial (inclusive fim de semana)
  mediante aviso até sexta ao meio-dia e sobreaviso pago à equipe (valor do sobreaviso confirmado
  pelo Julio em 23/09). Por quê: três clientes emitem nota só pela Maxcom e não querem o sistema de
  gestão completo.
- **2026-09-23** (Julio, Amanda Santos e Ramona Brito) [CS]: WhatsApp do atendimento num número por
  área, começando por Projetos e depois Consultoria, sincronizado com o HubSpot; o upgrade pago do
  Supabase (R$150 por mês) fica pra decisão no mês seguinte. Por quê: cortar custo de linha (cerca
  de R$60 por linha por mês) sem perder o histórico.
- **2026-09-25** (Julio) [retenção]: o MRR recuperado conta o contrato anual dividido por 12. Por quê:
  a planilha da central de cobrança soma o valor anual cheio como MRR e infla o número (setembro:
  R$ 34.052,84 na planilha contra R$ 25.101,44 com o anual dividido).
- **2026-09-25** (Julio) [retenção]: no status report da cobrança, cada cliente aparece em uma única
  aba; quem pagou o faturado e cancelou (Tellus, Theodoro) fica em Recuperação; o recuperado que não
  estava nas planilhas de cobrança entra como "extra", destacado em outra cor. Por quê: não contar o
  mesmo cliente duas vezes na apresentação à diretoria e separar o que a central trouxe além da lista.