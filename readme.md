# Controle Financeiro com Streamlit e Google Sheets

## 💡 Conceito

Este projeto tem como objetivo fornecer uma interface amigável para controle financeiro pessoal, com armazenamento dos dados diretamente em uma planilha do Google Sheets. A aplicação permite:

- Cadastro de lançamentos (receitas e despesas)
- Consolidação por mês de referência
- Avaliação por grupo de gastos
- Relatórios detalhados com filtros
- Dashboard interativo com gráficos

## 📦 Estrutura do Projeto
```bash
controle_financeiro/
│
├── .venv/                      # Ambiente virtual
├── requirements.txt            # Dependências
├── config.py                   # Configurações (como credenciais do Google Sheets)
├── google_sheets.py            # Funções para ler/escrever no Google Sheets
├── utils.py                    # Funções auxiliares
├── main.py                     # Interface principal com Streamlit
├── pages/
│   ├── 1_crud.py               # Tela de cadastro e edição
│   ├── 2_consolidacao.py       # Consolidação por mês
│   ├── 3_grupo.py              # Avaliação por grupo
│   ├── 4_relatorio.py          # Relatórios detalhados
│   ├── 5_dashboard.py          # Visualizações gráficas

```

## ⚙️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/controle_financeiro.git
cd controle_financeiro
```
2. Crie e ative o ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\\Scripts\\activate   # Windows
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```
## 🔐 Configuração do Google Sheets

1. Crie um projeto no Google Cloud Console.
2. Ative a API do Google Sheets.
3. Crie uma Service Account e baixe o arquivo service_account.json.
4. Compartilhe sua planilha com o e-mail da service account.
5. Edite o arquivo config.py com:
```bash
GOOGLE_SHEET_ID: ID da sua planilha
SHEET_NAME: nome da aba (ex: "lançamentos")
CREDENTIALS_FILE: caminho para o JSON de credenciais
```
## 🚀 Executando o Projeto
```bash
streamlit run main.py
```
Use o menu lateral para navegar entre as funcionalidades.

## 🧠 Funcionalidades

* CRUD: Cadastro de lançamentos com validação.
* Consolidação: Soma de receitas e despesas por mês.
* Grupo: Avaliação por grupo de gastos.
* Relatório: Filtros por grupo e mês.
* Dashboard: Gráficos interativos com Plotly.

## ✨ Melhorias Futuras

Validação automática mais robusta
Alertas de orçamento por grupo
Exportação de relatórios em PDF/Excel
Autenticação de usuários
Publicação via Streamlit Cloud