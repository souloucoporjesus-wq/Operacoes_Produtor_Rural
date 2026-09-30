leitura_base = """**Leitura:** as seis bases juntas somam 1.292 respostas, todas com campanha e produto
identificados (duas respostas de serviço de 2025 vieram sem linha de produto e ficam fora só do
filtro por produto). O motivo existe pra quase todo AgriManager e serviços, mas **quase nunca pro
myFarm**: 11 de 359 respostas em 2025 e 17 de 281 em 2026. No myFarm, o "porquê" da nota depende do
comentário escrito, que não é obrigatório. Os comentários sem conteúdo (texto de teste, "sem
comentário") estão listados acima e ficam fora da leitura de assunto."""

q1 = """**Resultado:** três realidades diferentes em 2026. O AgriManager empata promotor e detrator
(NPS perto de zero, com 4 em cada 10 respostas de detrator). O myFarm tem 2 em cada 3 respostas de
promotor, mas 1 em 4 de detrator, quase sem neutro: o cliente myFarm ou gosta ou não gosta. Serviços
é o ponto mais alto, e isso vale pras três campanhas com base razoável (implantação myFarm, apoio
técnico AgriManager e myFarm). A monitoria AgroScore tem 3 respostas, não dá pra ler sozinha. A
margem de erro do NPS anual fica entre 5 e 9 pontos, então a distância entre os três é real.
Atenção: em serviços a Track mostra 61 respostas e NPS 62; o arquivo exportado tem 56 e dá 59.
Faltam 5 promotores na exportação, a reexportação corrige."""

q2 = """**Resultado:** o NPS isolado de cada mês só se lê sem susto no myFarm (22 a 44 respostas por
mês). No AgriManager, o salto de setembro (7 respostas) é ruído, e serviços tem meses com 1 a 3
respostas: o −33 de setembro em serviços são 3 respostas, não uma queda. Por isso a leitura
principal passa a ser o acumulado do ano, logo abaixo."""

q_acum = """**Resultado:** o acumulado do ano é a conta que a Track mostra. Nele, o AgriManager fica
entre 0 e 4 o ano inteiro, sem tendência. O **myFarm desce quase todo mês**, de 61 em janeiro pra
41 em setembro; em oito meses, só março e agosto tiveram variação positiva, e pequena. Serviços
começa com 1 resposta em janeiro, então o tombo de março é efeito de base pequena; de março em
diante fica entre 57 e 65."""

q3 = """**Resultado:** no trimestre a tendência aparece limpa. O **myFarm caiu de 53 pra 36 e pra 32**,
porque os promotores foram de 74% pra 60% e os detratores de 21% pra 29%. O AgriManager ficou parado
entre 0 e 5. Serviços manteve perto de 60 nos três trimestres."""

q4 = """**Resultado:** no AgriManager, o detrator aponta **falhas e estabilidade** (6 em cada 10) e
**recursos do produto** (5 em cada 10), seguidos de suporte. Esses motivos quase não aparecem entre
promotores, que citam **aderência ao negócio**: o sistema atende o processo, o que incomoda é o erro
e o que falta. A pesquisa pode mostrar opções diferentes conforme a nota, então isso descreve o que
cada grupo marca, não prova causa. No myFarm, só 11 dos 71 detratores têm motivo, e usabilidade
lidera; é base pequena demais pra ranking, o comentário diz mais (abaixo)."""

q5 = """**Resultado:** o comentário confirma e completa. No myFarm, **lentidão e travamento** é o assunto
de 10 comentários de detrator, bem à frente de qualquer outro: é a queixa concreta que a categoria
"usabilidade" esconde. No AgriManager, o texto fala de sistema complexo, erro depois de atualização
de versão e falta de recurso (custos, fiscal, relatórios). Em serviços, 18 comentários elogiam o
consultor pelo nome; a crítica fica na implantação (horas vendidas, prazo longo, troca de
consultor), não na pessoa."""

q6 = """**Resultado:** pelo status gravado na Track, dos 142 detratores de 2026 só 24 aparecem como
resolvidos ou esclarecidos, 46 foram encerrados sem conseguir contato e 51 aparecem como pendentes,
espalhados por todos os meses desde janeiro. Os pendentes não refletem o trabalho feito: veja o ajuste
logo abaixo."""

q7 = """**Resultado:** entre quem respondeu mais de uma vez em 2026, **caíram mais clientes do que
subiram** nos dois produtos (AgriManager 10 contra 5; myFarm 18 contra 9). No myFarm, isso reforça a
queda do trimestre com gente que já estava na base."""

