"""Categorias de análise e o texto das notas (observações) que explicam cada coluna da planilha."""

ERRO_PRODUTO = "Erro de produto"
CATEGORIAS = {
    ERRO_PRODUTO: ("C0392B", "F5B7B1", "Bug, Solução de contorno e Problema com causa \"Bug no Produto / ERP\". É o que o desenvolvimento corrige."),
    "Problema de configuração": ("E67E22", "FAD7A0", "Problema com causa \"Configuração\"."),
    "Erro de uso": ("B7950B", "FCF3CF", "Problema com causa \"Erro operacional\" (uso incorreto do sistema)."),
    "Externo ou sem causa definida": ("7F8C8D", "D5DBDB", "Problema com causa SEFAZ ou aplicativo de terceiros, não identificada, resolvido pelo próprio usuário ou sem causa registrada."),
    "Dúvida": ("2E86C1", "AED6F1", "Categoria \"Dúvida\"."),
    "Melhoria no produto": ("1E8449", "ABEBC6", "Adequação com necessidade \"Melhoria\" ou \"Sugestão Roadmap (Ideia)\"."),
    "Adequação à legislação": ("8E44AD", "D7BDE2", "Adequação com necessidade \"Legislação\"."),
    "Solicitação de serviço": ("C2185B", "F8BBD0", "Categoria \"Solicitação de serviço\" (instalação, atualização, licença, balança)."),
}

SIGNIFICADO = {
    ERRO_PRODUTO: "Defeito do sistema: é o que o desenvolvimento corrige.",
    "Problema de configuração": "Parametrização do sistema no cliente que gerou problema.",
    "Erro de uso": "O usuário operou o sistema de forma errada. Aponta necessidade de treinamento.",
    "Externo ou sem causa definida": "Problema que não é do AgriManager (SEFAZ, aplicativo de terceiros) ou sem causa apontada pelo suporte.",
    "Dúvida": "O cliente perguntou como fazer algo no sistema.",
    "Melhoria no produto": "O cliente pede algo que o sistema ainda não faz.",
    "Adequação à legislação": "Mudança exigida por lei ou pelo fisco.",
    "Solicitação de serviço": "Pedido de serviço técnico: instalação, atualização de versão, licença, balança, ambiente.",
}

SCORE, FILA, BASE, CONTRATOS, PARAM = "Score dos clientes", "Fila de atendimento", "Base de tickets", "Contratos", "Parâmetros"
VEM_DO_SCORE = " Vem da aba Score dos clientes (a explicação completa está na nota da coluna lá)."


def _pct(v):
    return f"{v * 100:.1f}".replace(".", ",") + "%"


