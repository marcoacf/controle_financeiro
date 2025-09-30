import streamlit as st
import pandas as pd
import plotly.express as px
from google_sheets import carregar_dados

st.title("📊 Dashboard Financeiro")

# Carregar dados da planilha
df = carregar_dados()

# Filtro opcional por mês
meses_disponiveis = sorted(df['Mes_Ref'].unique())
meses_selecionados = st.multiselect("Filtrar por Mês de Referência", meses_disponiveis)

if meses_selecionados:
    df = df[df['Mes_Ref'].isin(meses_selecionados)]

# Gráfico de pizza por grupo
st.subheader("Distribuição por Grupo")
fig1 = px.pie(df, names='Grupo', values='Valor', title='Distribuição de Valores por Grupo')
st.plotly_chart(fig1, use_container_width=True)

# Gráfico de barras por mês e natureza
st.subheader("Receitas e Despesas por Mês")
fig2 = px.bar(df, x='Mes_Ref', y='Valor', color='Natureza', barmode='group',
              title='Receitas vs Despesas por Mês')
st.plotly_chart(fig2, use_container_width=True)

# Gráfico de linha acumulada por mês
st.subheader("Evolução Financeira Mensal")
df_mes = df.groupby(['Mes_Ref', 'Natureza'])['Valor'].sum().reset_index()
fig3 = px.line(df_mes, x='Mes_Ref', y='Valor', color='Natureza', markers=True,
               title='Evolução de Receitas e Despesas')
st.plotly_chart(fig3, use_container_width=True)