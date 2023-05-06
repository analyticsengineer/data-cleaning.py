import streamlit as st
import pandas as pd
from openpyxl import load_workbook
import datetime
import numpy as np
import time
from PIL import Image 
import plotly.graph_objects as go
from scipy.stats import norm

col1, col2 = st.columns(2)

image = Image.open('gif.gif')

col1.header("Check data distribution")
col1.write("These shows the normal distribution of the dataset")
col2.image(image)


df_file = st.file_uploader("Upload your file: ", type=['csv', 'xlsx', 'pickle'])
try:
  df_file = pd.read_csv(df_file)
  st.markdown("Your Data Record: ")
  st.dataframe(df_file)
except:
  st.write("Upload A CSV, EXCEL OR PICKLE FILE")

# Open Excel File
try:
  df_file = pd.read_excel(df_file, engine='openpyxl')
  st.markdown("Your Data Record: ")
  st.dataframe(df_file)
except:
  pass

# Read Pickle File
try:
  df_file = pd.read_pickle(df_file)
  st.markdown("Your Data Record: ")
  st.dataframe(df_file)
except:
  pass


# Calculate mean and standard deviation of the dataset
try:
  if st.button('Check Data Normality'):
    mean = df_file.mean()
    std = df_file.std()
    st.write(mean)
    st.write(std)

except:
  pass
