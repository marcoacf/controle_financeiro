import os
import json
import streamlit as st
# Verifica se está rodando com variável de ambiente (ex: Streamlit Cloud)
st.success(os.environ["GOOGLE_CREDENTIALS"])
