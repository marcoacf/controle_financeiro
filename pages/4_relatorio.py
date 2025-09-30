import streamlit as st
import pandas as pd
from google_sheets import carregar_dados
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

st.title("📋 Relatório Detalhado")

# Carregar dados da planilha
df = carregar_dados()

# Filtros
filtro_grupo = st.multiselect("Filtrar por Grupo", df['Grupo'].unique())
filtro_mes = st.multiselect("Filtrar por Mês", df['Mes_Ref'].unique())

if filtro_grupo:
    df = df[df['Grupo'].isin(filtro_grupo)]
if filtro_mes:
    df = df[df['Mes_Ref'].isin(filtro_mes)]

st.dataframe(df)

# Função para exportar para Excel
def exportar_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Relatorio')
    output.seek(0)
    return output

# Função para exportar para PDF
def exportar_pdf(df):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    x_offset, y_offset = 40, height - 40
    line_height = 15

    c.setFont("Helvetica", 10)
    c.drawString(x_offset, y_offset, "Relatório Financeiro")
    y_offset -= 2 * line_height

    colunas = df.columns.tolist()
    for i, col in enumerate(colunas):
        c.drawString(x_offset + i * 70, y_offset, col)
    y_offset -= line_height

    for _, row in df.iterrows():
        for i, item in enumerate(row):
            c.drawString(x_offset + i * 70, y_offset, str(item))
        y_offset -= line_height
        if y_offset < 40:
            c.showPage()
            y_offset = height - 40

    c.save()
    buffer.seek(0)
    return buffer

# Botões de exportação
col1, col2 = st.columns(2)

with col1:
    excel_data = exportar_excel(df)
    st.download_button(
        label="📥 Exportar para Excel",
        data=excel_data,
        file_name="relatorio_financeiro.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

with col2:
    pdf_data = exportar_pdf(df)
    st.download_button(
        label="📄 Exportar para PDF",
        data=pdf_data,
        file_name="relatorio_financeiro.pdf",
        mime="application/pdf"
    )
