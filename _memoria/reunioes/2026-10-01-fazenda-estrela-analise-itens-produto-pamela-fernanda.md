# Fazenda Estrela: análise item a item das demandas com produto (Pâmela e Fernanda)
- data: 01/10/2026 11:22 (Brasília)
- participantes: Julio, Fernanda Lima e Pâmela (produto myFarm), Lucas Nogueira, Ana Rocha e Jaqueline Martins (segundo o resumo do Granola); falas via Microphone/System audio
- fonte: Granola — transcrição literal (id fcab455a-c2a6-454d-95dd-a32341640ba6)

---

System audio: Okay.

Microphone: Gia, tudo bem?

System audio: Mm-hmm.

System audio (Fernanda Lima): Pode puxar no item 2 aí, Karen,

System audio (Fernanda Lima): enquanto eu anoto 1 aqui.

System audio (Fernanda Lima): Informa que o sistema não possui bloqueios ou alertados para impedir a duplicidade de lances fiscais e financeiros.

System audio (Fernanda Lima): No recebimento,

System audio (Kerolin Silva): o sistema impede nota idêntica.

System audio (Kerolin Silva): No financeiro.

System audio (Kerolin Silva): Exibe alerta de duplicidade, mas permite que o usuário prossiga.

System audio (Kerolin Silva): Na rotina baixar notas, criar recebimento, toque para nota já lançada. No financeiro, caso o documento possua parcela total, exibir alerta explícito detalhando o registro e a conta utilizada para evitar exclusões acidentais.

System audio (Kerolin Silva): Certo.

System audio (Kerolin Silva): Então, basicamente, dentro do documento, quando for lançar um novo documento que já tenha um lançamento idêntico, é para bloquear e não deixar seguir, seria isso?

System audio (Lucas Nogueira): Isso.

System audio (Lucas Nogueira): E nesse, nessa regra de negócios dela, precisaria desse bloqueio.

System audio (Lucas Nogueira): E na questão do

Microphone: E pelo que eu— perdão, Lucas— pelo que eu entendi também, o Keroli e Fernanda, e eu não sei, tá, Lucas, me corrija se eu tiver Parece que existe esse bloqueio, mas se eu não tiver enganado, esse bloqueio ele só aparece no final do lançamento do documento. E a principal dor da cliente É o tempo que ela gasta para fazer o lançamento dentro do sistema, aonde essa validação ela só acontece no final. Aí ela até trouxe como exemplo durante a reunião: ah, eu tô com item de venda, Tô com a nota de 20 itens, lancei os 20 itens. Quando eu mando gravar nota é que me aparece esta questão, tá? Aí eu até peguei e mencionei isso Então aí eu até comecei a falar com o Leandro, ele falou, ah, mas não sei se esse seria o caminho mais adequado e eu nunca vi nenhum outro sistema fazendo isso, porque existe sim uma requisição do banco. Então aí eu até comecei a falar com o Leandro, ele falou, ah, mas não sei se esse seria o caminho mais adequado e eu nunca vi nenhum outro sistema fazendo isso, porque existe sim uma requisição do banco. Então aí eu até comecei a falar com o Leandro, ele falou, ah, mas não sei se esse seria o caminho mais adequado e eu nunca vi nenhum outro sistema fazendo isso, porque existe sim uma requisição do banco. Então aí eu até comecei a falar com o Leandro, ele falou, ah, mas não sei se esse seria o caminho mais adequado e eu nunca vi nenhum outro sistema fazendo isso, porque existe sim uma requisição do banco. Então aí eu até comecei a falar

System audio (Lucas Nogueira): Não.

System audio: Isso.

Microphone: Será que não daria para a gente talvez colocar alguma validação na hora que ela colocar o fornecedor, o número da nota, e já fazer essa validação? Não sei dizer, tá?

System audio: Você fala assim que ela preencher esses dados já aparecer a duplicidade.

Microphone: Isso, já apareceu um alerta para que ela não precise nem continuar o lançamento da nota.

System audio (Fernanda Lima): Já sinaliza ali que é canal Jay-Z, né? Para mim,

System audio (Fernanda Lima): Jay-Z.

Microphone: Isso.

Microphone: É isso, né, Lucas? Me corrija se eu tiver falando besteira.

System audio (Fernanda Lima): Não, é isso mesmo, né? Quando já tem essa nota lançada, não tem nem a opção, né, quando selecionar

System audio (Lucas Nogueira): a nota lá pertinente, de receber no estoque ou no financeiro.

System audio (Lucas Nogueira): Já existe um bloqueio ali no início.

System audio (Lucas Nogueira): Certo.

System audio (Lucas Nogueira): Mas assim, só uma dúvida leiga mesmo: e se ela for

System audio (Kerolin Silva): fazer um lançamento para

System audio (Kerolin Silva): esse fornecedor, para esse cliente ali que seja, só que de outros itens, a gente bloquearia já aqui nos dados? do documento mesmo, mesmo que for outros itens, itens diferentes.

Microphone: Mesmo que seja outros itens.

System audio (Kerolin Silva): Eu ia pontuar, porque ela pode, é porque ela pode não lançar tudo, né? Que ela pode lançar um item ou

System audio (Fernanda Lima): outro só.

Microphone: Mas aí no lançamento seria uma edição, não é um lançamento novo. Se ela lançou metade da nota, deu 18 horas, tô indo embora, salvei da forma que estava para continuar amanhã, tem que ser uma edição.

Microphone: André, eu te puxei aí, tá? Só para você ficar a par do que nós estamos fazendo aqui de movimentação da Fazenda Estrela. Mas se você precisar sair por alguns outros motivos, fica à vontade, tá?

System audio: Não, obrigado por ter me convocado. Vou ficar aqui.

System audio: Tudo bem.

System audio (Andre Cunha): A agenda tá sendo gravada, eu vou dar o contexto

System audio (Andre Cunha): para a Pâmela também que eu puxei aqui, para os

System audio (Fernanda Lima): demais, né? Nós estamos com uma lista de solicitações de um cliente que tá com risco de churn e aí tá bem Tá bom, obrigado por ter me convocado. Quem fez o mapeamento para tentar entender melhor qual que é a dor da cliente, né? E aí estamos batendo ponto a ponto dessa lista junto com Frontend Only Farm para ver se a gente tem isso no sistema, se tem, se atende, se não, o que nós precisaríamos fazer ou melhorar no sistema para uma avaliação futura de viabilidade.

System audio (Fernanda Lima): Não sei se todos têm acesso, então compartilhando novamente aqui qual documento que a gente está se debruçando, que é essa ata aí. Nós já estamos no item 2, tá? Pode seguir aí, quero.

System audio (Fernanda Lima): Tá, beleza. Sobre essa questão, eu acho que ela tem que ser assim, aí se você tiver outra opinião sobre,

System audio (Kerolin Silva): parametrizável.

System audio (Kerolin Silva): Não acho que tenha que bloquear de todos os clientes especificamente. Acho que teria que ser um parâmetro ali, se os dados do documento forem idênticos a um documento já existente, Já tem um alerta ali no início. Aí só uma dúvida, Júlio. Esse seria um bloqueio mesmo total, assim, nem deixaria seguir?

Microphone: Na minha visão, se for parâmetro, sim, bloqueio total. Júlio, não é um parâmetro, é um alerta, e tem que ser um alerta que vai deixar o cara definir se ele quer continuar. Tá, apesar que existe aí, eu vou entrar no mérito, que não é o caso, tá, mas apesar que existe ali um indício que às vezes o dedo nervoso do usuário clica em sim para tudo e vai embora. Fora de olhos fechados, tá? Novamente, na minha visão, se for, eu sei, mas um parâmetro talvez seja muito trabalhoso e demorado, e a cliente quer uma ação instantânea, imediata, tá?

