import streamlit as st
import requests
import pandas as pd
from config import API_URL

st.title("Dashboard")

data = requests.get(f"{API_URL}/empleados").json()
df = pd.DataFrame(data)

st.dataframe(df)
st.write(df["salario"].mean())
