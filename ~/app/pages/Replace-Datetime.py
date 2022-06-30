import streamlit as st
import pandas as pd
from openpyxl import load_workbook
import datetime
import time
from PIL import Image 

col1, col2 = st.columns(2)
image = Image.open('gif.gif')

col1.header("Replace Date Time In Your Data")
col1.write("Misisng Date Time Creates Outliers In Your Data")
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
   time = df_file.select_dtypes(include=['timestamp', 'datetime'])
   df_date = time.fillna(0)
   if st.button('Clean Data'):
      st.write(df_date)

   df_date1 = df_date.isnull().sum()
   if st.button('View Null Value'):
      st.write(df_date1)

   df_date = pd.DataFrame(df-date)
   file_name = "clean_data.csv"
   file_path = f"./{file_name}"

   df_date.to_csv(file_path)

   df_date = open(file_path, 'rb')
   st.download_button(label='Click to download',
                       data=df_date,
                       file_name=file_name,
                       key='download_df')
   df_date.close()


except:
  pass

