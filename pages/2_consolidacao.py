import streamlit as st
import pandas as pd
from google_sheets import carregar_dados

st.title("📅 Consolidação por Mês")

# Carregar dados da planilha
df = carregar_dados()

# Garantir que o campo Mes_Ref esteja como string
df['Mes_Ref'] = df['Mes_Ref'].astype(str)

# Filtro opcional por mês
meses_disponiveis = sorted(df['Mes_Ref'].unique())
meses_selecionados = st.multiselect("Filtrar por Mês de Referência", meses_disponiveis)

if meses_selecionados:
    df = df[df['Mes_Ref'].isin(meses_selecionados)]

# Agrupar por mês e natureza (Receita/Despesa)
consolidado = df.groupby(['Mes_Ref', 'Natureza'])['Valor'].sum().reset_index()

# Exibir tabela consolidada
st.subheader("Resumo por Mês e Natureza")
st.dataframe(consolidado)

# Exibir gráfico de barras
st.subheader("Gráfico de Receitas e Despesas por Mês")
grafico = pd.pivot_table(consolidado, values='Valor', index='Mes_Ref', columns='Natureza', fill_value=0)
st.bar_chart(grafico)