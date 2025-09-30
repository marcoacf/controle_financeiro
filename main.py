import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Controle Financeiro",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
st.title("📊 Controle Financeiro Pessoal")

# Mensagem de boas-vindas
st.markdown("""
Bem-vindo ao seu sistema de controle financeiro pessoal!  
Use o menu lateral para navegar entre as funcionalidades:
- Cadastro de lançamentos
- Consolidação por mês
- Avaliação por grupo
- Relatórios detalhados
- Dashboard interativo
""")

# Rodapé opcional
st.markdown("---")
st.markdown("Desenvolvido com ❤️ usando Streamlit e Google Sheets")