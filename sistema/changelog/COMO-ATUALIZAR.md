# Atualizar o seu RatosOS

**Pra você (humano):** baixe o kit novo na plataforma, descompacte **ao lado** da pasta do seu
sistema (nunca por cima), abra o seu agente (Claude Code ou Codex) **dentro da pasta do seu
sistema** e diga:

> leia `../<pasta-do-kit-novo>/sistema/changelog/COMO-ATUALIZAR.md` e faz o que está escrito

Se o seu sistema te atende como está, **não precisa atualizar.** Nada abaixo é obrigatório.

---

<!-- Daqui pra baixo é instrução pro agente. -->

## Como você (agente) se comporta aqui

**A casa do usuário manda.** O kit novo é sugestão; a instalação dele é a verdade. Você compara,
propõe, nunca sobrescreve, e adapta tudo aos nomes que ele usa (se a memória dele se chama
`cerebro/`, é `cerebro/` no papel também).

1. **Primeira frase da conversa:** "Se o seu sistema te atende como está, não precisa atualizar.
   Quer ver o que a versão nova traz, e escolher o que entra?"
2. **Cópia de segurança antes de qualquer mudança.** Se a pasta tem git: `git add -A && git commit
   -m "antes de atualizar pra <versão>"` (aqui o `add -A` é de propósito: é a foto inteira). Sem
   git: `cp -R` da pasta inteira pra `<pasta>-antes-da-<versão>-<data>`, conferindo a contagem de
   arquivos dos dois lados. Dizer onde a cópia está.
3. **No máximo 3 mudanças por rodada.** Terminou as três, pergunta se segue. "Faz tudo, decide tu"
   vale pra aplicar; não vale pra apagar nada nem pra mexer em arquivo que ele escreveu.
4. **Antes/depois na tela** de todo arquivo que muda, antes de mudar.
5. **Nunca apagar.** Arquivo absorvido por outro só sai depois de conferir que o conteúdo chegou
   inteiro; na dúvida, renomear pra `<nome>-antigo.md` e avisar.
6. **Fale como gente.** Sem "merge", "rebase", "diff", "commit" na tela: "cópia de segurança",
   "salvar", "juntar os dois textos".
7. **Escreva na voz dele:** ler o `preferencias.md` dele antes de escrever qualquer texto novo.

## O procedimento

### 1. Descobrir de onde ele parte

```bash
cat .ratosos 2>/dev/null || echo "sem .ratosos"
ls sistema/changelog/ 2>/dev/null || echo "sem changelog"
ls ../<kit-novo>/sistema/changelog/
```

- Sem `.ratosos` e sem `sistema/changelog/`: é a **1.0**. Tudo do `2.0.md` (e dos seguintes)
  está por aplicar.
- Com changelog: o que existe no kit novo e **falta** na instalação é o que falta aplicar, em
  ordem de versão. Funciona pra quem pulou versões.
- Dentro de uma versão, o que já foi aplicado ou recusado está registrado no `decisoes.md` dele
  (entradas com `[atualizacao]`). Ler antes de propor: não oferecer de novo o que ele recusou,
  a não ser que ele peça.

### 2. Reconhecer a casa, sem presumir nome

`ls -a`, `find . -maxdepth 2 -type d`, `ls .claude/skills/`, `wc -l AGENTS.md` (ou `CLAUDE.md`,
se a instalação for anterior ao `AGENTS.md`). Descobrir qual pasta cumpre qual papel **pelo
conteúdo**: memória do negócio (tem `empresa.md`), marca (tem `design-guide.md`), scripts e
modelos, material cru. Anotar o mapa dele; toda mudança abaixo é escrita com os nomes dele.

### 3. Ler o(s) arquivo(s) de versão que faltam

Cada mudança tem cinco campos: **o que é · por quê · te afeta se (o check) · como aplicar · como
testar**. Rodar o check de cada uma na instalação dele. As que o check diz "não te afeta" somem
da lista. As que sobram, apresentar **rankeadas como estão no arquivo** (valor primeiro), em
linguagem de gente, e propor as 3 primeiras.

### 4. Aplicar, uma por vez

Pra cada mudança aceita: antes/depois → aplicar → rodar o "como testar" → uma linha no
`decisoes.md` dele: `- **AAAA-MM-DD** (agente) [atualizacao]: aplicada "<nome da mudança>" da
versão X. Por quê: <motivo dele, se disse>`. Recusada: mesma linha com "recusada".

### 5. Fechar a rodada

Quando todas as mudanças da versão estiverem aplicadas ou recusadas: escrever a versão no
`.ratosos` (uma linha) e copiar a pasta `sistema/changelog/` do kit novo pra dentro da instalação
(é assim que a próxima versão sabe de onde ele parte). Se sobrou mudança pra próxima rodada,
`.ratosos` fica como estava e a rodada seguinte continua daqui.

Se a instalação tem git e o `/syncar` existe: oferecer sincronizar. Depois, dizer em três linhas o
que mudou e o que ficou de fora.
