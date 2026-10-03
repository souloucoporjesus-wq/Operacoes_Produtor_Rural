// gerar-painel.js · monta o painel da análise do Teams a partir do JSON do dia.
// Uso (da raiz do repositório ou de qualquer lugar): node projetos/Teams/gerar-painel.js [AAAA-MM-DD]
// Sem data, usa o JSON mais recente de analises/.
// Gera: analises/AAAA-MM-DD.html (o painel do dia), analises/AAAA-MM-DD.md (texto) e painel.html (o mais recente).
// O HTML leva os dados embutidos: abre direto do arquivo no navegador, sem servidor e sem internet.

"use strict";
const fs = require("fs");
const path = require("path");

const PASTA = __dirname;
const ANALISES = path.join(PASTA, "analises");
const MODELO = path.join(PASTA, "modelo.html");

function falhar(msg) { console.error("ERRO: " + msg); process.exit(1); }

const datas = fs.existsSync(ANALISES)
  ? fs.readdirSync(ANALISES).filter((f) => /^\d{4}-\d{2}-\d{2}\.json$/.test(f)).map((f) => f.slice(0, 10)).sort()
  : [];
if (!datas.length) falhar("nenhum analises/AAAA-MM-DD.json encontrado");
const data = process.argv[2] || datas[datas.length - 1];
if (!/^\d{4}-\d{2}-\d{2}$/.test(data)) falhar("data inválida: " + data + " (use AAAA-MM-DD)");

function lerJson(d) {
  const arq = path.join(ANALISES, d + ".json");
  if (!fs.existsSync(arq)) falhar("não achei " + arq);
  let txt = fs.readFileSync(arq, "utf8");
  if (txt.charCodeAt(0) === 0xfeff) txt = txt.slice(1);
  try { return JSON.parse(txt); } catch (e) { falhar(d + ".json não é um JSON válido: " + e.message); }
}

const dados = lerJson(data);
if (dados.data !== data) falhar(`o campo "data" (${dados.data}) não bate com o nome do arquivo (${data})`);
const arr = (x) => (Array.isArray(x) ? x : []);

// conferência mínima das chaves que o painel usa
const obrigatorias = ["data", "gerado_em", "janela", "fontes", "termometro", "resumo", "pendencias"];
const faltando = obrigatorias.filter((k) => !(k in dados));
if (faltando.length) falhar("faltam chaves no JSON: " + faltando.join(", "));
const validos = { prioridade: ["critica", "alta", "media", "baixa"], tipo: ["voce_deve", "time_deve", "outra_area_deve"] };
arr(dados.pendencias).forEach((p, i) => {
  if (!validos.prioridade.includes(p.prioridade)) console.warn(`aviso: pendencias[${i}] prioridade "${p.prioridade}" fora do padrão`);
  if (!validos.tipo.includes(p.tipo)) console.warn(`aviso: pendencias[${i}] tipo "${p.tipo}" fora do padrão`);
});

// histórico: um resumo de cada análise guardada (até a data pedida)
const historico = datas.filter((d) => d <= data).map((d) => {
  let j;
  try { j = d === data ? dados : JSON.parse(fs.readFileSync(path.join(ANALISES, d + ".json"), "utf8").replace(/^﻿/, "")); }
  catch (e) { return { data: d }; }
  const abertas = arr(j.pendencias).filter((p) => p.status !== "resolvida");
  return {
    data: d,
    nivel: (j.termometro || {}).nivel || "",
    criticas: abertas.filter((p) => p.prioridade === "critica").length,
    abertas: abertas.length,
    alertas: arr(j.time).filter((t) => t.gravidade === "alerta").length,
    mensagens: (j.fontes || {}).mensagens,
  };
});

const modelo = fs.readFileSync(MODELO, "utf8");
const seguro = (obj) => JSON.stringify(obj).split("<").join(String.fromCharCode(92) + "u003c");
function montar(base) {
  return modelo
    .replace("/*__DADOS__*/null", () => seguro(dados))
    .replace("/*__HISTORICO__*/[]", () => seguro(historico))
    .replace("/*__BASE__*/", base);
}

fs.writeFileSync(path.join(ANALISES, data + ".html"), montar(""), "utf8");
const ehMaisRecente = data === datas[datas.length - 1];
if (ehMaisRecente) fs.writeFileSync(path.join(PASTA, "painel.html"), montar("analises/"), "utf8");