System audio (Kerolin Silva): Uhum.

System audio (Pamela Hort): Ô Júlio, o que que você acharia se a gente colocasse uma mensagem mesmo, tipo, olha, os dados desse documento aqui são similares aos dados do documento tals, tem certeza que você

System audio (Pamela Hort): deseja criar? E a gente pode colocar, tem alguns produtos que eles colocam tipo um countdown, sabe, uma contagem, aquela mensagem tem que ser devida pelo menos 10 segundos para a gente deixar o cara seguir se os dados forem iguais. Ele pode falar que sim ou que não. do número diferente, não sei o quê diferente. O que que você acharia dessa solução aí?

Microphone: Sim.

Microphone: Sim, concordo contigo. E aí eu vou abrir um outro parênteses. Talvez essa validação faz muito sentido, tá, Pamela? Só que talvez ela tenha que ser por acaso, porventura, tá, por tipo de documento.

System audio: Aqui você diz, né?

Microphone: É isso.

Microphone: Então, a validação, concordo com você, resolve, na minha visão.

System audio: Uhum.

Microphone: Só que a gente precisa confrontar tipo de documento, número e fornecedor.

System audio (Kerolin Silva): Uma

System audio (Kerolin Silva): compilação em duas partes também.

System audio (Ana Rocha): Deseja mesmo continuar? Depois que ela clicar em salvar, deseja mesmo continuar? Porque aí tem a duplicidade, porque aí

System audio (Ana Rocha): ela pode criar duplicidade, mas aí é a conta e risco dela, né, por escolha dela.

System audio (Ana Rocha): Só para eu entender, porque eu cheguei aqui no meio da agenda, quando vocês falam de criar documentos em duplicidade, né, quais informações desse documento aí a gente vai considerar nessa regra? Vai ser só

System audio (Ana Rocha): tipo de documento, número de

System audio (Pamela Hort): documento, fornecedor, como você falou, ou tem outros itens que também precisam ser levados em consideração?

Microphone: Fica à vontade.

Microphone: Na minha visão, não existe nenhum outro item a ser levado em consideração a não ser tipo de documento, pessoa e número de documento.

System audio (Pamela Hort): Tá.

Microphone: Porque assim, ó, pode acontecer da cliente ter um recibo, tá? Recibo. Então assim, o número da nota é 3030, aí de repente ela recebe um recibo desse mesmo fornecedor errado. 30/30, tá? É um recibo, não é uma nota, documentos diferentes.

System audio: Eu tenho, eu tenho.

System audio: Tá perfeito, mas a gente, se esse documento tiver material, por exemplo, alguma coisa assim, a gente não vai validar, só vai validar esses 3 campos aí.

Microphone: Não.

Microphone: Exato. Até mesmo porque, Pamela, com a regra de negócio que existe hoje no mercado, às vezes o cara ele pode, a pessoa que vai vender para aquela pessoa especificamente, pode ser que ele emite 50% com nota, 50% sem nota. Existe isso no mercado. Então assim, 50% vem com nota fiscal, modelo 55, chave, tudo mais, e 50% os mesmos itens sem nota fiscal, apenas um recibo.

System audio (Pamela Hort): Uhum.

System audio (Lucas Nogueira): Sim.

System audio (Fernanda Lima): É, eu tô mais pedindo porque assim, aquele óbvio que vale a pena você precisar para garantir que a gente não vai fazer uma coisa que é diferente do que vocês pensaram ali, alinharam e entenderam a expectativa da cliente.

Microphone: É isso aí, mas tá corretíssima. Fica à vontade, Fernando.

System audio (Fernanda Lima): Eu acho que tem que, talvez a gente valide também o que que é feito, né? Porque em caso de duplicidade de documento, a gente não lance a nota, talvez só referencie, sabe? E aí, ao invés de lançar o documento com base na nota, dá o alerta: esse documento já foi lançado com a nota tal, deseja referenciar a mesma nota? E aí não cria um documento com a nota anexada, entendeu? Deu para entender?

Microphone: A mim não.

System audio (Fernanda Lima): Não, então, por exemplo, hoje se eu lanço um documento vinculado à nota com todos os itens já lançados, tô partindo do melhor cenário, tá? Lancei um para um, e aí o cliente vai, vai lançar de novo essa nota.

Microphone: Mm-hmm.

System audio (Fernanda Lima): O sistema sinaliza que ele tá lançando, que aquele documento já foi lançado. Ah, não, mas eu quero lançar esse documento com essa nota mesmo, porque eu preciso dos itens ali, né, que é o caso que a Pamela trouxe, que é o caso que a gente vê às vezes. O cliente quer duplicar aquele documento. Ao invés da gente permitir que ele lance novamente porque tá errado, não pode ter dois documentos Então seria um documento vinculado à nota fiscal com a mesma nota de forma idêntica. Essa nota não fica vinculada, ela fica relacionada. Então seria um documento que não tem nota fiscal anexado a ele, porque O que tem nota fiscal é um documento só, para fins financeiros tem que ser um documento só, para fins de baixar notas é um documento só, mas esse outro documento ele fica a título de Então ele vai ter uma nota relacionada, que aí ficaria certo com a legislação, com os parâmetros do que que é a nota um para um.

System audio (Fernanda Lima): com contábil, com fiscal.

Microphone: Eu acho que isso faz muito sentido, Fernanda, se fosse uma CTE ou uma MDFE, mas para casos de nota recibo, na minha visão, não. Inclusive tem um outro email de um outro cliente da Coap que você já até comentou comigo, que solicitou exatamente isso que você trouxe aqui agora, tá?

System audio (Fernanda Lima): Entendi.

System audio (Lucas Nogueira): Uhum.

Microphone: Mas é isso.

System audio: Tá.

Microphone: Ah.

System audio (Fernanda Lima): Então, com base nisso, a gente segue

System audio (Fernanda Lima): aí com a sugestão que você validou junto com a APA, né?

Microphone: Na minha visão, sim. Lucas, fica à vontade para contribuir, tá? Se você tiver alguma consideração diferente disso, traga para mesa, tá?

System audio (Fernanda Lima): Então, tranquilo, pode continuar.

System audio (Fernanda Lima): Acho que tá bem, tá bem nítido.

System audio (Lucas Nogueira): Então, item

System audio (Fernanda Lima): 3: controle de aplicação de itens em

System audio (Lucas Nogueira): máquinas.

System audio (Lucas Nogueira): Itens permanecem disponíveis para aplicação em máquinas mesmo após já terem sido totalmente utilizados.

System audio (Lucas Nogueira): Os itens

System audio (Fernanda Lima): que você fala são os itens de suprimento ali? Isso, basicamente os materiais, quando é utilizados, eles permanecem com estoque zerado ou negativo. Resumindo, né, ela queria um bloqueio Referente a não poder utilizar

System audio (Lucas Nogueira): quando não estiver com estoque positivo.

System audio (Lucas Nogueira): Não sei se foi.

System audio (Lucas Nogueira): Tanto abastecimento quanto aplicação de materiais, né, tipo de manutenção.

System audio (Lucas Nogueira): Tipo de aplicação. Fiz uma manutenção aqui, coloquei os filtros,

System audio (Lucas Nogueira): acabou meu estoque de

System audio (Lucas Nogueira): filtro.

System audio (Lucas Nogueira): Isso aí existe um bloqueio após isso.

System audio (Lucas Nogueira): Eu, o Leonardo Oz também fez esse pedido, Pamela, que é tipo assim, ah,

System audio (Pamela Hort): ele aplicou defensivo na lavoura e ele não tem aquele defensivo em estoque.

System audio (Lucas Nogueira): E ele quer saber que aquele defensivo

System audio (Fernanda Lima): acabou, não sabe, com base na aplicação.

