"""Motivo real de cada nota: um motivo principal por resposta.

Regra (definida em 29/09/2026 depois de ler comentários e colunas de motivo):
1. Comentário escrito com assunto específico manda, porque é a fala do cliente. Em detrator e neutro
   vale o primeiro assunto negativo do comentário; em promotor, o primeiro positivo. Quando a leitura
   do comentário pede um motivo diferente do assunto marcado, vale o que está em LEITURA.
2. Sem comentário útil, vale o motivo marcado pelo cliente ou registrado na tratativa, na ordem de
   prioridade do grupo e da classe (PRIORIDADE). "Outro" sozinho não conta como motivo.
3. Sem nada disso: "Sem motivo informado".
A pesquisa mostra opções diferentes para cada faixa de nota, então o motivo marcado já vem com o
sentido da classe (detrator só vê opções negativas; promotor, positivas).
"""

SEM = "Sem motivo informado"

# assunto do comentário (temas_comentarios.TEMAS) -> motivo real
TEMA = {
    "Lentidão e travamento": "Lentidão e quedas do sistema",
    "Falhas e erros de versão": "Erros e falhas do sistema",
    "Usabilidade e complexidade": "Facilidade de uso",
    "Relatórios e recursos": "Recursos e relatórios",
    "Evolução do produto": "Evolução e melhorias do produto",
    "Aderência ao negócio": "Aderência ao negócio",
    "Suporte": "Suporte",
    "Prazo e condução da implantação": "Condução da implantação",
    "Preço e custo": "Custo",
}
POSITIVOS = {"Elogio ao atendimento", "Elogio ao produto"}
GENERICOS = {"Avaliação genérica", "Sem conteúdo"}

# leitura do comentário quando o assunto marcado não diz o motivo real (id da resposta -> motivo)
LEITURA = {
    # 2026
    "95910674": "Facilidade de uso",            # "facilidade em acessar o sistema"
    "94888352": "Facilidade de uso",            # "fácil entendimento"
    "94699886": "Relacionamento com a Aliare",  # CS mais próximo, atento às necessidades
    "98111323": "Recursos e relatórios",        # processos manuais, falta automatizar a baixa de NF
    "97554306": "Recursos e relatórios",        # "fornece muitos dados e resultados"
    "97234749": "Facilidade de uso",            # "bom de trabalhar"
    "96539139": "Facilidade de uso",            # "facilidade"
    "94887517": "Aderência ao negócio",         # "acompanha a realidade brasileira"
    "94319130": "Aderência ao negócio",         # "gestão completa do negócio"
    # 2025
    "92666746": "Aderência ao negócio",         # "ERP completo"
    "90099851": "Aderência ao negócio",         # "atende muito bem o negócio"
    "88561107": "Aderência ao negócio",         # "bem desenvolvido para o agronegócio"
    "93013468": "Facilidade de uso",            # "muito prático"
    "91912653": "Facilidade de uso",            # "facilidade, simplicidade"
    "91010820": "Aderência ao negócio",         # "software muito completo"
    "90435999": "Aderência ao negócio",         # "sistema é completo"
    "88344053": "Aderência ao negócio",         # "não atendeu minhas expectativas"
}

