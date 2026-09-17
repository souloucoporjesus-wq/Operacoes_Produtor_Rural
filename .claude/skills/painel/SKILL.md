---
name: painel
description: >
  Regenera o painel de acompanhamento (prazos, o que cobrar de quem, decisões a tomar, projetos
  e decisões recentes) a partir do agora.md, dos andamento.md dos projetos e do decisoes.md, e
  abre a página no navegador. Só lê os arquivos de contexto; nunca escreve neles.
  Use quando o usuário chamar /painel, disser "abre o painel", "atualiza o painel", "o que tá
  atrasado", "o que eu preciso cobrar", "me mostra os prazos", "cadê o painel". Com "publicar"
  (/painel publicar), também publica a página como link privado pra abrir no celular.
---

# /painel · o painel de acompanhamento

O painel é uma **vista** do que já está escrito no sistema, não um lugar novo pra digitar. Fonte:
`_contexto/agora.md` (pendências, onde paramos, quente agora), o `andamento.md` de cada pasta de
projeto (`projetos/`, `clientes/`, `retencao/`, `equipe/`) e `_memoria/decisoes.md`. Quem muda o
conteúdo é o `/atualizar`; esta skill só regenera a página.

## Passo 0 · o que ainda não foi guardado não aparece

Se nesta conversa surgiu pendência, prazo ou decisão que ainda não passou pelo `/atualizar`, dizer
em uma linha antes de gerar: *"o painel mostra o que está escrito; o que a gente conversou hoje só
entra depois do `/atualizar`. Quer rodar ele primeiro?"* Se o usuário topar, rodar o `/atualizar` e
voltar aqui. Se não, seguir.

## Passo 1 · gerar

Da raiz do sistema:

```bash
python painel/gerar.py
```

O script imprime quantas pendências abertas, atrasadas, pra cobrar, projetos e decisões entraram,
e lista as linhas fora do formato (sem dono). Elas entram no painel mesmo assim, como do dono do
sistema e sem prazo, mas a lista serve pra corrigir na próxima passada do `/atualizar`.

Falhou (Python não encontrado, arquivo não achado): dizer o que aconteceu e o que fazer, sem
erro cru. O `painel/index.html` anterior continua válido até a próxima geração.

## Passo 2 · abrir

- Windows: `Invoke-Item painel\index.html`
- Mac: `open painel/index.html`
- Linux: `xdg-open painel/index.html`

## Passo 3 · dizer o que tem lá

Três linhas, direto, com os números que o script imprimiu: atrasadas, vencendo até domingo, pra
cobrar. Se houver linha fora do formato, dizer quantas e de qual arquivo, sem listar tudo.

## `/painel publicar` · link pra abrir no celular

Publicar `painel/index.html` com a ferramenta de artefato (link privado, favicon fixo, sem
`description` que exponha nome de cliente). Antes de publicar pela primeira vez, avisar em uma linha:
o painel carrega nome de gente do time e de cliente; o link é privado, mas existe fora deste
computador. Publicou uma vez, as próximas publicações atualizam o mesmo link (mesmo caminho de
arquivo na sessão, ou a URL guardada em `_contexto/infra.md`). Registrar a URL em `infra.md` pelo
`/atualizar`.

## O formato que o painel lê

Pendência, no `agora.md` e no `andamento.md` de projeto:

```
- [ ] Quem: o que precisa acontecer — até AAAA-MM-DD          (com prazo)
- [ ] Quem: o que precisa acontecer — desde AAAA-MM-DD        (sem prazo; a data é quando entrou)
- [ ] Quem: o que precisa acontecer — toda semana             (recorrente)
- [ ] Quem: decidir se ... — até AAAA-MM-DD                   (começa com "decidir": vai em Decisões a tomar)
```

- `Quem` é nome de gente (`Julio`, `Amanda`, `Lucas e Guilherme`, `Jaqueline e Joyce`). Quem
  não é o dono do sistema aparece em "Pra cobrar". `Agente` é aceito e fica só em Prazos.
- `[tema]` opcional no fim (`[retenção]`, `[churn]`, `[sistema]`).
- Data aceita nos dois jeitos: `AAAA-MM-DD` ou `DD/MM/AAAA`.
- `- [x]` some do painel. Pendência resolvida sai da lista pelo `/atualizar`, com motivo.
- Pendência de projeto mora no `andamento.md` do projeto, não no `agora.md`: o painel junta os dois
  e mostra de qual projeto veio.

Decisão em `_memoria/decisoes.md` segue o formato do próprio arquivo; o painel mostra as 8 mais
recentes, com o "Por quê" recolhido.

## Pergunta no chat

"O que tá atrasado?", "o que eu preciso cobrar da Amanda?", "que decisão tá pendente?": responder
lendo os mesmos arquivos (`agora.md` e os `andamento.md`), sem precisar gerar a página. Gerar só
quando o usuário quiser ver o painel.

## Regras

- Nunca editar `painel/index.html` na mão: é gerado. Mudança de aparência é em `painel/modelo.html`;
  mudança de leitura é em `painel/gerar.py`.
- Nunca escrever em `agora.md`, `andamento.md` ou `decisoes.md` a partir desta skill. Linha fora do
  formato se corrige pelo `/atualizar`.
- Não publicar sem o usuário pedir "publicar".
