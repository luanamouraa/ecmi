import streamlit as st
import pandas as pd

st.title('Trabalho csv')
st.caption('Luana Moura')

df = pd.read_csv('starbucks.csv', sep=',', quotechar='"')
st.dataframe(df)