System audio (Fernanda Lima): Eu acho que tem alguma coisa, tá, sobre esse negócio de estoque negativo que o MyFarm permite hoje, né, porque nem todos os nossos clientes eles fazem um controle de estoque, né? Tem gente que faz esse controle.

System audio (Pamela Hort): E para máquinas é muito comum que o pessoal não tenha estoque de coisa de máquina realmente. Eles pedem conforme demanda, conforme manutenção. Então

Microphone: Eu vou

System audio (Pamela Hort): Mas eu acho que não é só em maquinário não, eu acho que a produção agrícola também, atividades agrícolas. Então atividades agrícolas eu acho que faz sentido, aí tem esse caso aí do estoque negativo que eu comentei. Aí a gente tem algumas alternativas. Eu sei que tinha alguém que queria falar, eu meio

System audio (Fernanda Lima): que interrompi, tá? Perdão. Mas a gente assim, a gente tem a opção de bloquear, mas isso não bloqueia só

System audio (Pamela Hort): para essa cliente. que é para todo mundo. Será que não faria sentido a gente ter alguma outra tratativa para esses casos de estoque negativo? Do tipo, olha, o seu estoque aqui, sei lá, a gente põe lá no dashboard de suprimentos, a gente fala, olha, estoque negativo desses itens aqui, por favor faça alguma correção. E aí faz uma entrada de estoque ou alguma coisa nesse sentido.

Microphone: É.

Microphone: Lucas, deixa eu te fazer uma provocação aqui. Lá, quando a gente acaba de lançar nota, existe alguma aplicação direta após o lançamento da nota do estoque?

System audio (Pamela Hort): Sim.

System audio (Pamela Hort): Perdão, não entendi.

Microphone: Acabei de lançar a nota fiscal, comprei pneu, comprei rolamento, comprei bomba de combustível, filtro e assim por diante. Acabei de lançar a nota, existe uma tela para fazer o lançamento desses produtos referente a essa nota?

System audio (Lucas Nogueira): Sim, aplicação

System audio (Lucas Nogueira): direto pelo estoque, sim.

Microphone: Tá, por quê? O que a cliente reportou, Pâmela, Caroline e Fernanda, foi que ela acabou de fazer uma aplicação, não sabia o nome, Lucas, aplicação direta. Ela volta Ela fez a aplicação na nota fiscal e ela ficou na dúvida, cara, eu apliquei ou não apliquei esses materiais? E ela consegue reaplicar os produtos na aplicação direta. Existe uma trava, ó, tais produtos já foram aplicados, não existe, tá? E ela trouxe esse cenário lá também. Em minha visão, isso é um bug. Não sei se é devido à questão da ausência de trava para não deixar consumir itens com estoque negativo, se devido a essa ausência ele deixa passar, tá?

System audio: Aplicação que você fala, e aí desculpa, é que dentro do MyFarm mesmo, tá? Que eu não tô entendendo todos os módulos, é na atividade agrícola mesmo ali, né? Seria isso?

Microphone: Eu acho que é lá dentro de suprimentos, na hora que você vai receber a nota, mas eu não tenho conhecimento e propriedade para afirmar, tá, Lucas? Você tiver e puder nos auxiliar referente a isso, beleza.

System audio (Fernanda Lima): É refazer o cenário aí dela, porque eu acho que fica mais fácil conduzir a Carol

System audio (Fernanda Lima): refazendo o cenário dela para a gente entender. É um dos pontos assim que ocorre, é, por exemplo, né, se ela faz essa

System audio (Lucas Nogueira): aplicação em maquinário direto pela, pelo recebimento

System audio (Fernanda Lima): de estoque. Se ela for no, na manutenção corretiva, por exemplo, né, dentro da, do módulo de maquinário, Ela consegue lançar

System audio (Lucas Nogueira): talvez ali o mesmo, a mesma peça, o mesmo item novamente sem o sistema exibir nenhum alerta. Ó, tal data, 2 dias atrás você já aplicou essa correia nesse maquinário.

System audio (Lucas Nogueira): Então não tendo essa recebimento, então aqui suprimentos, recebimento.

System audio (Lucas Nogueira): Seria isso.

System audio (Lucas Nogueira): Isso pela baixa de notas normalmente.

Microphone: Eu recebimento, baixo de nota.

System audio (Lucas Nogueira): Baixa de notas.

Microphone: Então é lá em cima, baixo de notas.

System audio (Kerolin Silva): Então, suprimentos, baixar notas.

System audio (Kerolin Silva): É que eu não tenho certificado, não vou conseguir.

System audio (Kerolin Silva): Mas

System audio (Lucas Nogueira): é que assim, o baixar notas, quando tu clica em receber no estoque,

System audio (Kerolin Silva): ele vai para essa tela de

System audio (Lucas Nogueira): recebimento, tá? É, ele vai para a tela de recebimento. Só que ele já vai preenchido ali com os dados que vem na nota. mesma, por caminha para o mesmo lugar. Então a cliente tá ali no baixar notas, tinha uma nota de um

System audio (Pamela Hort): fornecedor de peças, ela clicou na nota, comprou e recebeu no estoque, deu entrada no estoque dela daquelas, daqueles materiais, fez isso, beleza.

System audio (Pamela Hort): Aí ela foi lá agora em maquinários, que ela vai registrar uma manutenção na máquina dela.

System audio (Pamela Hort): Exato.

Microphone: Agora tem uma dúvida, Pamela. Tem uma Pamela que tem uma dúvida que eu vou te trazer, Pamela. Perdão, é, tem uma Pamela com dúvida.

System audio (Pamela Hort): Tá, e aí que acontece depois disso?

System audio (Pamela Hort): Vai para melhor que a Google. Tem alguns meses que eu não tenho

System audio (Lucas Nogueira): a cola.

Microphone: Me tira uma dúvida aqui. Se eu for no baixar notas e clicar novamente na mesma nota para fazer o recebimento, ele permite? É uma dúvida que

System audio (Fernanda Lima): Não

System audio (Fernanda Lima): permite.

System audio (Fernanda Lima): Não deveria permitir, tá? Uma nota que já está recebida tanto financeiro quanto no estoque não deveria

System audio (Fernanda Lima): permitir que você faça baixa novamente.

Microphone: Lucas.

System audio (Pamela Hort): Aí se tiver algum caso assim, vocês vão abrir um

System audio (Pamela Hort): bug para isso aí, tá? Mas eu até tava atendendo alguns casos ontem, eu não consegui repetir isso aí não, tá? A nota já é baixada.

Microphone: Lucas, tem que testar isso.

System audio (Pamela Hort): Entraria naquele, tá, vou fazer a validação, entraria naquele mesmo caso, né, ele não permitiria, porém ele vai deixar receber a nota, né, e aí só vai comunicar que A nota já foi implementada no sistema quando a cliente for finalizar, que é

System audio (Lucas Nogueira): aquela questão que a gente tava falando do recebimento.

Microphone: É amazing.

System audio (Lucas Nogueira): O baixar notas, ele não vai deixar. Pensa que tu tem uma nota ali no baixar notas, você clicou em receber no financeiro, tu recebeu aquela nota no financeiro, criou um documento, existe um documento vinculado. Se você for lá no baixar notas, ele não vai deixar. Se for o contrário, né, se

System audio (Pamela Hort): você também estiver recebendo, não contrário, né, mas o outro caso de estou recebendo essa nota no estoque, se você falando baixar notas já recebeu essa nota no estoque, terminou de criar, fazer todo o fluxo de recebimento, da entrada no estoque, e você Se você voltar lá no baixar notas, você não deve conseguir receber essa nota novamente. Mas aí, quando você fala em receber, Pamela, é quando você clica ali para receber a nota, ele já deveria queria bloquear, ou só ao final quando você tiver lançando todos os itens?

