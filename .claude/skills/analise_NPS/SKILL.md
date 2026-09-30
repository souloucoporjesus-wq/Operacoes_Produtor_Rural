---
name: analise_NPS
description: >-
  Atualiza e apresenta a análise de NPS da vertical produtor rural (produto AgriManager, produto
  myFarm e serviços de implantação, apoio técnico e monitoria) a partir das exportações da Track:
  confere os totais com o painel da Track, lê os comentários novos, define o motivo real de cada
  nota, roda o notebook, gera a apresentação em arquivo único (visão geral, evolução acumulada,
  2025 × 2026, projeção contra a meta, motivos, comentários, cliente a cliente) e republica no
  mesmo link. Use sempre que o usuário chamar /analise_NPS ou falar em NPS, nota de NPS,
  detratores, promotores, motivo da nota, comentários da pesquisa, campanha ou exportação da
  Track, NPS do mês, NPS por produto ou por serviço, comparação com o ano anterior, meta ou
  projeção de NPS, ou apresentação de NPS para a diretoria ou o CEO, mesmo sem dizer "skill".
---

# /analise_NPS · NPS de produto e serviços

A análise mostra à diretoria (e ao CEO) como está a percepção do cliente em cada produto e
serviço, para onde está indo, por que o cliente dá a nota e se o ano fecha acima da meta. Tudo mora
na **pasta do NPS** (ver o mapa do `AGENTS.md`). A página publicada fica em
https://claude.ai/artifact/CWdhZDZNtvGv7zMxn38nED e o Julio também abre o arquivo local
`NPS 2026.html` direto no navegador, então ela precisa funcionar sem internet.

O método de análise é o da skill `analise_dados_senior`: uma pergunta por vez, resultado
conferido antes de virar conclusão, interpretação em vez de repetir número. Pergunta nova entra no
notebook acima da conclusão.

## O que tem na pasta

| arquivo | papel |
|---|---|
| `NPS produto - AGM.csv`, `NPS produto - myFarm.csv`, `NPS serviços.csv` | ano corrente, exportados da Track |
| `NPS AGM 2025.csv`, `NPS myFarm 2025.csv`, `NPS Serviço 2025.csv` | ano anterior, base de comparação e meta |
| `temas_comentarios.py` | assunto de cada comentário lido (`TEMAS`, pela coluna `#`), mapa dos motivos marcados (`MOTIVOS`) e rótulos que não são motivo (`IGNORAR`) |
| `motivo_real.py` | regra do motivo real de cada nota (`LEITURA`, `MARCADO`, prioridades por grupo e classe) |
| `montar_notebook.py` | monta e executa `analise-nps.ipynb`; grava `dados-nps.json` e `resumo-nps.json` |
| `reflexoes.py` | a interpretação escrita de cada resultado do notebook |
| `modelo-apresentacao.html` | a página, com marcadores `{{chave}}` (números do resumo) e `/*__DADOS__*/` |
| `gerar_apresentacao.py` | embute os dados e os números e grava `NPS 2026.html` |

## Passo 1. Receber as exportações

Os arquivos vêm da Track, **uma linha por resposta** (tela de opiniões), cada grupo com todas as
campanhas dele, período cheio do ano e nenhum outro filtro. Salvar na pasta com os nomes da tabela,
substituindo os anteriores. A leitura é `sep=";"` e `encoding="latin-1"`; conferir que o número de
linhas do arquivo bate com o de respostas lidas (comentário com aspas ou quebra de linha pode juntar
linhas).

## Passo 2. Conferir com o painel da Track

Nenhum número vai para a diretoria sem bater com a Track. Pedir ao Julio o print do painel (as
mesmas campanhas e o mesmo período) e comparar **por campanha**: detratores, neutros, promotores e
NPS. O notebook mostra essas contagens logo no começo. Se não bater, mostrar a conciliação por
campanha, dizer quantas respostas faltam e de qual classe, e pedir a reexportação antes de seguir.
Em 29/09/2026 a exportação de serviços veio com 5 promotores a menos (NPS 59 no arquivo, 62 na
Track), e o erro só apareceu porque o Julio comparou com o painel.

## Passo 3. Ler os comentários novos

O motivo real depende da leitura de cada comentário, então comentário novo precisa ser lido:

1. Listar os comentários que ainda não têm assunto: o notebook mostra, na checagem de leitura, os
   que ficaram como "Sem conteúdo". Texto de verdade nessa lista quer dizer comentário não lido.
2. Ler um por um e acrescentar o assunto em `TEMAS` (a chave é o `#` da resposta), usando os
   assuntos que já existem. Em comentário com mais de um assunto, o principal vem primeiro.
3. Quando o comentário diz o porquê mas o assunto não traduz (elogio que na verdade fala de
   facilidade de uso, "sistema completo" que é aderência ao negócio), registrar em `LEITURA`
   (`motivo_real.py`). Elogio genérico ("muito bom") fica sem leitura: cai no motivo marcado.
4. Rótulo de motivo novo na pesquisa ou na tratativa vai para `MOTIVOS` e `MARCADO`; rótulo de
   produto ou raiz da árvore de categorias vai para `IGNORAR`.

## Passo 4. Rodar o notebook e interpretar

Na pasta do NPS: `python montar_notebook.py`. Ler os resultados de verdade, passar pela revisão
crítica da `analise_dados_senior` (o `n` visível, base pequena não é tendência, associação não é
causa) e atualizar `reflexoes.py` com a interpretação do que mudou, com as tags [Certo],
[Provável] e [Suposição]. Rodar de novo até não sobrar "(a preencher depois de ler o output)" e sem
célula com erro.