// versão em texto, pra ler no GitHub pelo celular
const conf = { certo: "[Certo]", provavel: "[Provável]", suposicao: "[Suposição]" };
const c = (x) => (x ? " " + (conf[x] || "[" + x + "]") : "");
const L = [];
const f = dados.fontes || {};
L.push(`# Análise do Teams · ${data}`, "");
L.push(`Janela ${(dados.janela || {}).inicio || ""} a ${(dados.janela || {}).fim || ""} · ${f.mensagens ?? "?"} mensagens em ${f.conversas ?? "?"} conversas · ${f.do_julio ?? "?"} do Julio`, "");
L.push("> Confidencial: fala de pessoas do time. Não encaminhar.", "");
if ((dados.termometro || {}).frase) L.push(`**Termômetro (${dados.termometro.nivel}):** ${dados.termometro.frase}`, "");
arr(dados.resumo).forEach((r) => L.push(`- ${r}`));
if (arr(dados.foco).length) { L.push("", "## Foco de hoje", ""); arr(dados.foco).forEach((x, i) => L.push(`${i + 1}. **${x.titulo}** ${x.porque || ""} Como: ${x.acao || ""}`)); }
const ordem = { critica: 0, alta: 1, media: 2, baixa: 3 };
const pend = arr(dados.pendencias).slice().sort((a, b) => (ordem[a.prioridade] ?? 9) - (ordem[b.prioridade] ?? 9));
if (pend.length) {
  L.push("", "## Pendências", "");
  pend.forEach((p) => L.push(`- [${p.prioridade}${p.status ? ", " + p.status : ""}${p.chefe ? ", Leandro" : ""}] **${p.titulo}** (${p.quem || "?"}${p.para ? " → " + p.para : ""}, desde ${p.desde || "?"}). ${p.detalhe || ""}${c(p.confianca)}`));
}
if (arr(dados.destravar).length) { L.push("", "## Destravar", ""); arr(dados.destravar).forEach((d) => L.push(`- **${d.titulo}**: travado em ${d.travado_em || "?"}; quem destrava: ${d.quem_destrava || "?"}. ${d.como || ""}`)); }
if (arr(dados.decisoes_a_tomar).length) { L.push("", "## Decisões esperando o Julio", ""); arr(dados.decisoes_a_tomar).forEach((d) => L.push(`- **${d.titulo}**: ${d.recomendacao || ""}`)); }
if (arr(dados.decisoes).length) { L.push("", "## Decisões tomadas", ""); arr(dados.decisoes).forEach((d) => L.push(`- ${d.titulo} (${d.quem || "?"}, ${d.quando || "?"})${d.registrada ? "" : " · sem registro"}`)); }
const ch = dados.chefe || {};
if (ch.leitura || arr(ch.itens).length) { L.push("", "## Leandro", ""); if (ch.leitura) L.push(ch.leitura, ""); arr(ch.itens).forEach((i) => L.push(`- **${i.titulo}** ${i.detalhe || ""}${c(i.confianca)}`)); }
if (arr(dados.time).length) { L.push("", "## Time", ""); arr(dados.time).forEach((t) => L.push(`- **${t.pessoa}** (${t.gravidade}): ${t.sinal} O que fazer: ${t.sugestao || "-"}${c(t.confianca)}`)); }
if (arr(dados.entrelinhas).length) { L.push("", "## Entrelinhas", ""); arr(dados.entrelinhas).forEach((e) => L.push(`- **${e.pessoa}**: "${e.citacao}" Leitura: ${e.leitura} Outro lado: ${e.leitura_benigna} Como agir: ${e.como_agir || "-"}${c(e.confianca)}`)); }
if (arr(dados.cuidados).length) { L.push("", "## Cuidados", ""); arr(dados.cuidados).forEach((x) => L.push(`- [${x.gravidade}] **${x.titulo}** ${x.detalhe || ""}`)); }
if (arr(dados.dicas).length) { L.push("", "## Dicas de liderança", ""); arr(dados.dicas).forEach((x) => L.push(`- **${x.titulo}** ${x.texto || ""} Pratique hoje: ${x.pratica || "-"}`)); }
if (arr(dados.mensagens).length) { L.push("", "## Mensagens prontas", ""); arr(dados.mensagens).forEach((m) => L.push(`- Para ${m.para} (${m.assunto}): ${m.texto}`)); }
fs.writeFileSync(path.join(ANALISES, data + ".md"), L.join("\n") + "\n", "utf8");

console.log(`ok: analises/${data}.html, analises/${data}.md${ehMaisRecente ? ", painel.html" : ""}`);
