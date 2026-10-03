# Teams · contexto

## O que foi pedido (2026-10-03)

O Julio pediu uma análise do Teams dele todo dia às 9h, de segunda a sexta: itens que ficaram em
aberto, decisões, o modo dele de decidir e de escrever, o que ele precisa melhorar, pontos
pendentes, o que precisa da atenção dele, o que precisa ser destravado, cuidados, leitura de
"maldade" na fala das pessoas e dicas pra ser um líder melhor. Sempre que rodar, abrir um painel
interativo (HTML, CSS e JavaScript) com tudo e uma seção de dicas. Tem que rodar nesta máquina e na
máquina do serviço. Tudo que for captado do Teams fica nesta pasta.

## Como funciona

- **Quem roda:** a tarefa agendada do Windows "Analise do Teams 9h", seg a sex às 9:00, em cada
  máquina que rodou o `instalar-agendamento.bat`. Se o computador estiver desligado às 9h, roda
  quando ligar. Chama `rodar-analise.ps1`, que chama o Claude Code sem janela com a skill
  `analise_teams` e só as ferramentas de leitura do Microsoft 365 liberadas (nenhuma de envio).
- **Duas máquinas:** a primeira que começa grava `analises/AAAA-MM-DD.rodando-<origem>` e envia pro
  GitHub; a outra vê, espera e só abre o painel quando a análise chega. Empate (as duas ligadas às
  9h em ponto): roda a de nome de origem menor.
- **Janela:** desde a análise anterior até agora (segunda cobre o fim de semana).
- **Saída:** `analises/AAAA-MM-DD.json` + `.html` + `.md` e `painel.html`, enviados pro GitHub só
  esses arquivos. Falhou: recado em `_memoria/recados/` e uma página `falha.html` abre dizendo o motivo.
- **Pessoas:** `pessoas.json` (lista passada pelo Julio em 2026-10-03). Emails no Teams diferem da
  lista em dois casos: Guilherme Job e Andrezza Perroni aparecem com `@aliare.co`.

## Diferença pro briefing

O `briefing` (rotina de nuvem das 9:30) cruza email, Teams, Granola e agenda num resumo executivo.
Esta análise é só do Teams, mais funda e mais pessoal: leitura de pessoas, entrelinhas, escrita e
decisão do Julio, mentoria de liderança.

## Requisitos de cada máquina

Claude Code (extensão do VS Code ou linha de comando) com login feito e o conector Microsoft 365
ligado; Node.js; git (o do Git for Windows ou o do GitHub Desktop) com login no GitHub.
