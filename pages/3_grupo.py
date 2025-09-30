import streamlit as st
import pandas as pd
from google_sheets import carregar_dados
import plotly.express as px

st.title("👥 Avaliação por Grupo")

# Carregar dados da planilha
df = carregar_dados()

# Filtro opcional por grupo
grupos_disponiveis = sorted(df['Grupo'].unique())
grupos_selecionados = st.multiselect("Filtrar por Grupo", grupos_disponiveis)

if grupos_selecionados:
    df = df[df['Grupo'].isin(grupos_selecionados)]

# Agrupar por grupo e natureza
grupo_total = df.groupby(['Grupo', 'Natureza'])['Valor'].sum().reset_index()

st.subheader("Resumo por Grupo e Natureza")
st.dataframe(grupo_total)

# Gráfico de barras por grupo
st.subheader("Gráfico por Grupo")
fig = px.bar(grupo_total, x='Grupo', y='Valor', color='Natureza', barmode='group',
             title='Receitas e Despesas por Grupo')