Microphone: Eita!

System audio (Pamela Hort): Ele é na, quando você clica na nota mesmo. Quero, vai no baixar notas, por favor, só para eu mostrar um jeito de jogar.

System audio (Lucas Nogueira): Pensa que nessa tela da Quero a gente tem várias notas aí, né? Vamos usar a imaginação aqui. E dentro da nota tem um checkbox. Quando tu clica no checkbox, essas

System audio (Pamela Hort): ações do lado elas vão habilitar ou desabilitar. Se uma nota já tiver sido recebida no estoque, a opção de receber no estoque vai estar desabilitada, ele não vai conseguir. Se for no financeiro, ela vai ficar exatamente dessa forma que tá aí, vai ficar desabilitado, o cara não vai conseguir receber novamente. Então é esse que é o comportamento que deve acontecer.

Microphone: Agora tem um ponto aqui, tá, Lucas? Aí de novo, tá, Lucas? Preciso que depois dessa reunião você valida esse ponto aí para gente, tá? E esse comportamento de fato está acontecendo ou se não está acontecendo, tá? Só que Aí tem um outro ponto aqui, tá, Lucas? Se a cliente falar: ah, eu recebi essa nota, fiz toda a parte, pelo que eu entendi, essa aplicação direta ele habilita aqui. Me corrijam se eu tiver errado, tá? Cara, acabei de fazer. Eu vou lá em aplicação em máquina e vou tentar aplicar os produtos daquela nota na máquina novamente. Sistema deixa eu passar, porque lá o sistema não valida Ele valida a aplicação pela nota, ele valida a aplicação pelo estoque. É como se ela tivesse fazendo uma nova manutenção da máquina, tá? Então o sistema não tem, Lucas, e ele não vai ter, não faz sentido Aí, Lucas, tem que testar isso.

Microphone: Pode ter enceragado novamente.

System audio (Pamela Hort): Pode acontecer, né? Problemas acontecem aí. Às vezes o cara fez a manutenção, mas deu algum problema. Então tudo que for trava assim, preenchimento de coisa, de duplicidade, a gente tem que ter muito cuidado porque Problemas acontecem, né? Situações às vezes realmente acontecem nesse sentido. Acho que os avisos eles fazem, fazem

System audio (Pamela Hort): parte, né? E aí por isso que a gente faz mais pergunta, porque assim, às vezes o problema dela é porque ela não, ela tá querendo ter uma gestão melhor de estoque. Aí, beleza, vamos explorar então o que que seria uma gestão melhor de estoque para ela, o que que ela gostaria de ver, como é que ela gostaria de gerenciar, porque Às vezes o que ela relatou ali na hora é a superfície do problema, mas quando a gente vai ver mais a fundo, a gente entende realmente a necessidade e consegue pensar numa solução mais assertiva, assim, do que só fazer exatamente o que ela tá pedindo.

System audio (Pamela Hort): Pessoal, desculpa aí.

System audio (Pamela Hort): Se eu estou sendo completamente leiga aqui sobre o assunto, um cliente, eu tava fazendo uma QBR ontem, um cliente tava trazendo inclusive um feedback a respeito Dessas entradas e saídas, e ele tava dando uma sugestão sobre a validade dos

System audio (Ana Rocha): produtos, né, e fazer também a correlação do que que tá Seja sendo aplicado ou não, inclusive ali nos baixar as notas a partir de QR code. Hoje existem outros outros sistemas que fazem essas leituras. Aí vamos imaginar aqui que a gente também tá falando de máquinas, né? Aí o próprio cliente, eu já vi cliente falando que geram os próprios QR codes para fazer aquelas Agricultura de Precisão, aqueles relatórios de agricultura de precisão. Será que uma solução parecida com isso poderia nos atender? Porque aí ele faria as validações dos suprimentos deles,

System audio (Ana Rocha): defensivas, as sementes, a partir desses QR codes, e poderia ser o mesmo, né, só que é diferente porque ele tem um código separado, assim como talvez em questão de máquina maquinário, né, no maquinário permitir isso, porque a gente sabe que a situação pode ser mais recorrente.

Microphone: A resposta é sim, tá? Mas eu acredito que esse aí vai ter que ficar para uma segunda leva de tratativa nossa, tá? Porque sim, faz sentido, mas aí a gente tá falando de É um projeto que, conhecendo o fluxo, vamos ser sensatos, tá? O que eu vou falar aqui é com sensatez, não acusações apontando dedo. Conhecendo o fluxo, a gente sabe que não vai ser uma coisa fácil, que vai sair assim. Tá, então olhando para a questão hoje da cliente, a gente precisa de algo assim, tá. Então sim, faz sentido, mas também a gente tem que levar isso como um banco de ideias para se tratar de um projeto futuro, tá.

Microphone: Vamos para o próximo item. Lucas, aí detalhe, tá? Fica aí como tarefinha testar e validar esse item. Talvez até pegando a própria base da cliente, tá? Vai lá, baixa uma nota lá. Você comentou sobre a aplicação, Tenta replicar, ver se as travas que a Pâmela comentou está sendo validadas, estão de fato funcionando, e aí traz um retorno aqui para a gente no chat, tá? Se de fato tiver, aí esse item 3 está riscado da lista, tá?

System audio: Sim.

System audio (Lucas Nogueira): Tá.

Microphone: Vamos para o próximo, quero, por favor.

System audio: Bora.

System audio: Informa que precisa consultar o pedido manualmente para verificar a condição de pagamento, reproduzir as informações de lançamento da nota fiscal.

System audio (Kerolin Silva): A integração ocorre via previsão na agenda financeira. A condição de pagamento do pedido não é

System audio (Kerolin Silva): importada automaticamente para nota fiscal no recebimento.

System audio (Kerolin Silva): Tratando-se de fluxo operacional, há necessidade, ao vincular a nota fiscal ao pedido de compra, o sistema deve puxar automaticamente a forma de pagamento registrada no pedido. E efetuar a quitação parcial ou integral de forma automatizada.

Microphone: Para mim ficou claro, não sei para ti, tá, Carol? Se não, eu tento exemplificar, ou senão também trago o Lucas aí para trazer melhor entendimento.

System audio (Kerolin Silva): Se puder exemplificar, por gentileza.

Microphone: Você quer segui-lo? Casou, eu sigo com meu entendimento e você valida.

System audio (Kerolin Silva): Pode ser, pode seguir.

Microphone: Tá, pelo que eu me recordo que a cliente trouxe lá atrás, o seguinte: vamos supor que a gente foi lá, fez um pedido de compras, este pedido de compras foi acertado. O financiero da forma ABC, sei lá, em 3 parcelas, todo dia 10 do mês, e assim por diante. Quando chega o XML, ela quer que Cara, tô dando entrada, o fornecedor pode ter colocado lá nas tags de financiar dentro do XML qualquer paçoca, mas ela quer que segue o que tá dentro do pedido de compra. Além disto também, se por acaso teve adiantamentos, que exista alguma validação desses adiantamentos ao fornecedor lá dentro na hora do lançamento do XML. É isso.

System audio: Pelo que eu tô entendendo, ela quer uma amarração bem completa do pedido, seria isso? Pedido com a nota.

Microphone: É isso, porque eu

System audio: Pedido com o que ela tá recebendo lá no pedido recebimentos.

Microphone: Pedido recebimentos, o que ela tá recebendo no financeiro, tá falando de valor monetário. Porque hoje, pelo que ela trouxe ali para gente durante a reunião, cara, às vezes o pedido de compras já foi faturado, já foi pago à vista. Inclusive, até onde eu me recordo, no MyFarm existe lá já pago, coisas do tipo, tá? Só que não existe nenhuma validação. Então, quando chega o XML para ela, o pedido tá uma coisa, o XML tá outra, ela tem que ficar ali validando, tá? Talvez aí, não sei a complexidade, mas talvez tem uma amarração, uma tela que mostrar o pedido tal, nota tal. Você quer respeitar o pedido ou nota fiscal? E talvez o cliente decidir ali o que que ele faz com aquilo, tá, com a vida dele.