def montar_notas(participacao):
    """participacao: {categoria: fração dos tickets da análise}. Devolve a lista de notas a aplicar.

    Cada nota: aba, linha do cabeçalho (None = procura em qualquer linha), texto da célula a achar,
    deslocamento de coluna a partir dela e o texto da nota."""
    notas = []

    def add(aba, linha, procurar, nota, desloc=0):
        notas.append({"aba": aba, "linha": linha, "procurar": procurar, "deslocamento": desloc, "nota": nota})

    s = lambda procurar, nota: add(SCORE, 1, procurar, nota)
    s("Prioridade CS", "Marcação humana do CS: escolha Sim ou Não na lista da célula. Cliente com Sim vai para o topo da aba Fila de atendimento, na frente de todos, qualquer que seja o score. Não altera o score: é a decisão do CS por cima do cálculo.")
    s("Cliente (grupo econômico)", "Nome do grupo econômico (um grupo pode reunir várias fazendas e CNPJs). Vem da Lista de Clientes, do contrato ativo de maior valor do grupo. Quando o grupo não está na lista, usa o nome que mais aparece nos tickets.")
    s("Valor mensal", "Quanto o grupo paga por mês hoje. Soma do VALOR_CONTRATO de todos os contratos ATIVOS do grupo na aba Contratos, em todos os produtos (AgriManager, myFarm, Cloud, Vistra BI). Contrato suspenso ou cancelado não entra. Zero = sem contrato ativo ou grupo fora da Lista de Clientes.")
    s("Score", "Nota de 0 a 100 que define a prioridade. Cada cliente recebe sua posição relativa entre todos os clientes da planilha em três itens (0 = o menor da lista, 1 = o maior): valor mensal, erros de produto e total de tickets.\nScore = 100 x (40% da posição no valor + 40% da posição nos erros de produto + 20% da posição no volume).\nUsar a posição, e não o número bruto, evita que um cliente muito grande achate todos os outros. Pesos na aba Parâmetros.")
    s("Urgência", "Nível a partir do score (cortes na aba Parâmetros): Crítica a partir de 85; Alta a partir de 70; Média a partir de 45; Baixa abaixo de 45.\nRegra extra: cliente entre os 10% com mais erros de produto fica no mínimo em Alta, mesmo com score menor. Muito erro de produto é urgência mesmo em cliente pequeno.")
    s("Categoria em destaque", "Tipo de ticket em que o cliente mais foge do padrão da base. Para cada categoria: (% da categoria nos tickets do cliente) dividido por (% da categoria em toda a base). Vence a maior razão.\nSó vale com pelo menos 5 tickets do cliente na categoria e razão de 1,5x ou mais; se nenhuma chegar lá, aparece \"Perfil na média\". A cor é a da categoria.")
    s("Vezes acima da média", "Quantas vezes a proporção da Categoria em destaque neste cliente supera a proporção dela na base inteira. Ex.: 3,4x em Erro de produto = a fatia de erro de produto deste cliente é 3,4 vezes a média. Vazio quando o perfil está na média.")
    s("Categoria predominante", "Tipo de ticket que o cliente mais abre em números absolutos (a maior das 8 colunas de categoria). Na maioria dos clientes é Dúvida, porque dúvida é quase metade da base; por isso use junto com a Categoria em destaque.")
    s("Total de tickets", "Soma das 8 colunas de categoria: todos os tickets do cliente de 02/01/2025 a 22/09/2026, só os abertos pelo próprio cliente (sem tickets internos, cancelados e pesquisas de satisfação).")
    s("% erro de produto", f"Erros de produto dividido pelo Total de tickets: quanto do volume do cliente é defeito do sistema. Na base inteira, erro de produto é {_pct(participacao[ERRO_PRODUTO])} dos tickets.")
    for cat, (_, _, desc) in CATEGORIAS.items():
        s(cat, f"Quantidade de tickets do cliente nesta categoria no período. O que entra: {desc}\n{SIGNIFICADO[cat]} Na base inteira, é {_pct(participacao[cat])} dos tickets.\nContado na aba Base de tickets pelo código do grupo econômico. Quanto mais forte a cor, mais tickets.")
    s("Em aberto hoje", "Tickets do cliente ainda não Fechados, Resolvidos ou Cancelados na data da base (22/09/2026): Aguardando, Pausado, Produto | Desenvolvimento, Novo ou Em Andamento.")
    s("Tickets nos últimos 6 meses", "Tickets abertos a partir de 22/03/2026 (6 meses antes da última data da base). Compare com o Total de tickets pra ver se o cliente está abrindo mais ou menos ticket recentemente. A data de início está na aba Parâmetros.")
    s("Situação AgriManager", "Situação dos contratos AgriManager do grupo na aba Contratos: Ativo; Suspenso; Cancelado; \"Sem contrato AgriManager\" (o grupo só tem outros produtos); ou \"Fora da lista de clientes\" (o grupo abre ticket mas não aparece na Lista de Clientes).")
    s("Valor mensal AgriManager", "Parte do Valor mensal que vem só dos produtos AgriManager ativos (ERP, Autorize, Algodoeira). Todos os tickets desta análise são de AgriManager.")
    s("Curva", "Curva ABC do cliente (A = maior faturamento). Vem da Lista de Clientes; se o grupo não está lá, vem da planilha de tickets.")
    s("CS responsável", "Agente de relacionamento (CS) do contrato ativo de maior valor do grupo, na Lista de Clientes. Vazio quando o grupo não está na lista.")
    s("Gerente de conta", "Gerente de conta do contrato ativo de maior valor do grupo, na Lista de Clientes.")
    s("ID grupo econômico", "Código do grupo econômico: a chave que cruza as duas planilhas (\"ID Grupo Econômico\" nos tickets = \"CODI_GRUPO\" na Lista de Clientes). Todas as contas desta linha partem deste código.")
    s("Ordem (auxiliar)", "Coluna oculta que monta a Fila de atendimento: score + 1000 quando Prioridade CS = Sim (é o que garante o topo). Não editar.")
    for cat in CATEGORIAS:
        s(f"Fator {cat} (auxiliar)", f"Coluna oculta usada na Categoria em destaque: proporção de \"{cat}\" nos tickets do cliente dividida pela proporção na base inteira. Fica zero quando o cliente tem menos de 5 tickets nesta categoria. Não editar.")

    f = lambda procurar, nota: add(FILA, 4, procurar, nota)
    f("Posição", "Ordem de atendimento (1 = primeiro). Clientes com Prioridade CS = Sim vêm antes de todos, ordenados pelo score entre si; depois vêm os demais, do maior para o menor score. Esta aba é toda calculada: não editar.")
    f("Prioridade CS", "Espelho da marcação feita na aba Score dos clientes. Para mudar, altere lá: a fila se reordena sozinha.")
    f("Cliente (grupo econômico)", "Nome do grupo econômico." + VEM_DO_SCORE)
    f("Valor mensal", "Quanto o grupo paga por mês hoje (contratos ativos, todos os produtos)." + VEM_DO_SCORE)
    f("Score", "Nota de 0 a 100: 40% valor pago, 40% erros de produto, 20% volume de tickets, em posição relativa entre os clientes." + VEM_DO_SCORE)
    f("Urgência", "Crítica, Alta, Média ou Baixa, a partir do score e da regra de erros de produto." + VEM_DO_SCORE)
    f("Categoria em destaque", "Tipo de ticket em que o cliente mais foge da média da base." + VEM_DO_SCORE)
    f("Vezes acima da média", "Quantas vezes a Categoria em destaque supera a média da base neste cliente." + VEM_DO_SCORE)
    f("Categoria predominante", "Tipo de ticket que o cliente mais abre em números absolutos." + VEM_DO_SCORE)
    f(ERRO_PRODUTO, "Quantidade de tickets de defeito do sistema (Bug, Solução de contorno, Problema causado por bug)." + VEM_DO_SCORE)
    f("Total de tickets", "Todos os tickets abertos pelo cliente no período." + VEM_DO_SCORE)
    f("Em aberto hoje", "Tickets do cliente ainda não fechados, resolvidos ou cancelados." + VEM_DO_SCORE)
    f("CS responsável", "Agente de relacionamento (CS) do grupo." + VEM_DO_SCORE)
    f("Linha (auxiliar)", "Coluna oculta: a linha da aba Score dos clientes que ocupa esta posição da fila. Não editar.")

    for cat, (_, _, desc) in CATEGORIAS.items():
        c = lambda procurar, nota: add(cat, 4, procurar, nota)
        c("Posição", "Ranking do cliente nesta categoria: 1 = quem mais abriu este tipo de ticket. Empate desempata pelo valor mensal.")
        c("Cliente (grupo econômico)", "Nome do grupo econômico, o mesmo da aba Score dos clientes.")
        c("Valor mensal", "Quanto o grupo paga por mês hoje (contratos ativos, todos os produtos). Vem da aba Score dos clientes.")
        c("Tickets nesta categoria", f"Quantidade de tickets do cliente classificados como \"{cat}\" no período, só os abertos pelo próprio cliente. O que entra: {desc}")
        c("Total de tickets do cliente", "Todos os tickets do cliente no período, de todas as categorias.")
        c("% desta categoria no cliente", f"Tickets nesta categoria dividido pelo Total de tickets do cliente. Para comparar: na base inteira, \"{cat}\" é {_pct(participacao[cat])} dos tickets.")
        c("Em aberto nesta categoria", "Tickets desta categoria do cliente ainda não fechados, resolvidos ou cancelados na data da base (22/09/2026).")
        c("Urgência do cliente", "Urgência geral do cliente (aba Score dos clientes), que considera valor pago, erros de produto e volume; não é só desta categoria.")
        c("Prioridade CS", "Espelho da marcação feita na aba Score dos clientes.")
        c("Principais módulos", "As 3 telas ou rotinas do AgriManager com mais tickets desta categoria para o cliente, com a quantidade entre parênteses. Vem do 4º nível de serviço do ticket (ou do 3º nível quando o 4º está vazio). Mostra onde está o problema. Calculado na geração da planilha.")
        c("Ticket mais recente", "Data de abertura e assunto do ticket mais recente do cliente nesta categoria. Calculado na geração da planilha.")
        c("ID grupo econômico", "Código do grupo econômico, usado para buscar os dados nas outras abas.")

    origem = lambda col: f"Vem da planilha \"Analise de tickets abertos\", coluna \"{col}\"."
    b = lambda procurar, nota: add(BASE, 1, procurar, nota)
    b("Ticket", origem("Ticket") + " Todos os 20.587 tickets estão aqui, inclusive os que ficam fora da análise (ver coluna Entra na análise).")
    b("Abertura", origem("Abertura") + " Usada na janela dos últimos 6 meses.")
    b("ID grupo econômico", origem("ID Grupo Econômico") + " É a chave de cruzamento com a Lista de Clientes (CODI_GRUPO).")
    b("Grupo econômico (nome no ticket)", origem("Grupo Econônomico") + " O nome pode variar para o mesmo grupo (filial, fazenda); a chave confiável é o ID.")
    b("Tipo", origem("Tipo") + " Público = aberto pelo cliente; Interno = aberto por alguém da Aliare. Só Público entra na análise.")
    b("Status", origem("Status") + " Cancelado fica fora da análise; Fechado, Resolvido e Cancelado contam como encerrados.")
    b("Prioridade", origem("Prioridade") + " Não entra no score.")
    b("Categoria", origem("Categoria") + " Base da classificação na coluna Categoria de análise.")
    b("Causa", origem("Causa") + " Preenchida só em Problema; separa erro de produto, configuração, erro de uso e causa externa.")
    b("Necessidade", origem("Necessidade") + " Preenchida em Adequação; separa melhoria de produto de exigência legal.")
    b("Categoria de análise", "Coluna criada. Classificação usada em toda a planilha, a partir de Categoria + Causa + Necessidade, pela tabela de regras da aba Parâmetros (dá pra alterar lá).\nEx.: Problema com causa \"Bug no Produto / ERP\" vira Erro de produto; Adequação com necessidade \"Legislação\" vira Adequação à legislação. \"Fora da análise\" = pesquisa de satisfação ou ticket sem categoria.")
    b("Entra na análise", "Coluna criada. Sim quando o ticket foi aberto pelo cliente (Tipo = Público), não foi cancelado e não é pesquisa de satisfação. Só os Sim entram nas contagens das outras abas (19.150 de 20.587).")
    b("Em aberto", "Coluna criada. Sim quando o Status não é Fechado, Resolvido nem Cancelado.")
    b("Módulo (4º nível)", origem("4° Nível Serviço") + " Tela ou rotina do AgriManager envolvida no ticket.")
    b("Área (3º nível)", origem("3° Nível Serviço") + " Área do sistema, ex.: Administrativo/Financeiro, Armazenagem, Controladoria.")
    b("Squad", origem("Squad") + " Equipe do suporte que atendeu.")
    b("Assunto", origem("Assunto"))
    b("Avaliação", origem("Avaliação") + " Nota do cliente ao atendimento, quando respondeu a pesquisa.")

    k = lambda procurar, nota: add(CONTRATOS, 1, procurar, nota)
    k("CODI_GRUPO", "Esta aba é a Lista de Clientes original, sem as 3 linhas de rodapé do relatório e sem a coluna de CPF/CNPJ. Uma linha por contrato.\nCODI_GRUPO: código do grupo econômico, a chave que cruza com os tickets. Contrato sem código não entra em nenhum cliente.")
    k("VALOR_CONTRATO", "Valor mensal do contrato. Os contratos ATIVOS somam R$ 1,287 milhão, o faturamento mensal recorrente da base. A soma dos ativos de cada grupo é o Valor mensal da aba Score dos clientes.")
    k("SITUACAO_CONTRATO", "ATIVO, SUSPENSO ou CANCELADO. Só ATIVO entra no Valor mensal.")
    k("PRODUTO", "Produto do contrato. Os que começam com AGRIMANAGER entram no Valor mensal AgriManager e na Situação AgriManager.")
    k("PERIODICIDADE", "Forma de cobrança: 1 = mensal, 6 = semestral, 12 = anual.")

    p = lambda rotulo, nota: add(PARAM, None, rotulo, nota, desloc=1)
    p("Peso do valor pago", "Quanto o valor mensal pesa no score. Os três pesos precisam somar 100%.")
    p("Peso dos erros de produto", "Quanto a quantidade de erros de produto pesa no score. Os três pesos precisam somar 100%.")
    p("Peso do volume total de tickets", "Quanto o total de tickets pesa no score. Os três pesos precisam somar 100%.")
    p("Urgência Crítica a partir do score", "Score igual ou acima deste valor = Crítica. Com 85, ficam cerca de 10% dos clientes.")
    p("Urgência Alta a partir do score", "Score igual ou acima deste valor (e abaixo do corte da Crítica) = Alta.")
    p("Urgência Média a partir do score", "Score igual ou acima deste valor (e abaixo do corte da Alta) = Média. Abaixo dele = Baixa.")
    p("Cliente entre os X% com mais erros de produto é no mínimo Alta (percentil)", "90% = o cliente que tem mais erros de produto que 90% dos outros fica no mínimo em Alta, mesmo com score menor.")
    p("Categoria em destaque: mínimo de tickets do cliente no tipo", "Evita destacar um cliente por causa de 1 ou 2 tickets: abaixo deste número a categoria não pode ser o destaque.")
    p("Categoria em destaque: quantas vezes acima da média da base", "A partir de quantas vezes acima da média a categoria vira destaque. Abaixo disso, o cliente aparece como Perfil na média.")
    p("Última data da base de tickets", "Data do ticket mais recente da base. Se trocar a base de tickets, atualize aqui: a janela dos últimos 6 meses é calculada a partir dela.")
    p("Início da janela \"últimos 6 meses\"", "Calculada: 6 meses antes da última data da base. Usada na coluna Tickets nos últimos 6 meses.")
    add(PARAM, None, "Categoria de análise", "Pode alterar: trocar a categoria de análise de uma combinação reclassifica todos os tickets dela na Base de tickets e recalcula a planilha inteira. Use exatamente um dos 8 nomes de categoria.")
    return notas
