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
| Outlook | email (`@aliare.co`) | sem conector no catálogo | não ligada | 2026-09-16 |
| Teams | agenda e reunião | sem conector no catálogo | não ligada | 2026-09-16 |
| Engenho (ferramenta própria) | controle de tarefas e prazos (Vercel + Supabase) | Supabase tem conector (MCP) no catálogo, combinado deixar pra depois | não ligada | 2026-09-16 |
| Disparo em massa (ferramenta interna) | mensagem em massa pra clientes | só você, na mão | não ligada | 2026-09-16 |
| Evolution API (em avaliação) | centralizar WhatsApp dos consultores, hoje em celulares individuais | sem conector no catálogo, projeto ainda não decidido | não ligada | 2026-09-16 |
| Python 3.12 + pandas/openpyxl/matplotlib/Jupyter | análise de dados (planilhas, reports), notebooks | CLI, instalado local nesta máquina (pc-aliare); na sessão de 16/09 à tarde `python` não respondia no shell do agente (só o atalho da loja), conferir PATH | ligada | 2026-09-17 |
| Excel (automação COM) | ler e gerar planilhas .xlsx quando o Python não responde | PowerShell + COM, Excel instalado nesta máquina | ligada | 2026-09-17 |
| Granola | transcrição de reunião (grava e transcreve automaticamente) | MCP | ligada | 2026-09-22 |

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
