import streamlit as st
import pandas as pd
import numpy as np

# 1. Título do App
st.title("Meu Primeiro Dashboard 📊")

# 2. Input do Usuário (Sidebar)
st.sidebar.header("Configurações")
quantidade = st.sidebar.slider("Quantos números gerar?", 10, 100, 50)

# 3. Lógica de Dados
dados = pd.DataFrame(
    np.random.randn(quantidade, 2),
    columns=['Vendas', 'Metas']
)

# 4. Exibição de Resultados
st.write(f"Exibindo os últimos {quantidade} registros gerados aleatoriamente:")

# Criar abas para organizar o conteúdo
tab1, tab2 = st.tabs(["Gráfico", "Tabela de Dados"])

with tab1:
    st.bar_chart(dados)

with tab2:
    st.dataframe(dados)

# Botão de interação
if st.button('Comemorar!'):
    st.balloons()