System audio: Tá.

System audio (Pamela Hort): Sim.

Microphone: E eu sei que isso é complexo, tá? Eu tenho plena consciência disso.

System audio (Pamela Hort): Esse é daqueles que é banco de ideias, a gente tem que analisar para ver. Assim, eu acho que faz sentido, tá? É uma ideia legal, um pedido que faz sentido. Eu não sei se é possível ou não, dependendo do fluxo de trabalho, mas a gente tem que analisar como é que isso ficaria dentro do sistema, porque a gente tem— eu criei

System audio (Pamela Hort): um pedido lá que eu tô aguardando recebimento, aí eu vou lá para receber e aí lá anda esses e-mails Ele já vem informações que dizem respeito inclusive à forma de pagamento, talanã, enfim.

System audio (Pamela Hort): Teria que dar uma olhada com mais carinho, tá? Para vocês disserem para esse cara aí, não sei como é que tá a urgência da cliente nesse item. Isso é a mesma coisa do primeiro pedido, pelo que eu entendi, né? Lucas, que o primeiro pedido dela aí é vincular a emissão da nota ao contrato.

Microphone: Para ontem.

System audio (Pamela Hort): Isso aí é outra coisa. Não, gente, seria diferente, Fernanda. Eu falo que é a mesma coisa

System audio (Fernanda Lima): no sentido de o pedido ter todas as informações e ela bater a nota fiscal de entrada com o pedido. E aqui é, ela bater a nota de saída dela com as informações do contrato. Mas é o mesmo vínculo.

System audio (Fernanda Lima): É a mesma coisa, só mudando um pouco o assunto. Eu esqueci, tem um que eu acho que eu não acompanhei a discussão. Essa cliente usa emissão de nota de dentro do contrato ou não? Usa, mas tem alguns Aí depois a gente mapeou isso lá no comecinho da gravação, depois eu te passo esse ponto específico. Tem que levantar quais são os itens que tem. A gente hoje não aproveita 100%

System audio (Pamela Hort): das informações de contrato, E pelo que eu tô vendo por aqui, é a mesma coisa. Lá dentro da tela de contrato, a cliente consegue o tal do emitir nota em massa

System audio (Fernanda Lima): que a gente fez para Coop. Não sei se tu vai lembrar aí, Júlio, dessa novela que foi. Não sei se atenderiam o caso da cliente. Eu sei que lá a gente tem umas melhorias para fazer, né, tipo de permitir mais vínculos, enfim.

Microphone: É, e eu não sei, tá? Não sei. Eu acredito, você tem conhecimento, Lucas, dessa nova rotina de contrato que foi criado?

System audio (Pamela Hort): Não, essa que a Pamela mencionou referente a Coap, não. É aquela que dá para colocar uma quantidade de nota, sabe, que a gente tinha visto? Deixa eu mostrar para vocês.

System audio (Kerolin Silva): Enquanto a Keron mostra, ô Júlio, pelo que eu tô entendendo

System audio (Lucas Nogueira): aqui com essa agenda, tem muita coisa que hoje

System audio (Kerolin Silva): o MyFarm pede um lançamento duplo, uma validação que daria para amarrar.

System audio (Kerolin Silva): Mas que não foi pensado assim lá atrás e hoje

System audio (Kerolin Silva): alimenta muitas.

Microphone: É isso aí.

System audio (Fernanda Lima): Muitas telas, então tem que ser feito um lançamento. Acho que essas, para essas duas coisas, é abrir change e banco de ideias.

System audio (Fernanda Lima): Seria essa, esse campo aqui, Lucas. Ah, que a gente viu lá no início, né? Mostra aqui na criação do contrato também, quero, porque senão eu vou lhe dar para todos os contratos. Beleza, vamos lá. Só para mostrar os campinhos aí, mas não precisa criar o contrato não, tá? Acho que fica lá em agenda.

System audio (Kerolin Silva): Ah, então na finalidade, né, tu consegue colocar, permitir

System audio (Lucas Nogueira): emissão de nota direto do contrato. Essa parte de venda por

System audio (Pamela Hort): conteúdo a gente não tá usando ainda, tá? Então é uma evolução aí que vai acontecer, mas ele consegue selecionar E aí lá naquela outra telinha que a Carol tava mostrando ontem, ontem não, né, antes, é só preencher algumas outras informações que a gente não puxa, né, da operação, e emitir, emissão lá 3, 4 notas, 20 notas, que elas são iguais, né? Tem os mesmos valores, mas são notas diferentes.

System audio (Pamela Hort): Aí inclusive, só rapidinho, o Lucas trouxe a necessidade dessa observação, desse campo de observação, ele já ir direto para nota também, porque hoje ele não vai, né? Então a cliente ela emite nota aqui pelo contrato, hoje existe uma observação dentro da nota fiscal, mas ela não reflete.

System audio (Kerolin Silva): No Loomis.

Microphone: Agora o seguinte, aí eu não sei, tá, Lucas, é isso que a cliente quer? Porque até onde eu entendi, ela tava questionando que a limite se anota através do Home One e as informações de contrato não puxava.

System audio (Kerolin Silva): Ok.

System audio (Kerolin Silva): Não, ela tá

System audio (Pamela Hort): auxiliada nessa questão de emitir a nota direto pelo

System audio (Pamela Hort): contrato, mas ela tinha essa questão do

System audio (Lucas Nogueira): campo de observações e o quantitativo de peso nem quilos também

System audio (Pamela Hort): que tem dentro do contrato para puxar direto para nota.

System audio (Pamela Hort): Tem essas duas questões.

Microphone: Tá, mas a quantidade de quilos não se puxa através do contrato, porque o contrato vai ter lá 1 milhão de quilos. Ela não vai dar conta de entregar 1 milhão de quilos, a não ser que ela vai com aquele E havia um grandão lá que parece uma baleia, né? Então como é que tá essa questão lá especificamente?

System audio (Lucas Nogueira): Então, na rotina dela, ela diz realizar toda, né, todo o processo

System audio (Lucas Nogueira): de venda em uma única nota fiscal.

System audio: Então ali é a quantidade real que tá no contrato, é o que vai na emissão da nota fiscal que ela vai estar fazendo.

Microphone: Ela vai ser multada, você pode escrever.

System audio: Isso na rotina dela, né?

Microphone: Ela vai ser multada. Você pode escrever que eu tô te falando.

System audio (Lucas Nogueira): Tem que ser um para cada caminhão que sai.

System audio (Lucas Nogueira): É porque aí tem a ver com romaneio, né, igual o Júlio trouxe lá nesse petição. Mas assim, aí também dá de vincular com romaneio, tá? É que na verdade isso só tem uma das perninhas, não tem a outra perninha, né? Mas tipo assim, a gente pode até verificar, não lembro agora

System audio (Pamela Hort): bem certinho, mas eu sei que as notas que são emitidas por aí você consegue fazer o vínculo com o Romaneio também. No caso de quem emite nota antes de ter o romaneio, né? Pode ser uma nota de ajuste, pode ser uma nota de devolução, uma nota complementar. A gente pode mandar a documentação certinho para vocês também, para vocês darem uma olhada, ver se tem mais alguma dúvida, mais alguma coisa que vocês podem tirar para ajudar na rotina dessa cliente.

Microphone: Lucas, agora me responda. Não existe resposta certa ou errada, tá? Lembre-se disso. Você conhecia já essa tela?

