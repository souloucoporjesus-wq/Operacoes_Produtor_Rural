# Teams · análise diária

Quem abre esta pasta de dentro do sistema: as regras da raiz continuam valendo. Os gatilhos
abaixo dizem o que ler antes de agir.

## O que é
Análise profunda do Microsoft Teams do Julio, todo dia útil às 9h: pendências, o que destravar,
decisões, Leandro, sinais do time, entrelinhas, como ele escreve e decide, cuidados e dicas de
liderança, num painel interativo que abre sozinho no navegador. **Tipo:** interno.
**Confidencial:** fala de pessoas do time. Não publicar, não compartilhar, não citar fora daqui.

## Antes de agir
- Pra saber do projeto: `contexto.md` (como funciona, onde roda) e `andamento.md` (pendências).
- Rodar a análise: a skill `analise_teams` (na raiz, `.claude/skills/analise_teams/`).
- Antes de salvar arquivo: a tabela de destinos em `../../AGENTS.md`. Aprendizado sobre o Julio ou
  sobre o time sai daqui pelo `/atualizar`, com ele, pra `jeito-do-julio.md` ou `equipe/radar.md`.

## Arquivos
- `analises/AAAA-MM-DD.json` · os dados de cada dia (a skill grava)
- `analises/AAAA-MM-DD.html` e `.md` · o painel e a versão em texto de cada dia (o gerador monta)
- `painel.html` · sempre o painel mais recente (não editar na mão)
- `modelo.html` · o modelo do painel; `gerar-painel.js` · o gerador (`node gerar-painel.js [data]`)
- `pessoas.json` · quem é quem (time, área, emails no Teams)
- `rodar-analise.ps1` · o que a tarefa das 9h chama; `instalar-agendamento.bat` · liga a tarefa na máquina
- `.notas/`, `*.log`, `falha.html` · locais da máquina, fora do git

## Regras deste projeto
- Só leitura no Teams. Mensagem sugerida é rascunho no painel, nunca enviada.
- Entrelinhas sempre com a leitura benigna e a confiança. Vida pessoal de ninguém entra.
