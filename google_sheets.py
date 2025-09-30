import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from config import GOOGLE_SHEET_ID, SHEET_NAME, CREDENTIALS_FILE

import os
import json
from oauth2client.service_account import ServiceAccountCredentials

creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)


# Autenticação com Google Sheets
def autenticar_google_sheets():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
    client = gspread.authorize(creds)
    return client

# Carregar dados da aba "lançamentos"
def carregar_dados():
    client = autenticar_google_sheets()
    sheet = client.open_by_key(GOOGLE_SHEET_ID).worksheet(SHEET_NAME)
    data = sheet.get_all_records()
    return pd.DataFrame(data)

# Salvar novo lançamento
def salvar_dado(novo_dado):
    client = autenticar_google_sheets()
    sheet = client.open_by_key(GOOGLE_SHEET_ID).worksheet(SHEET_NAME)

    sheet.append_row(novo_dado)