System audio (Pamela Hort): Essa tela aqui já.

Microphone: Tá, tenta rever sobre ela, Lucas, e ver todos esses pontos que a cliente trouxe referente à parte de romaneio, se aqui atende, tá? Romaneio barra emissão de notas fiscais. Tento olhar se essa tela aqui também atende a necessidade dela, tá? Se não atender por algum motivo, aí a gente tem que trazer luz para isto, tá? Aí, recapitulando, Lucas, vai ficar 2 trabalhos para ser feito referente a recebimento, que a gente comentou ainda pouco. Se a cliente, aquele botãozinho lá do baixar notas, recebimento, alimento em estoque tá ficando bloqueado após a entrada. E também agora essa aqui, se por acaso vai resolver atender a cliente, tá?

System audio (Pamela Hort): Sabe.

System audio (Fernanda Lima): Tá.

Microphone: E aí, Lucas, regra de negócio, tá? Regra de negócio total aqui, que eu acho que a gente tem que historiar cliente com isso. Cliente, não é certo você emitir uma nota fiscal todo o seu contrato. Ah, não sei que ela faça um contrato por carga, por caminhão. O caminhão geralmente, Lucas, vai depender do tamanho, mas geralmente são 33 mil quilos que cabe em cima do caminhão, tá? 33 mil quilos líquido, tá? Aí tem que mensurar com ela, cara, você tá emitindo contrato de 33 mil quilos, a nota fiscal tá saindo como 33 mil quilos ou tá saindo 1 milhão de quilos? Ah, 1 milhão de quilos. Ó, vou te alertar, pode ser que você tenha multa. A gente já viu e eu já presenciei casos assim porque eu fiz Chega e fala assim: ah, então você tá mandando o caminhão sem nota fiscal? Como é que você tá emitindo só uma nota lá no final de 1 milhão de quilos e o caminhão tá indo sem nota? É isso que você tá me falando? E o cara tira a caneta do bolso e lá encontrou a multa para o cara pagar, tá? Então, falando de regra de negócio, não faz sentido. Mas aí a gente precisa puxar a língua da cliente, entender exatamente o que que ela tá fazendo.

Microphone: Tiver dúvidas, me pergunte, tá? Então tá, na ausência da fala tá ok.

System audio: Ok.

System audio: Responde, né, Júlio?

Microphone: Vamos para o próximo, Caroline, por favor.

System audio: Então esse 4 aí só para fechar, né? Vai entrar aí como nosso banco de ideias, a ideia faz sentido, mas a gente tem que analisar uma implementação mais complexa. Estamos entendidos, né?

Microphone: Família, eu não sei, vamos descobrir da cliente se estamos entendidos.

System audio (Lucas Nogueira): Aí, Júlio.

System audio (Lucas Nogueira): Não, aí mais explicar.

System audio (Lucas Nogueira): Se a gente aqui estamos entendidos que é uma coisa

System audio (Kerolin Silva): um pouco mais complexa e também a gente às vezes, né, ir um pouco

System audio (Pamela Hort): mais a fundo aí no processo da cliente, na dor da cliente, para a gente conseguir pensar em soluções que às vezes são simples, mas que já resolverem uma dor dela, tá?

Microphone: Sim.

Microphone: É, e aí eu não sei, André, mas você também fica à vontade para pontuar alguma coisa, tá? Você tá sentindo ali também um pouquinho da dor e da insatisfação do cliente, tá? Você também fica à vontade para opinar, tá?

System audio (Pamela Hort): Aí eu acho que é importante também, Júlio e André principalmente, né, e eu, a gente alinhar aqui, nivelar. Depois, Júlio, acho que é importante a gente

System audio (Pamela Hort): bater um papo com Leandro sobre isso, como a gente vai tratar e como nós vamos dar devolutivas aos clientes de todas essas

System audio (Fernanda Lima): demandas que vêm para o banco de ideias e que precisam de uma análise um pouco mais completa.

System audio (Fernanda Lima): Porque hoje qual que é a realidade do MyPharm? Eu tenho a Querum, que hoje 70% a 80% hoje do capacity dela tá nas demandas regulatórias, e eu tenho a Pâmela que É part-time, né? Não é só do MyPharm, hoje não atende só esses estudos e análise de produto. Então assim, você melhor do que ninguém sabe O volume de coisas que chegam para banco de ideias para serem estudadas, avaliadas e afins, nós precisamos definir. Eu não tenho ainda lugar de fala para te falar o preço, Pra gente entender melhor o prazo disso, como a gente vai dar uma devolutiva, mas para talvez já alinhar com o Leandro como a gente faz para dar essas devolutivas para o cliente. A gente arruma uma resposta padrão aí de pro comercial, né, para vocês e afins.

System audio (Fernanda Lima): Para que isso não fique agarrado, você fique, ah, qual o prazo disso, né? Deu para entender, Júlio? Ficou claro que eu trouxe? Concorda?

System audio (Fernanda Lima): Não? Então pode trazer seu ponto. Eu gosto do Júlio porque ele é muito sincero. Assim, tem lado bom, lado ruim, né? Mas no geral é bom. Não sei se tu sabe como é que isso funciona do lado do suporte, porque hoje em dia basicamente chegam também sugestões de banco de ideia pelo suporte, né? E aí eles preenchem um mini formuláriozinho assim

System audio (Pamela Hort): Na verdade, mais uma organização de informação. Esse ticket, ele fica marcado com o banco de ideias, mas ele é encerrado. Os clientes acho que nunca nem recebem devolutiva disso. Aí eu não sei se o CS também recebe essa informação, Não é só do MyPharm. Hoje não atende só esses estudos e análise de produto. Então assim, você melhor do que ninguém sabe o volume de coisas que chegam para banco de ideias para serem estudadas, avaliadas e afins. Nós precisamos definir. Eu não tenho ainda lugar de fala para te falar, mas para deixar registrado a informação, ou como é que vocês fazem essa gestão? Porque por mais que hoje em dia a gente não esteja resolvendo nada dessas coisas, essas coisas estão lá. Uma vez por ano, uma vez a cada 6 meses, a gente vai lá e passa uma limpa em algumas coisas. Talvez inicialmente, para a gente não perder essas ideias, a gente coloque esses tickets lá para a gente ter isso registrado em algum lugar. Depois a gente vê o que a gente faz com isso.

System audio (Pamela Hort): Não sei se faz sentido. Eu acho que não, porque eu acho que hoje a gente não atua em cima disso. Eles não têm devolutiva nem suporte nem CS, e o que é muito ruim, a gente tem Não é só do MyPharm. Hoje não atende só esses estudos e análise de produto. Então assim, você precisa também entender o nível de prioridade até para a gente visitar esse banco de ideias e falar, ó,

System audio (Fernanda Lima): isso aqui realmente, de fato, Faz sentido, ou isso é urgente, ou isso é um caso de churn, ou isso é um caso que impacta 100% a operação. Então acho que por isso que eu puxei, que não é provável, não, não querendo ser grosseira, mas se isso haja, peço desculpa, tá? Eu acho que desse fórum, acho que é problema meu e do Júlio e do Ângelo, porque a gente que tem ali que tratar comercialmente as dores do cliente e ver, achar uma forma de como a gente vai responder isso.

System audio (Fernanda Lima): Porque a parte aqui do análise e desenvolvimento é problema do Júlio, como ele vai tratar isso lá na frente com o cliente, é problema do Ângelo do que que ele tá vendendo, sonhos, e a gente tem que administrar. Isso que eu puxei ele, eu acho que a gente tem que bater esse papo com o Leandro assim para saber como que nós vamos tratar, né, essa frente.

System audio (Fernanda Lima): Uma sugestão.

System audio (Fernanda Lima): É...

