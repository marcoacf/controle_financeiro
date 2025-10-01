import os

# ID da planilha e nome da aba
GOOGLE_SHEET_ID = "1mmRw_6zvRZ9mkHLv2JcsrO74K6_s6Jpwk5n1Ly0ZpfQ"
SHEET_NAME = "lancamentos"

#  Nome do arquivo local (usado apenas se não estiver no Streamlit Cloud)
CREDENTIALS_FILE = "service_account.json"

# Verifica se está rodando no Streamlit Cloud
USANDO_SECRETS = "GOOGLE_CREDENTIALS" in os.environ

