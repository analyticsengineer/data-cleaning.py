import streamlit as st
import pandas as pd
from openpyxl import load_workbook
import datetime
import time
from PIL import Image 

col1, col2 = st.columns(2)

image = Image.open('gif.gif')

col1.header("Replace the object null values with mode")
col1.write("These Reduces The Number Of Outliers In Your Data")
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

try:
  df = df_file.isnull().sum()
  if st.button('View Missing Values'):
     st.write(df)

except:
  pass

try:
   if st.button('Clean Data'):
    for column in df_file.columns:
        df_file[column].fillna(df_file[column].mode().iloc[0], inplace=True)
    st.write(df_file)

    df = df_file.isnull().sum()
    if st.button('View Missing Values'):
     st.write(df)

    file_name = "clean_data.csv"
    file_path = f"./{file_name}"

    df_file.to_csv(file_path)

    with open(file_path, 'rb') as file:
        st.download_button(label='Click to download',
                           data=file,
                           file_name=file_name,
                           key='download_df')
    df.close()
except:
  pass