q_meta = """**Resultado:** no mesmo ponto do ano, os três estão abaixo de 2025: AgriManager 4 pontos,
myFarm 12, serviços 16 (13 com o número da Track). A meta de dezembro é o fechamento de 2025. No
myFarm e em serviços ela é mais baixa que o setembro de 2025, porque o fim de 2025 foi fraco nesses
dois; no AgriManager é mais alta, porque o AgriManager teve o melhor trimestre de 2025 justamente de
outubro a dezembro (NPS 21)."""

q_comp = """**Resultado:** o myFarm começou 2026 à frente de 2025 e ficou para trás a partir de junho: a
diferença no acumulado foi de 25 pontos a favor em fevereiro pra 14 contra em agosto. O AgriManager
está abaixo de 2025 desde fevereiro, com distância estável entre 3 e 8 pontos. Serviços oscila pela
base pequena, mas está abaixo de 2025 desde abril."""

q_mf_patamar = """**Resultado:** a queda do myFarm **começou em setembro de 2025**, não em 2026. O patamar
de abril a agosto de 2025 (70, com 81% de promotores) caiu pra 26 de setembro a dezembro de 2025,
voltou a 53 no 1º trimestre de 2026 e caiu de novo pra 34 de abril a setembro. Cada bloco tem de 100
a 170 respostas, então as mudanças são bem maiores que a margem de erro (perto de 8 pontos). O
arquivo não diz a causa; o que acompanha a queda nos comentários é a lentidão (próxima seção)."""

q_vol = """**Resultado:** de janeiro a setembro, o AgriManager recebeu 37% menos respostas que em
2025 e serviços 25% menos; o myFarm manteve o volume. Menos respostas não mudam o NPS por si, mas
deixam o acumulado mais sensível a cada nota e diminuem o quanto dá pra recuperar até dezembro.
[Suposição] No AgriManager, pode ser menos disparo ou menos usuário ativo; a exportação só traz
quem respondeu, então não dá pra separar."""

q_motivos = """**Resultado:** o perfil do detrator do AgriManager é o mesmo de 2025: falhas e
estabilidade em 6 de cada 10, suporte e relacionamento em 1 de cada 3; recursos do produto subiu de
44% pra 53%. No comentário escrito, a queixa de suporte do AgriManager caiu (9 comentários de
detrator de janeiro a setembro de 2025, 2 em 2026) [Provável, base pequena]. No myFarm, **lentidão e
travamento foi de 3 pra 10 comentários de detrator**; os motivos marcados do myFarm não permitem
comparar os anos (1 detrator com motivo em 2025). Serviços tem 5 detratores por ano, base pequena
demais pra ler motivo."""

q_proj = """**Resultado:** **nenhum dos três fecha 2026 acima de 2025 em nenhum dos cenários.**
- AgriManager: o melhor cenário (repetir o 4º trimestre de 2025) leva a 5; pra passar de 8,5,
  outubro a dezembro precisariam de NPS 38, e o melhor trimestre de 2026 foi 5.
- myFarm: o melhor cenário (repetir o 1º trimestre de 2026) leva a 44; seria preciso 67 no 4º
  trimestre, acima de qualquer trimestre dos dois anos (o melhor foi 65, no 2º trimestre de 2025).
- Serviços: a conta não fecha nem com 100% de promotores; com o volume atual, o 4º trimestre teria
  que ter mais promotores líquidos do que respostas.

A simulação confirma: chance de 4% no AgriManager e abaixo de 1% nos outros dois. [Provável] Isso só
muda se o volume de respostas crescer muito, e com nota alta, o que não aparece em nenhum mês de 2026."""

q_menu = """**Resultado:** [Certo] a lista de motivos **muda conforme a nota**. Quem dá de 0 a 6 só vê
opções negativas (falhas, recursos, atendimento do suporte, atualização de versão, falta de contato);
quem dá 7 ou 8 vê usabilidade, aderência ao dia a dia e suporte; quem dá 9 ou 10 vê aderência ao
negócio, suporte e outras áreas. Por isso "usabilidade" só aparece entre neutros e "falhas" só entre
detratores: é o cardápio da pesquisa, não uma descoberta. O motivo marcado só compara dentro da
mesma classe, e a comparação útil é de um ano para o outro dentro da classe."""

q_bate = """**Resultado:** em serviços o motivo marcado e o comentário contam a mesma história em 9 de
cada 10 casos; no AgriManager, em 7 de cada 10. **No myFarm, só em 4 de cada 10.** O desencontro mais
comum, somando os grupos, é a tratativa registrar "usabilidade" ou "falhas" quando o cliente escreveu
sobre lentidão (17 casos). É por isso que o motivo real usa o comentário primeiro."""

