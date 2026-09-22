<!-- quem alimenta: o /atualizar acrescenta automação nova, desligada ou mudada. A /faxina confere se
     o que está aqui ainda roda de fato. Nasceu em 2026-09-22, no primeiro registro. -->
# Automações

> Inventário do que roda sozinho ou junto com a sessão, sem precisar de comando explícito. Automação
> que não está aqui não deveria estar rodando.

| rotina | o que faz | onde roda | quando | origem que assina | como saber se quebrou |
|---|---|---|---|---|---|
| Granola → sistema | puxa as reuniões novas do Granola via MCP, salva a transcrição bruta em `_memoria/reunioes/` (ou na pasta do projeto, se identificado), distila o essencial pro `contexto.md` certo, e no fim roda o `/atualizar` sozinha (sem perguntar) pra fechar diário/agora.md/decisões do dia | dentro da sessão do Claude Code, pela skill `granola` | no primeiro comando de cada dia (qualquer mensagem, não precisa ser `/iniciar`) | dono (é a sessão do Julio que dispara) | se o resumo do dia não menciona reunião nenhuma por vários dias, ou se `_memoria/reunioes/` não ganha arquivo novo apesar de ter reunião marcada, conferir se o MCP do Granola ainda está ligado (`_contexto/ferramentas.md`) |
