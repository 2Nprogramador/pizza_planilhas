import streamlit as st
import pandas as pd
import os

# Nomes dos arquivos das planilhas
FILES = {
    "Planilha 1": "destaques_pizza_com_text.csv",  # Ou "dados1.csv"
    "Planilha 2": "legendas_pizza_com_text.csv",  # Ou "dados2.csv"
    "Planilha 3": "postagens_pizza_com_text.csv",  # Ou "dados3.csv"
}

# Título do app
st.title("Visualizador de Planilhas")

# Criando as abas
tab1, tab2, tab3 = st.tabs(FILES.keys())

# Função para carregar e exibir a planilha
def load_and_display_file(file_name):
    if os.path.exists(file_name):
        try:
            if file_name.endswith(".xlsx"):
                df = pd.read_excel(file_name)
            else:
                df = pd.read_csv(file_name)

            # Exibe a planilha
            st.write(f"### {file_name}")
            st.dataframe(df)

            # Botão para download da planilha
            st.download_button(
                label="Baixar Planilha",
                data=df.to_csv(index=False).encode("utf-8"),
                file_name=f"{file_name}_exportado.csv",
                mime="text/csv",
            )
        except Exception as e:
            st.error(f"Erro ao abrir {file_name}: {e}")
    else:
        st.warning(f"Arquivo {file_name} não encontrado.")

# Exibir cada planilha na respectiva aba
with tab1:
    load_and_display_file(FILES["Planilha 1"])

with tab2:
    load_and_display_file(FILES["Planilha 2"])

with tab3:
    load_and_display_file(FILES["Planilha 3"])

