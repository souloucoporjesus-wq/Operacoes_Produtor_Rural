<!-- quem alimenta: o /setup semeia na entrevista; o /atualizar acrescenta ferramenta nova, acesso novo ou "não alcanço"; a /faxina confere e pergunta. Lido antes de dizer "não consigo" e ao criar skill. -->
# Ferramentas

> O que o negócio usa e como o agente alcança cada coisa. **"não ligada" é resposta válida:** é assim
> que o agente sabe que aquilo existe e dá pra ligar, em vez de achar que é impossível.
> Chave nunca fica aqui. Chave mora no `.env` (fora do git) ou no gerenciador de senha; aqui vai só o
> nome da variável. O cardápio do que dá pra ligar está em `sistema/templates/ferramentas/catalogo.md`.

| ferramenta | pra quê | como o agente alcança | estado | última checagem |
|---|---|---|---|---|
| ClickUp | trilha de implantação de ERP, tarefas do time | MCP | ligada | 2026-09-16 |
| Hubspot | ficha do cliente (CRM), WhatsApp de projetos/CS; mal implantado, sem automações | sem conector no catálogo | não ligada | 2026-09-16 |
| Movidesk | atendimento/suporte | sem conector no catálogo | não ligada | 2026-09-16 |
| Track Sales | vendas | sem conector no catálogo | não ligada | 2026-09-16 |
| Qulture.Rocks | OKRs do time | sem conector no catálogo | não ligada | 2026-09-16 |
| Outlook | email (`@aliare.co`) e agenda | MCP Microsoft 365 (na sessão e nas rotinas de nuvem); pode ler, mover entre pastas e criar pasta; em 25/09 não apareceu na sessão desta máquina depois do novo login do Claude, reconectar | ligada (desconectada na sessão local) | 2026-09-25 |
| Teams | conversas e reuniões | MCP Microsoft 365 (`chat_message_search`, na sessão e nas rotinas de nuvem); em 25/09 não apareceu na sessão desta máquina depois do novo login, reconectar | ligada (desconectada na sessão local) | 2026-09-25 |
| GitHub | cópia do sistema (`souloucoporjesus-wq/Operacoes_Produtor_Rural`) e caminho das rotinas de nuvem pro repositório | nesta máquina, o git do GitHub Desktop (fora do PATH); conta conectada ao claude.ai e app do Claude instalado no repositório (24/09): as rotinas de nuvem leem e gravam | ligada | 2026-09-24 |
| Rotinas de nuvem do Claude Code | rodar tarefa agendada com o computador desligado (triagem de email, resumo do Teams, briefing) | ferramenta de rotinas da sessão; lista em https://claude.ai/code/routines; inventário em `_contexto/automacoes.md` | ligada | 2026-09-23 |
| Engenho (ferramenta própria) | controle de tarefas e prazos (Vercel + Supabase) | Supabase tem conector (MCP) no catálogo, combinado deixar pra depois | não ligada | 2026-09-16 |
| Disparo em massa (ferramenta interna) | mensagem em massa pra clientes | só você, na mão | não ligada | 2026-09-16 |
| Evolution API (em avaliação) | centralizar WhatsApp dos consultores, hoje em celulares individuais | sem conector no catálogo, projeto ainda não decidido | não ligada | 2026-09-16 |
| Python 3.12 + pandas/openpyxl/matplotlib/Jupyter | análise de dados (planilhas, reports), notebooks | CLI, instalado local nesta máquina (pc-aliare); na sessão de 16/09 à tarde e de novo em 25/09 `python` não respondia no shell do agente (só o atalho da loja), conferir PATH | ligada (não responde no shell do agente) | 2026-09-25 |
| Node.js 24 | ler .xlsx (unzip + script) e gerar páginas HTML quando o Python não responde | CLI no PATH desta máquina (`node`), usado na análise de cobrança de 25/09 | ligada | 2026-09-25 |
| Microsoft Edge (sem interface) | capturar tela de página HTML pra conferir layout no computador e no celular | `msedge.exe --headless=new --screenshot`, em `C:\Program Files (x86)\Microsoft\Edge\Application\` | ligada | 2026-09-25 |
| Excel (automação COM) | ler e gerar planilhas .xlsx quando o Python não responde | PowerShell + COM, Excel instalado nesta máquina | ligada | 2026-09-17 |
| Granola | transcrição de reunião (grava e transcreve automaticamente) | MCP; em 25/09 não apareceu na sessão desta máquina depois do novo login do Claude, reconectar | ligada (desconectada na sessão local) | 2026-09-25 |

## Os sete assuntos que todo negócio tem

- **Mensagem com cliente:** ferramenta interna de disparo em massa; equipe de projetos e CS usa
  WhatsApp dentro do Hubspot (mantém histórico); consultores usam celular pessoal — em avaliação
  trazer a Evolution API pra central própria e reduzir horas de implantação
- **Tarefa e prazo:** ClickUp (trilha de implantação) e o Engenho, ferramenta própria em
  Vercel + Supabase
- **Email:** Outlook, domínio próprio `@aliare.co`
- **Agenda:** Teams
- **Dinheiro entrando e saindo:** nenhuma ferramenta do lado do CS — a cobrança é da equipe de
  cobrança, mas o CS acaba puxando porque ela não dá conta
- **Ficha do cliente:** Hubspot (mal implantado, sem automação nenhuma)
- **Reunião:** Teams pra agenda; Granola grava e transcreve

Nenhuma integração entre os sistemas hoje.
