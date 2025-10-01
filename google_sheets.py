import gspread
import pandas as pd
import os
import json
import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account as sa
from config import GOOGLE_SHEET_ID, SHEET_NAME, CREDENTIALS_FILE

def autenticar_google_sheets():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    # Verifica se está rodando com variável de ambiente (ex: Streamlit Cloud)
    # Lê credenciais do st.secrets
    creds_dict = json.loads(st.secrets["GOOGLE_CREDENTIALS"])
    # creds = ServiceAccountCredentials.from_json_keyfile_name(json.loads(os.environ["GOOGLE_CREDENTIALS"]), scope)
    creds = sa.Credentials.from_service_account_info(creds_dict, scope)
    client = gspread.authorize(creds)
    return client

def carregar_dados():
    client = autenticar_google_sheets()
    sheet = client.open_by_key(GOOGLE_SHEET_ID).worksheet(SHEET_NAME)
    data = sheet.get_all_records()
    return pd.DataFrame(data)

def salvar_dado(novo_dado):
    client = autenticar_google_sheets()
    sheet = client.open_by_key(GOOGLE_SHEET_ID).worksheet(SHEET_NAME)
    sheet.append_row(novo_dado)