q_outro = """**Resultado:** marcar só "Outro" (sem nenhuma categoria de tratativa) é raro no produto,
mas em serviços de 2026 são 20 respostas, e só 2 com comentário. Nessas, o motivo fica em branco. É
uma perda de informação nova de 2026 em serviços: em 2025 eram 4."""

q_real = """**Resultado:** com um motivo principal por resposta, a leitura fica direta. **No AgriManager,
o detrator sai por erros e falhas do sistema (metade) e por falta de recursos e relatórios (um em
cada quatro)**; o promotor fica pela aderência ao negócio (três em cada quatro). **No myFarm, dos 71
detratores de 2026, só 16 dizem o porquê, e 9 deles falam de lentidão e quedas do sistema.** Em
serviços, o promotor elogia o consultor (quase 9 em cada 10) e os poucos detratores reclamam da
condução da implantação. No myFarm, 183 de 187 promotores não dizem por que gostam; não dá para
tirar motivo de promotor ali."""

q_real_ano = """**Resultado:** o detrator do AgriManager tem o mesmo perfil nos dois anos (erros e falhas
em pouco mais da metade), com recursos e relatórios subindo de 19% para 26% e suporte caindo de 13%
para 9% [Provável, diferenças perto da margem]. No myFarm, a lentidão foi de 3 de 8 detratores que
disseram o motivo em 2025 para 9 de 16 em 2026; a base é pequena, mas vai na mesma direção dos
comentários. Serviços tem 5 detratores por ano, sem base para comparar."""

q6b = """**Resultado:** com a confirmação de que os pendentes já foram tratados, 85 dos 142 detratores
de 2026 aparecem como tratados pelo CS. O que sobra é, principalmente, contato que não aconteceu: em
46 casos o cliente não atendeu às tentativas do CS. É o desafio de trazer o cliente para a conversa.
Para a Track bater com a apresentação, os status dos loops precisam ser atualizados na plataforma."""

q_positivos = """**Resultado:** há boas histórias em 2026. Oito contas foram de detrator a promotor dentro do
ano, entre elas o Condomínio Itaguassu (a mesma usuária foi de 5 em março para 10 em setembro,
apontando o suporte) e, no myFarm, a conta de Fabricio Krzyzanski (de 2 em janeiro para 10 em abril).
O Condomínio Bigolin também melhorou: reclamação de falta de suporte em abril, só notas 10 em junho. Pela nota
anterior, 32 respondentes que davam nota de detrator ou neutro passaram a promotores. Para ter a foto
inteira: entre os 287 que já tinham nota anterior, 64 subiram e 75 baixaram, então o saldo individual
ainda é levemente negativo; os destaques são reais, mas não compensam sozinhos a queda do myFarm.
No texto, o cliente reconhece o acompanhamento: "a equipe de Sucesso do Cliente está mais próxima,
atenta às nossas necessidades" (Parceria Agrícola S EPP Nova, nota 9)."""

conclusao = """## Resumo
- **NPS acumulado em setembro de 2026:** serviços 59 no arquivo (62 na Track), myFarm 41, AgriManager 2.
- **Contra 2025 no mesmo ponto:** os três abaixo (AgriManager 4 pontos, myFarm 12, serviços 16).
- **myFarm:** a queda começou em setembro de 2025 (de 70 pra 26), teve alívio no 1º trimestre de
  2026 (53) e voltou a 34 de abril a setembro; lentidão e travamento dominam o comentário do detrator.
- **AgriManager:** perto de zero o ano todo, mesmo perfil de detrator de 2025 (falhas, recursos,
  suporte), com 37% menos respostas.
- **Serviços:** maior NPS da operação, sustentado pelo consultor; a crítica é a condução da implantação.
- **Meta (superar 2025 em cada grupo):** nenhum grupo chega lá em nenhum cenário; AgriManager
  precisaria de NPS 38 e myFarm de 67 de outubro a dezembro.
- **Motivo real (um por resposta, comentário primeiro):** AgriManager perde por erros e falhas do
  sistema e por falta de recursos; myFarm por lentidão e quedas, mas só 16 de 71 detratores dizem o
  porquê; serviços ganha pelo consultor e perde pela condução da implantação. A lista de motivos da
  pesquisa muda conforme a nota, então motivo só se compara dentro da mesma classe.
- **Acompanhamento:** 85 de 142 detratores de 2026 tratados pelo CS (os 51 pendentes da Track já
  foram tratados, confirmado pelo Julio em 29/09/2026); em 46 o cliente não atendeu às tentativas de
  contato. Oito contas foram de detrator a promotor dentro de 2026.

A apresentação `NPS 2026.html` lê `dados-nps.json` e `resumo-nps.json` e recalcula tudo pelos
filtros de tela."""
