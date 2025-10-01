import os
import json
import streamlit as st
# Verifica se está rodando com variável de ambiente (ex: Streamlit Cloud)
#str_cred = os.environ["GOOGLE_CREDENTIALS"]
#st.success(str_cred)
#str_json = json.loads(str_cred)
#st.success(str_json)

# Lê credenciais do st.secrets
    creds_dict = json.loads(st.secrets["GOOGLE_CREDENTIALS"])

    # Cria objeto de credenciais
    creds = Credentials.from_service_account_info(
        creds_dict,
        scopes=["https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive"]
    )

    client = gspread.authorize(creds)