System audio (Fernanda Lima): A gente ter um lugar como a gente tem uma pasta lá na Azul, por exemplo, que seja só de melhorias ou que a gente possa subir o God Lovable igual a gente fez com um produto. com produto para

System audio (Ana Rocha): poder fazer, mas para registrar.

System audio (Ana Rocha): Esses tickets é um trabalho a mais para CS, por exemplo, porque eu tô na área de CS, então meu lugar de fala vai ser para CS, tá? Mas assim, é um trabalho a mais da gente pegar E jogar lá e tals. É, mas é muito melhor do que estar separado, todos em vários tickets separados, que a gente também não consegue denominar. Se a gente fizesse uma extração de todos os Tickets, que se eles permanecessem abertos era mais fácil, mas se a gente pudesse fazer toda essa extração para poder segmentar eles, o que que é de fato melhoria e tudo mais. E aqui já é uma

System audio (Fernanda Lima): sugestão minha, tô dando pitaco.

System audio (Fernanda Lima): em área que eu não

System audio (Ana Rocha): entendo muito bem, mas se a gente pudesse colocar isso em paralelo com o nosso roadmap, porque vai ter coisas sendo desenvolvidas lá na frente Que vamos supor, vocês estão na área de baixar notas. Isso aqui que a gente está vendo é uma sugestão de melhoria de uma cliente ou três ou quatro clientes, enfim. E aí vocês vão atuar, ela anota já dentro do roadmap. Aí talvez seria uma boa alternativa já. Ah, eu vou mexer em um ponto aqui, eu já mexo nos outros. Que trane de melhorias, talvez seja uma forma de encaixar elas ali no desenvolvimento, porque assim por experiência própria eu vejo que melhorias ela fica perdida no espaço por anos e anos, e a gente não consegue até que o próprio cliente dá uma carteirada igual essa tá fazendo, entendeu? Você quer complementar aí com a sua discordância, Júlio?

Microphone: Não, eu acho que a Ana já pontuou, e é justamente isso também o que eu penso. A grande questão hoje da gente levar essas questões para banco de ideias é que elas não são pescadas. E se a gente olhar Hoje, para questões que nós temos do lado de cá, Fernanda, a gente vai perceber que tem muita coisa que é coerente o que o cliente pede, que realmente é uma muleta do sistema não ter a verdadeira informação. A verdade é essa. Então acaba que aí entra muito o que eu já comentei algumas vezes, que eu, na minha visão, mas isso não pertence ao Júlio, pertence a vocês em estratégia Já com o Leandro, que é reduzir talvez o roadmap que nós temos e começar a atacar, olhar para o cliente. Porque se a gente não olhar para o cliente, e aí ontem eu até brinquei, ontem não, perdão, Terça-feira o Leandro me falou uma coisa, eu falei, ah, mudou o vento, a gente vai. Mudou de novo, a gente vai. Mas não foi nada referente a produto, tá? Mas foi uma brincadeira de outro assunto. Então assim, literalmente isso, um gritou, a gente muda o vento. Outro falou não sei o quê, a gente muda o vento de novo. Então acho que a gente tem que ter essa visão voltada ao cliente. É muito bom tudo que a gente tem construído e visto aqui dentro do MyFarm, e até pega até uma fala do próprio Diego. A gente fez, por exemplo, não é do seu tempo ainda, agricultura digital. Mas a gente olha qual foi o impacto real da agricultura digital dentro do MyFarm, qual tempo a gente perdeu com isso, que poderia ser utilizado para as outras frentes. Então, de novo, na minha visão, precisamos enxugar roadmap dentro do MyFarm para começar a olhar para as demandas de cliente e começar a puxar o que o cliente de fato nos traz como melhoria, que realmente são relevantes para o produto.

System audio: Uhum.

System audio: Tá bom.

Microphone: Mas é isso, tá? Mas eu sei, de novo, tá, Fernanda, não é a questão, sei das suas limitações, como você me expontou, Júlio, que até quero ler. Eu tenho aqui um backup Pelo menos para mim, eu acho que é isso que a gente precisa fazer. Então, de novo, na minha visão, precisamos enxugar o roadmap dentro do MyFarm para começar a olhar para as demandas de cliente e começar a puxar o que o cliente de fato nos traz como melhoria, que realmente são relevantes para o produto. Eu acho que uma dessas tentativas, justamente essa agenda que a gente tá fazendo aqui agora.

System audio (Fernanda Lima): Exato, e escalar qual que, em qual nível de prioridade esses retornos

System audio (Fernanda Lima): vão passar para um cliente, porque é diferente, pelo que eu bati um

System audio (Fernanda Lima): papo com o Gustavo, né, é muito diferente do trabalho que É feito no IGM, que lá o cliente paga. Então lá o cliente ele tem lugar de fala, ele tem uma, ele tem um fórum que ele é ouvido e minimamente algumas demandas que são entregues para ele mesmo que ele Pagar ou não, no MyFarm não tem isso hoje, né, Júlio?

System audio (Fernanda Lima): Pelo menos se existe, não me passaram nesses 4 meses que eu tô aqui. Então tudo que a gente vai fazendo aqui, a gente tem que absorver ou num olhar geral, do cliente, ou eu recebo aqui na minha mesa, ó, faz isso, não faz isso. Hoje, para mim, os critérios do qual, com quem que eu vou priorizar o item A ou item B, não são Então acho que é puxar essa clareza para conseguir dar esse retorno para todo mundo.

Microphone: É isso.

Microphone: Uhum.

Microphone: Perfeito.

Microphone: Vamos lá.

Microphone: Eu acho que o item

System audio (Fernanda Lima): Esse quinto aí a gente pode pular, que a gente já analisou, já tá no documento. Pode para o item 6.

Microphone: Is.

System audio (Fernanda Lima): Dúvidas e falha operacional na integração técnica e comunicação com a balança no ambiente físico. É o MyPharmaIntegra.

System audio (Fernanda Lima): via COM ou IP na mesma rede. O cliente foi orientado

System audio (Fernanda Lima): a acionar o suporte, porém

System audio (Fernanda Lima): reportou que a tentativa não obteve êxito.

System audio (Fernanda Lima): atendente.

System audio (Fernanda Lima): Solicitado chamado junto à equipe de

System audio (Kerolin Silva): projetos suporte PDS para

System audio (Kerolin Silva): prestação de apoio técnico e direto e homologação da balança na Fazenda. Esse item a gente já tratou aqui, eu estava tratando aqui, né, com o Lucas ali.

System audio (Kerolin Silva): Esse item é por cliente. Todo cliente que tem que integrar balança, a gente tem que abrir uma testa ali para ele. Normalmente o pessoal do PDS ele consegue resolver, às vezes vem para o Lucas dar esse apoio, mas realmente teria que entender qual que é a balança, dados aí do cliente e tudo mais, para a gente ver se a gente tem alguma coisa para fazer ou se o pessoal consegue resolver. Lucas, você tem o número desse ticket? Que foi aberto com suporte

System audio (Pamela Hort): aí para a gente ver o andamento de como que tá. Esse da balança não, até então quando o cliente me passou, né, que tinha sido orientado, ele com suporte, o suporte orientou ele a entrar em contato com o suporte da balança.

Microphone: Ma.

Microphone: Não.

System audio (Pamela Hort): Né, apresentando aí algum problema

System audio (Fernanda Lima): na balança.

System audio (Fernanda Lima): Depois disso eu não tive mais retorno, aí foi feito esse pedido de suporte da equipe de BDS.

Microphone: Mas esse item eu tinha solicitado para que a outra analista de projetos que estava seguindo o projeto fizesse o levantamento, tá? Eu acredito que foi aberto um ticket, tá? Na paralela, Jaqueline, dá uma olhada para nós se consegue encontrar algum ticket aberto referente a esta questão no Move Desk do MyFarm, por gentileza.

