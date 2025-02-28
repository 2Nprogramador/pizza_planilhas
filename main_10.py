import streamlit as st
import pandas as pd
import os

# Nome do arquivo da planilha (ajuste conforme necessário)
FILE_NAME = "destaques_pizza_com_text.csv"  # Ou "dados.csv" se for CSV

# Título do app
st.title("Visualizador de Planilha")

# Verifica se o arquivo existe
if os.path.exists(FILE_NAME):
    try:
        # Tenta abrir como Excel primeiro, se falhar, tenta CSV
        if FILE_NAME.endswith(".xlsx"):
            df = pd.read_excel(FILE_NAME)
        else:
            df = pd.read_csv(FILE_NAME)

        # Exibe a planilha
        st.write("### Dados da Planilha:")
        st.dataframe(df)

        # Permite baixar a planilha
        st.download_button(
            label="Baixar Planilha",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="dados_exportados.csv",
            mime="text/csv",
        )
    except Exception as e:
        st.error(f"Erro ao abrir a planilha: {e}")
else:
    st.warning("Arquivo da planilha não encontrado. Certifique-se de que o arquivo está no diretório do projeto.")

