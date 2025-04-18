import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Análise de Dados com Upload de CSV")

# Upload do arquivo CSV
uploaded_file = st.file_uploader("Faça upload do seu arquivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Prévia dos dados:")
    st.dataframe(df)

    # Selecionar coluna numérica
    numeric_columns = df.select_dtypes(include='number').columns.tolist()

    if numeric_columns:
        selected_column = st.selectbox("Selecione uma coluna numérica para análise:", numeric_columns)

        if selected_column:
            col_data = df[selected_column]
            st.write(f"📈 **Estatísticas da coluna '{selected_column}':**")
            st.write(f"👉 Média: {col_data.mean():.2f}")
            st.write(f"👉 Mediana: {col_data.median():.2f}")
            st.write(f"👉 Desvio padrão: {col_data.std():.2f}")

            # Gráfico interativo (histograma)
            st.subheader("Gráfico interativo")
            fig = px.histogram(df, x=selected_column, nbins=30, title=f"Distribuição de {selected_column}")
            st.plotly_chart(fig)
    else:
        st.warning("O CSV enviado não contém colunas numéricas.")
else:
    st.info("Por favor, envie um arquivo CSV para começar.")
