# Claude Code OS — Kit de Boas-Vindas 🐀

Feito pelo [Ratos de IA](https://ratosdeia.com.br) pra alunos do curso **Claude Code OS**.

---

## Como instalar

Este kit funciona no **Claude Code** e no **Codex** (Windows, Mac ou Linux). Escolha um.

### Opção 1 — Via prompt (mais fácil)

Com o Claude Code **ou** o Codex aberto em qualquer pasta, copie e cole esse prompt:

```
Clona https://github.com/dobralabs/ccos-ratos.git na pasta atual, entra nela, lê e segue o arquivo .claude/skills/setup/SKILL.md
```

O agente faz tudo: clona, entra na pasta e inicia a configuração (que já deixa Claude e Codex prontos).

> Se você está no **Claude Code**, depois de clonar dá pra chamar direto `/setup` — dá no mesmo.

---

### Opção 2 — Via terminal

**1. Clone o repositório**
```bash
git clone https://github.com/dobralabs/ccos-ratos.git
cd ccos-ratos
```

**2. Abra no VS Code**
```bash
code .
```

**3. Abra o terminal integrado** (Ctrl + ` no Windows / Cmd + ` no Mac) e rode o seu agente:
```bash
claude      # ou: codex
```

**4. Chame o setup**
- No Claude Code: `/setup`
- No Codex (primeira vez): peça `leia e siga o arquivo .claude/skills/setup/SKILL.md`

---

O agente vai te fazer algumas perguntas e configurar o sistema pro seu negócio. Em 5 minutos você tem tudo pronto, funcionando nos dois.

---

## O que vem no kit

**Skills prontas pra usar:**
- `/setup` — configura o sistema pro seu negócio (comece por aqui)
- `/iniciar` — abre a sessão: puxa o GitHub, carrega o contexto, anuncia recados e diz onde você parou
- `/atualizar` — fecha a sessão: escreve o diário do dia, o "onde paramos", as decisões e o contexto, e diz o que escreveu onde
- `/syncar` — manda o trabalho pro GitHub e diz o que subiu
- `/novo-projeto` — cria pasta de projeto ou cliente com contexto próprio
- `/mapear` — entrevista você sobre o dia a dia e cria skills personalizadas
- `/carrossel` `/proposta-comercial` `/slide` `/publicar-site` `/analisar-dados` `/roteiro-post` `/email-profissional` — modelos prontos que o `/mapear` instala com a sua identidade

**A casa, depois do `/setup`:**

```
seu-negocio/
├── AGENTS.md        as regras, o boot, o mapa e a tabela de destinos (o cérebro, com teto de 180 linhas)
├── CLAUDE.md        uma linha: @AGENTS.md
├── _contexto/       o que o sistema sabe do negócio: empresa, preferências, foco, ferramentas, infra, marca/
├── _memoria/        o que aconteceu e por quê: diario/ (um arquivo por dia), decisoes.md, recados/
├── sistema/         o motor do kit: scripts e modelos. Você não precisa abrir
├── .claude/         as skills
└── clientes/ propostas/ conteudo/ ...   as pastas de trabalho, conforme o seu perfil
```

Três comandos que você vai confundir no começo: `/iniciar` lê, `/atualizar` escreve, `/syncar` manda pro GitHub.

**Se você já tinha a versão anterior do kit** (a que tinha `dados/` e `marca/` na raiz): não precisa
mudar nada se o seu sistema te atende. Quando quiser atualizar, existe um arquivo de atualização que
você cola no agente e ele faz com você, no máximo três mudanças por vez.

---

## Ficou travado?

Assiste a **Aula 1.3** do curso (instalação do Claude Code).

Dúvidas: [ratosdeia.com.br](https://ratosdeia.com.br)
