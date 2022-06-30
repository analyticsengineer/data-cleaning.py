import streamlit as st
import pandas as pd
from openpyxl import load_workbook
import datetime
import time
from PIL import image 

col1, col2 = st.columns(2)

col1.header("Check For Missing Values In Your Data")
col2.write("Misisng Values Creates Outliers In Your Data")

image = Image.open('gif.gif')

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

try:
  df = df_file.isnull().sum()
  if st.button('View Missing Values'):
  st.write(df)

except:
  pass

try:
  df = df_file.fillna(df_file.median().round(0))
  if st.button('Clean Data'):
  st.write(df)

  df1 = df.isnull().sum()
  if st.button('View Null Value'):
  st.write(df1)

  df = pd.DataFrame(df)
  file_name = "clean_data.csv"
  file_path = f"./{file_name}"

  df.to_csv(file_path)

  df = open(file_path, 'rb')
  st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
  df.close()
