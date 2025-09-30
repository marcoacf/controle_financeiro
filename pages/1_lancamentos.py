import streamlit as st
from google_sheets import salvar_dado
from utils import validar_lancamento
from datetime import date

st.title("📝 Cadastro de Lançamentos")

with st.form("form_lancamento"):
    grupo = st.selectbox("Grupo", [
        "Receita","Alimentos", "Advogado", "Cartão de Crédito", "Moradia",
        "Investimentos", "Tributos", "Reserva", "Outros"
    ])
    natureza = st.selectbox("Natureza", ["Despesa", "Receita"])
    tipo = st.selectbox("Tipo", ["Fixo", "Variável"])
    data_cadastro = st.date_input("Data do Cadastro", value=date.today())
    mes_ref = st.text_input("Mês de Referência (AAAA-MM)")
    categoria = st.text_input("Categoria")
    descricao = st.text_input("Descrição")
    parcela = st.number_input("Número da Parcela", min_value=1, step=1)
    plano = st.number_input("Plano de Parcelamento", min_value=1, step=1)
    valor = st.number_input("Valor", min_value=0.0, step=0.01)
    data_efetivado = st.date_input("Data Efetivado", value=date.today())

    submitted = st.form_submit_button("Salvar Lançamento")

    if submitted:
        novo_dado = [
            grupo, natureza, tipo, str(data_cadastro), mes_ref, categoria,
            descricao, parcela, plano, valor, str(data_efetivado)
        ]

        valido, msg = validar_lancamento({
            "Valor": valor,
            "Mes_Ref": mes_ref,
            "Parcela": parcela
        })

        if valido:
            salvar_dado(novo_dado)
            st.success("✅ Lançamento salvo com sucesso!")
        else:
            st.error(f"❌ Erro: {msg}")