## Passo 5. Gerar a página e revisar o texto fixo

1. `python gerar_apresentacao.py`. Ele avisa se algum marcador ficou sem número.
2. **Reler cada frase da Visão geral contra o notebook.** Os quadros têm texto fixo em volta dos
   números e citam clientes e falas específicas ("melhorou a cada trimestre", "dois em cada três",
   o caso do Condomínio Itaguassu, a fala da Parceria Agrícola). A Parte 4 do notebook lista os
   candidatos do mês: contas que foram de detrator a promotor, respondentes que viraram promotores,
   elogios ao atendimento. O que deixou de ser verdade é reescrito.
3. Conferir o script da página: extrair o trecho entre `<script>` e `</script>` e rodar
   `node --check`.
4. Uma olhada só: captura sem janela do Edge (modo claro) das abas que mudaram. Corrigir o que
   estiver visivelmente quebrado, sem entrar em ciclo de capturas.

## Passo 6. Publicar

Republicar `NPS 2026.html` no mesmo link (de outra conversa, passar o `url` e ler antes). Lembrar
o Julio de que o link é privado: para outra pessoa abrir, ele libera no menu Share da página.

## Versão para a diretoria e o CEO

Regras que o Julio pediu para a apresentação:

- **Visão geral só com o ano corrente e em tom positivo:** primeiro o que sustenta a nota; o
  desafio dito de forma construtiva ("o desafio é trazer o cliente para a conversa"); cliente que
  melhorou citado pelo nome; elogio do cliente ao CS com a fala dele. Os quadros do topo não
  comparam com o ano anterior: mostram % de promotores e o melhor mês.
- **Projeções escondidas por padrão.** O botão só com ícone, no topo, mostra ou esconde a aba
  Projeção, a frase de projeção da abertura e a linha da meta.
- **Texto:** sem hífen nem travessão, sem nome de pessoa do time em plano de ação, sem seção de
  ressalvas ou de metodologia, português sem termo em inglês.
- **Positivo não é inventado.** Toda frase da página precisa ser verdade nos dados. Status ou
  número só muda com o fato confirmado pelo Julio, e a confirmação fica registrada no notebook com
  data. Exemplo: os detratores de 2026 que a Track mostrava como pendentes até 29/09/2026 foram
  confirmados como tratados (a Track não atualizou os loops); isso está em `CONFIRMADO_ATE`, no
  `montar_notebook.py`. Pendente novo precisa de confirmação nova, perguntada ao Julio.
- **A foto inteira vai para o Julio no chat.** O que a página não mostra, mas o CEO pode perguntar
  (quantos baixaram a nota, tendência pequena demais para chamar de melhora, queda que está só nas
  outras abas), é dito a ele antes da reunião.

## Como ler os dados

- **Acumulado, não o mês isolado.** NPS é % de promotores (9 e 10) menos % de detratores (0 a 6).
  O painel da Track usa o acumulado do ano; o mês isolado com poucas respostas engana (o −33 de
  serviços em setembro de 2026 eram 3 respostas). Ponto com menos de 10 respostas aparece vazado.
- **Opções de motivo por faixa de nota.** A lista de motivos da pesquisa muda conforme a nota:
  detrator só vê opções negativas, promotor só positivas. Motivo só se compara dentro da mesma
  classe; o útil é comparar a mesma classe entre anos.
- **Onde vem o motivo em cada arquivo.** AgriManager: dentro do comentário, depois de
  `## Justificativas ##`, sem vírgula entre as opções. myFarm: não tem motivo marcado, só a
  categoria da tratativa, que costuma dizer "usabilidade" quando o cliente fala de lentidão.
  Serviços: coluna `Justificativas`.
- **Motivo real.** Um por resposta: o comentário manda; sem comentário útil, vale o motivo marcado
  na ordem de prioridade do grupo e da classe; "Outro" sozinho conta como sem motivo informado.
  Grupo com menos de 10 respostas aparece em contagem.
- **Cliente a cliente.** A conta pode ter vários usuários. Primeira e última nota saem pela data e
  hora; o JSON da página guarda só a data, e respostas do mesmo dia podem empatar.
- **Resposta interna.** Nome de alguém da Aliare como respondente (já apareceu o do diretor na base
  do myFarm de 2025) é apontado ao Julio antes de apresentar.
- **Arredondamento.** O resumo arredonda meio para cima, igual à página; arredondamento diferente
  faz o texto dizer 66% e o quadro 67%.
- **Projeção e meta.** A meta, definida pelo Julio em 29/09/2026, é superar o NPS fechado do ano
  anterior em cada grupo. A projeção usa o volume e o NPS dos últimos três meses, com três cenários
  (ritmo atual, repetir o fim do ano anterior, repetir o melhor trimestre do ano) e o NPS que o
  restante do ano precisaria ter para bater a meta.

## Virada de ano

Em 2027: o ano que fechou vira a base de comparação e a meta. Acrescentar os arquivos novos em
`ARQ` no `montar_notebook.py`, trocar os anos fixos (as variáveis `n26` e `n25`, os textos com
"2026" no modelo da página e nas reflexões) e confirmar com o Julio a meta do novo ano.

## Fim

Registrar pelo `/atualizar`: o que mudou nos números, o link publicado e o que ficou pendente
(reexportação, status para atualizar na Track, confirmação que falta).