System audio (Lucas Nogueira): O set também a gente pode passar porque a gente

System audio (Lucas Nogueira): já sabe. Enquanto ela, a Jaqueline, olha, tá? Só para ser mais assertivo aqui.

Microphone: Tá bom.

System audio (Lucas Nogueira): O item 8.

Microphone: Esse item 8, acho que a gente também já foi tratado, né, o Lucas?

System audio (Lucas Nogueira): Importação.

System audio: Eu acho que foi conversado ontem, né?

Microphone: Tá.

System audio: Isso já foi tratado.

Microphone: O 9 também, que é a busca automática de cadastro por CNPJ.

System audio (Fernanda Lima): Aí, Pamela, esse item 9 é um item que eu julgo que, pelo que eu conheço assim, né, de outros sistemas, não é nada

System audio (Fernanda Lima): muito complexo e também não é nada que mexeria em muitos módulos do

System audio (Fernanda Lima): MyFarm. Então acho que é legal a gente pôr no radar,

System audio (Lucas Nogueira): que é buscar os cadastros com base No CNPJ. Então, ao

System audio (Fernanda Lima): invés dele ter que, tipo o CEP lá, né, que ele vai estar o CNPJ, tu vai buscar, a gente vai buscar, aí busca todos os dados. Isso, exatamente. E não é nada assim, dá para encaixar numa sprint aí, outra para os meninos fazerem.

System audio (Fernanda Lima): Sim, eu posso criar depois que a gente terminar essa reunião. A gente cria aí as que tiver faltando, já deixa organizadinho. Ah, esse aí eu acho que eu até comecei a criar ontem, só falta talvez atualizar aqui, mas já tá, já escrevi ela.

Microphone: Acho que encerramos então. Então

System audio (Fernanda Lima): Encerramos. Ficamos só com o tique-tique aí da questão da balança, porque aí também se for o caso, eu bato papo com a Joyce para o time dela entrar em contato com o

System audio (Pamela Hort): cliente, assessorar na questão da balança.

Microphone: Vamos fazer um compilado.

Microphone: Compartilha a tela novamente, se tiver, por favor, quero limpar no finalzinho daquele quadrante ali só para a gente fazer um balanço geral. Então vamos lá, tá? O que que nós conversamos aqui? Então O item referente ao item 4, item 4, importação da condição de pagamento, pelo que eu entendi, vai ficar como roadmap, não, banco de ideias, mas se eu estiver errado, tá?

System audio (Fernanda Lima): O item 1 e o item 4, tá? Ambos.

Microphone: O item 1 e o item 4, sem

System audio (Fernanda Lima): Isso.

System audio (Fernanda Lima): Sendo que o item

System audio (Lucas Nogueira): 1, o Lucas vai repassar com a cliente porque tem alguma, ela provavelmente

System audio (Fernanda Lima): tá lançando coisas que vão ser surpreendas aí, mas a gente Não supre 100%, né, Lucas, pelo que a gente levantou. Então ele vai passar algumas funcionalidades que ela ainda não conhecia, mas a gente segue não cumprindo 100% do

System audio (Fernanda Lima): que ela tá pedindo. Então parte do item 1 tá mapeado aqui para poder virar banco de ideias.

Microphone: Perfeito.

Microphone: Tá, 1 e 4.

System audio (Fernanda Lima): Assim como 4 totalmente.

Microphone: Tá, 1 e 4 então, banco de ideias totalmente. Para o item 2 aí a gente precisa da avaliação de vocês aí, o que que a gente vai conseguir fazer sobre isso? Tá aí pendente avaliação da Então vamos lá, tá? O que que nós conversamos aqui? Importação da condição de pagamento, pelo que eu entendi, vai ficar como roadmap. O bloqueio, o Lucas vai validar, que é o item 3, será validado por Lucas. E o Lucas, logo depois que validar, manda aqui para a gente no chat se o comportamento foi conforme Então vamos lá, tá? O que que nós conversamos aqui? Então vamos fazer um compilado. Algum comportamento que a gente não conseguiu validar e testar do lado de cá, tá? Beleza. Depois disso, tá, o item 5, detalhamento de conta.

System audio (Fernanda Lima): Uhum.

Microphone: E data do débito ao alertar exclusão. Eu acho que isso também já foi um bug, já tá ali mapeado já como bug. Existe uma correção para ser feita. Aí essa outra questão do item 6, já que ele tá validando conosco, para nós, o ticket. O item 7, que é rotina de controle de alertas, de e se não será feito, tá? Não será feito, né? Nem banco de ideias, isso não será feito. Associação automática de depara, isso hoje já existe, foi apresentado ali para o Lucas. E a consulta e preenchimento tá em análise também pelo Jeff. É isso, falei besteira.

System audio: É, não, o último você pode falar que será feito e a previsão é de entrega. Aí você pode colocar aí um mês, fala que já tava no nosso roadmap aqui nos próximos meses. Não sei se isso vai— não seria data mais ou menos dia 1/11, Fernanda? Pode ser, porque de fato não é nada muito complexo e

Microphone: Lucas, pode jogar.

System audio (Fernanda Lima): Daria

System audio (Fernanda Lima): para encaixar, tá?

Microphone: Lucas, depois eu vou te passar outra data, tá? Vai falar que não, senão o pessoal de produto vai se apegar essa outra data.

System audio (Fernanda Lima): Tá.

System audio (Fernanda Lima): Sim.

System audio (Fernanda Lima): Júlia, não encontrei ticket sobre balança, tá? Provavelmente não deve ter sido aberto.

Microphone: Já faz abertura para mim, por gentileza. Pede prioridade, eu preciso que você acompanhe isso com urgência, tá?

System audio (Lucas Nogueira): Aí eu acho que é importante

System audio (Fernanda Lima): bater um papo já aqui com a Joyce, ou com a Ana,

System audio (Jaqueline Martins): com o pessoal lá do suporte, né, de quais dados eles precisam para o BDS, para o que seja Tá? Para chamado de balança, mas com certeza o pessoal do suporte deve saber. Pessoal,

System audio (Jaqueline Martins): a Ana com certeza sabe, a Joyce com certeza sabe, porque a gente já teve

System audio (Fernanda Lima): alguns casos, eles devem saber o que precisa, tá?

Microphone: Beleza, então.

Microphone: Sobre esses itens que ficaram pendentes com vocês, o Nanda tem data para dar devolutiva?

System audio (Fernanda Lima): Sobre esses itens de estudo?

Microphone: Isso.

System audio (Fernanda Lima): Não, mas eu vou arrumar uma data para você

System audio (Pamela Hort): da qual eu consiga cumprir.

Microphone: Tá.

Microphone: Tá, porque o cliente pediu para a gente dar um retorno para ele definitivo até hoje à tarde, tá?

System audio (Pamela Hort): Tá.

System audio (Pamela Hort): Não, assim

System audio (Pamela Hort): que o Leandro voltar aqui, eu vou alinhar com ele como que eu vou tratar isso dessas datas de estudo.

System audio (Fernanda Lima): Vou ver com ele o que um fluxo de resposta disso, e a gente bate um papo,

System audio (Fernanda Lima): Júlio. Pode ser?

Microphone: Tá bom, combinado então.

Microphone: Fechou?

System audio (Fernanda Lima): Obrigada a todos. Obrigado. Deixou esse? Tem mais dois que eu

System audio (Fernanda Lima): te devo, que você já me

System audio (Fernanda Lima): pediu.

Microphone: Aí, você aí.

System audio (Fernanda Lima): Tá.

Microphone: Obrigado, pessoal. Até mais.

System audio (Fernanda Lima): Até mais, gente. Tchau, gente. Obrigado.
