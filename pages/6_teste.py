import os
import json
# Verifica se está rodando com variável de ambiente (ex: Streamlit Cloud)
creds_dict = os.environ["GOOGLE_CREDENTIALS"]
print(creds_dict)
