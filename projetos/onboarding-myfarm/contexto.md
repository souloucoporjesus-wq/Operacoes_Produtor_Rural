# Contexto · Onboarding myFarm

## Por que existe

Cliente myFarm começa a usar, abandona e não volta; a base está perdendo cliente pra concorrência.
O projeto muda a entrada do cliente pra ele enxergar valor na primeira implantação, com três
frentes que se cruzam: trilha de vídeos, plataforma guiada (Evoluto) e carga inicial de dados.
Referência de mercado citada: a Sanki promete cliente com sistema rodando em até 24 horas após a
contratação, lendo o XML com IA e importando cadastros e tributação.

## Quem é quem

- **Julio**: coordena, faz a ponte com Leandro, Wellington e Pâmela
- **Guilherme Job** (consultor de implantação myFarm): dono da gravação dos vídeos
- **Lucas Nogueira** (consultor de implantação myFarm): dono da importação de XML e da
  estruturação das planilhas
- **Pâmela**: trata os XMLs com IA (extração de fornecedores, produtos, tributação) e resolve a
  importação pro myFarm
- **Wellington**: coordenador do Plantar Educação; instala o OBS na máquina do Guilherme, orienta a
  gravação e sabe até onde os vídeos anteriores foram
- **Luiz Carlos**: dono anterior do projeto de vídeos; desligado em 17/09/2026 por corte de
  custos. Os vídeos que ele gravou serão reaproveitados; o Plantar Educação sabe até onde foram
- **Leandro Xavier** (diretor): bateu o martelo da Evoluto em 17/09/2026
- **Arley, Edson, Vera**: possíveis fontes de clientes do BPO pro piloto de XML

## Frentes

### 1. Trilha de vídeos (dono: Guilherme)

- Trilha de conhecimento do myFarm dentro do Plantar Educação; os mesmos vídeos entram na Evoluto
- Reaproveitar o que o Luiz gravou; o Plantar Educação diz até onde foi
- Prazo: tudo pronto até **15/10/2026**
- Padrão de gravação (o mesmo feedback dado ao Luiz): descer nos campos que têm impacto e explicar
  o impacto (ex.: certidão negativa de débito, unidade de medida); não gastar tempo no óbvio (data,
  talhão, horímetro). Entre curto demais e explicado demais, explicado demais. Rotina longa
  (operações) corta em parte 1, 2, 3, com texto de apoio na trilha. Roteiro antes de gravar, duas
  telas. Julio valida o material
- Guilherme disse ter uns 3 vídeos prontos pra começar

### 2. Evoluto (plataforma guiada de implantação e projetos)

- Decisão fechada com o Leandro em 17/09/2026
- O cliente recebe email de boas-vindas com login e senha e percorre um caminho: enviar certificado
  digital, dados da fazenda (formulários dentro da plataforma), vídeo de como acessar o myFarm,
  vídeo de como chamar o suporte
- A trilha inteira ainda precisa ser desenhada

### 3. Carga inicial de dados por XML (dono: Lucas, com Guilherme nos clientes)

- Etapa 1: XMLs de compra e venda do cliente (2026 e, se possível, de agosto/2025 pra cá, um ano
  fechado) → Pâmela extrai fornecedores, clientes, produtos e tributação com IA
- Cadastros (fornecedores, clientes, produtos) podem ser importados direto
- **Tributação não sobe direto.** Vai pra planilha no layout de importação do myFarm, o cliente (ou a
  contabilidade dele) valida, e só então importa. Motivo levantado pelo Guilherme: legislação mudou
  no período, muito cliente tributava errado e só descobriu quando a implantação provocou a
  contabilidade; importar às cegas compromete a percepção de qualidade
- Etapa 2 (depois): contas a pagar e a receber. Mais trabalhoso (classificação, relacionamento de
  tabelas). Respeitar a arquitetura do myFarm: sem conta contábil, só as categorias vigentes de
  receita e despesa (contas analíticas)
- Piloto: 2 ou 3 clientes em implantação com bom relacionamento bastam pra validar; depois vira
  padrão pra todo cliente que entra
- Fluxo: consultor pede o XML ao cliente (WhatsApp, pasta zipada ou pasta no Google Drive) →
  Guilherme repassa pro Lucas → Lucas avisa o Julio → Julio conecta a Pâmela
- Primeiro marco: XMLs de clientes em mãos até **22/09/2026** (terça)

## Em aberto

- Se a demanda de vídeos gera produtividade acima do normal pros consultores: Julio valida com o
  Leandro. Não decidido
- Evoluto: ainda sem detalhe de contratação, acesso ou prazo de configuração

## Fontes

- Reunião 17/09/2026 com Guilherme Job e Lucas Nogueira →
  `reunioes/2026-09-17-guilherme-lucas.md`: tudo acima
