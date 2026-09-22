<!-- quem alimenta: o /atualizar acrescenta automação nova, desligada ou mudada. A /faxina confere se
     o que está aqui ainda roda de fato. Nasceu em 2026-09-22, no primeiro registro. -->
# Automações

> Inventário do que roda sozinho ou junto com a sessão, sem precisar de comando explícito. Automação
> que não está aqui não deveria estar rodando.

| rotina | o que faz | onde roda | quando | origem que assina | como saber se quebrou |
|---|---|---|---|---|---|
| Granola → sistema | puxa as reuniões novas do Granola via MCP, salva a transcrição bruta em `_memoria/reunioes/` (ou na pasta do projeto, se identificado), distila o essencial pro `contexto.md` certo, e no fim roda o `/atualizar` sozinha (sem perguntar) pra fechar diário/agora.md/decisões do dia | dentro da sessão do Claude Code, pela skill `granola` | no primeiro comando de cada dia (qualquer mensagem, não precisa ser `/iniciar`) | dono (é a sessão do Julio que dispara) | se o resumo do dia não menciona reunião nenhuma por vários dias, ou se `_memoria/reunioes/` não ganha arquivo novo apesar de ter reunião marcada, conferir se o MCP do Granola ainda está ligado (`_contexto/ferramentas.md`) |
| Triagem de email → "Email Pendentes" | varre a Inbox do Outlook (MCP Microsoft 365) desde a última rotina, descarta ruído (marketing, notificações recorrentes, aceites automáticos), e move pra subpasta `Email Pendentes` (dentro da Inbox) dois tipos de caso: (A) pendência pessoal do Julio sem resposta dele, (B) cobrança que alguém do time dele fez a outra área/parceiro/cliente e que ainda está sem retorno de quem foi cobrado (visibilidade pra ele cobrar em cima); em dúvida, não move — reporta | rotina agendada na nuvem (Claude Code routines), duas instâncias | todo dia às 9:30 e às 16:30 (horário de Brasília) | robô (agente de nuvem, sem sessão do Julio por trás) | se `Email Pendentes` não ganhar nem perder emails por vários dias apesar de inbox ativa, checar as rotinas em https://claude.ai/code/routines (`trig_01MSWJMNSesBW2V84cJzhKv6` manhã, `trig_01DwDWRMhoCxz64MB1DujhjF` tarde) — GitHub não pôde ser anexado à rotina (conta não conectada), então ela roda sem acesso a este repositório, só ao Outlook |