# motivo marcado (rótulo original da pesquisa ou da tratativa) -> motivo real
MARCADO = {
    "Aderência do ERP ao seu Negócio": "Aderência ao negócio",
    "Aderência do ERP ao seu negócio": "Aderência ao negócio",
    "Aderência do ERP ao seu dia a dia": "Aderência ao negócio",
    "Aderência do produto ao seu negócio": "Aderência ao negócio",
    "Adaptação ao Negócio": "Aderência ao negócio",
    "Solução Alinhada ao Negócio": "Aderência ao negócio",
    "Produto ou Serviço de Alta Qualidade": "Aderência ao negócio",
    "Satisfeito com o produto": "Aderência ao negócio",
    "Falhas durante o uso do ERP": "Erros e falhas do sistema",
    "Falhas durante o uso do produto": "Erros e falhas do sistema",
    "Erro de versão": "Erros e falhas do sistema",
    "Atualização de versão do ERP": "Erros e falhas do sistema",
    "Segurança e Confiabilidade": "Erros e falhas do sistema",
    "Uso/navegação das funcionalidades do ERP": "Facilidade de uso",
    "Usabilidade": "Facilidade de uso",
    "Falta de Conhecimento": "Facilidade de uso",
    "Recursos do Produto": "Recursos e relatórios",
    "Recursos do produto": "Recursos e relatórios",
    "Produto": "Recursos e relatórios",
    "Desalinhamento entre Expectativas e Entregas": "Recursos e relatórios",
    "Demora na entrega de melhorias": "Evolução e melhorias do produto",
    "Falta de posicionamento - Melhorias": "Evolução e melhorias do produto",
    "Falta de posicionamento - RDM": "Evolução e melhorias do produto",
    "Custo x benefício": "Custo",
    "Experiência com o Suporte Aliare": "Suporte",
    "Atendimento do Suporte Aliare": "Suporte",
    "Suporte": "Suporte",
    "Satisfeito com o atendimento": "Suporte",
    "Demora no atendimento": "Suporte",
    "Experiência com outras áreas Aliare": "Relacionamento com a Aliare",
    "Experiência com outras áreas": "Relacionamento com a Aliare",
    "Falta de Contato": "Relacionamento com a Aliare",
    "Relacionamento": "Relacionamento com a Aliare",
    "Atendimento do Consultor": "Atendimento do consultor",
    "Experiência com o Apoio Técnico/Treinamento": "Atendimento do consultor",
    "Comunicação Clara e Proativa": "Atendimento do consultor",
    "Execução Eficiente": "Atendimento do consultor",
    "Planejamento e Organização": "Atendimento do consultor",
    "Comunicação Ineficiente": "Condução da implantação",
    "Comunicação": "Condução da implantação",
    "Problemas no Planejamento do Projeto": "Condução da implantação",
    "Planejamento e Execução": "Condução da implantação",
    "Experiência de Implantação": "Condução da implantação",
    "Execução do Projeto/Treinamento": "Condução da implantação",
    "Planejamento do Projeto/Treinamento": "Condução da implantação",
    "Problemas no Planejamento do Apoio Técnico/Treinamento": "Condução da implantação",
    "Dificuldades na Execução do Apoio Técnico/Treinamento": "Condução da implantação",
    "Dificuldades na Execução": "Condução da implantação",
}

_NEG_PRODUTO = ["Erros e falhas do sistema", "Lentidão e quedas do sistema", "Recursos e relatórios",
                "Evolução e melhorias do produto", "Facilidade de uso", "Suporte", "Relacionamento com a Aliare",
                "Aderência ao negócio", "Condução da implantação", "Atendimento do consultor", "Custo"]
_POS_PRODUTO = ["Aderência ao negócio", "Facilidade de uso", "Recursos e relatórios", "Suporte",
                "Relacionamento com a Aliare", "Atendimento do consultor", "Evolução e melhorias do produto",
                "Condução da implantação", "Erros e falhas do sistema", "Lentidão e quedas do sistema", "Custo"]
_NEG_SERV = ["Condução da implantação", "Atendimento do consultor", "Erros e falhas do sistema",
             "Lentidão e quedas do sistema", "Recursos e relatórios", "Evolução e melhorias do produto",
             "Facilidade de uso", "Suporte", "Relacionamento com a Aliare", "Aderência ao negócio", "Custo"]
_POS_SERV = ["Atendimento do consultor", "Condução da implantação", "Aderência ao negócio", "Facilidade de uso",
             "Suporte", "Recursos e relatórios", "Relacionamento com a Aliare", "Evolução e melhorias do produto",
             "Erros e falhas do sistema", "Lentidão e quedas do sistema", "Custo"]
PRIORIDADE = {("Serviços", True): _POS_SERV, ("Serviços", False): _NEG_SERV}


def _prioridade(grupo, promotor):
    return PRIORIDADE.get((grupo, promotor), _POS_PRODUTO if promotor else _NEG_PRODUTO)


def do_comentario(id_, temas, classe, grupo):
    """Motivo lido no comentário, ou None quando o comentário não diz o porquê."""
    if id_ in LEITURA:
        return LEITURA[id_]
    temas = temas or []
    neg = [t for t in temas if t not in POSITIVOS and t not in GENERICOS]
    pos = [t for t in temas if t in POSITIVOS]
    ordem = pos + neg if classe == "Promotor" else neg + pos
    for t in ordem:
        if t == "Elogio ao atendimento":
            return "Atendimento do consultor" if grupo == "Serviços" else "Suporte"
        if t in TEMA:
            return TEMA[t]
    return None


def do_marcado(marcados, classe, grupo):
    cats = {MARCADO[m] for m in marcados or [] if m in MARCADO}
    for c in _prioridade(grupo, classe == "Promotor"):
        if c in cats:
            return c
    return None


def motivo_real(id_, temas, marcados, classe, grupo):
    return do_comentario(id_, temas, classe, grupo) or do_marcado(marcados, classe, grupo) or SEM
