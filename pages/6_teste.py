import os
import json
import streamlit as st
# Verifica se está rodando com variável de ambiente (ex: Streamlit Cloud)
str_cred = os.environ["GOOGLE_CREDENTIALS"]
st.success(str_cred)
str_json = json.loads(str_cred)
st.success(str_json)
