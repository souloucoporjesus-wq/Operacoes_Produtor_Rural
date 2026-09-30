de: resumo-teams (rotina agendada de nuvem, 16:30)
quando: 2026-09-30 16:30
precisa de ação: sim

A rotina não conseguiu rodar hoje: o conector Microsoft 365 (Teams) apareceu como "precisa de
autenticação" nesta sessão de nuvem, e rotina agendada não tem como fazer o login OAuth sozinha.
Não existe `resumo-teams/2026-09-30.md` — não escrevi um arquivo dizendo "sem atividade" porque
não é verdade: simplesmente não deu pra olhar o Teams hoje.

Isso já tinha sido registrado em `_contexto/ferramentas.md` em 25/09 como desconexão na sessão da
máquina local, depois de um novo login do Claude. O resumo de 28/09 (cobrindo 25→28/09) funcionou
normal, então parece intermitente — mas hoje (30/09) voltou a falhar, e `resumo-teams/2026-09-29.md`
também está faltando, ou seja: ontem (terça) a rotina provavelmente já tinha falhado pelo mesmo motivo.

Próximo passo: reconectar o Microsoft 365 (Outlook/Teams) — via claude.ai, nas configurações de
conectores da conta — pra rotina das 16:30 voltar a funcionar. Se reconectar, vale rodar a rotina
manualmente uma vez pra cobrir a janela perdida de 29 e 30/09.
