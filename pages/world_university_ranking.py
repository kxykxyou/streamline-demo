import streamlit as st
import pandas as pd
from infrastructure import PROJECT_PATH
import os

file_path = os.path.join(PROJECT_PATH, "data/world_university_rankings_2023.csv")
df = pd.read_csv(file_path)

st.sidebar.markdown("world_university_rankings_2023.csv")

st.title("world_university_rankings_2023")
st.dataframe(df)
