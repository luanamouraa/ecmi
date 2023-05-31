import streamlit as st
import pandas as pd
st.title('Trabalho csv+gráfico')
st.caption('Luana Moura')

df = pd.read_csv('Microsoft Stocks.csv', sep=',')
st.dataframe(df)
