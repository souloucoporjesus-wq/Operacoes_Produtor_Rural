# Contexto · Onboarding AGM Web — automação de NF-e

## Por que existe

Roteiro padrão pra habilitar a automação de entrada de notas fiscais (NF-e) dentro do AGM Web:
o que precisa ser pedido ao cliente, quem cadastra e quem cuida do ambiente técnico. Serve como
checklist repetível a cada cliente que entra nessa implantação.

## Quem é quem

- **CS**: obtém os dados junto ao cliente e encaminha pro cadastro e pros agendamentos
- **Gustavo Silva**: cadastro (dados da empresa, usuários, certificado digital)
- **Mateus Pires**: ambiente técnico (ETL de homologação, base de dados de homologação, conta
  Siagri API de homologação)

## Itens necessários (checklist da implantação)

| item | o que se pede | observação | responsável |
|---|---|---|---|
| 1. Dados da empresa | Razão social, CNPJ, Inscrição Estadual, endereço completo | pro cadastro da empresa na plataforma | Gustavo Silva |
| 2. Usuários de acesso | Nome, CPF, e-mail de cada usuário | perfil de cada um (quem consulta, quem aprova/sincroniza) definido em conjunto durante a implantação | Gustavo Silva |
| 3. Certificado digital (e-CNPJ) | Arquivo modelo A1 (.pfx) + senha | usado pra consultar as notas fiscais na SEFAZ | Gustavo Silva |
| 4. Atualização da ETL | Cliente disponibiliza horário pra atualização/configuração do ETL de homologação | etapa técnica antes do início da implantação; se já existe ETL no servidor de produção, precisa de servidor adicional pro ETL de homologação | Mateus Pires |
| 5. Base de dados de homologação | Cliente disponibiliza horário pro ajuste do banco de homologação, a partir de backup da produção | ambiente isolado, sem impacto na produção; Mateus também apoia a configuração do tenant e do usuário pra gerar o token | Mateus Pires |
| 6. Conta Siagri API (homologação) | Sem ação do cliente | conta nova na Siagri API específica pra homologação, criada e administrada pela Aliare | Mateus Pires |

## Fontes

- 28/09/2026 → `Aliare - Onboarding AGM Web 2 1.pdf`: documento "Onboarding — AGM Web" da
  Aliare, checklist completo acima (itens 1 a 6, responsáveis e observações)
