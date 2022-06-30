import streamlit as st
import pandas as pd
from openpyxl import load_workbook
import datetime
import time
from PIL import Image 

col1, col2 = st.columns(2)
image = Image.open('gif.gif')


col1.header("Split Your Data Into Columns")
col1.write("This makes your data looks organized")
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
  col_clean = st.selectbox("Choose Column:",options=df_file.columns)
       
  df_clean1 = df_file[col_clean].str.split(',', expand=True)
  if st.button('split by comma'):
      st.write(df_clean1)
              
      df_clean1 = pd.DataFrame(df_clean1)
      file_name = "clean_data.csv"
      file_path = f"./{file_name}"

      df_clean1.to_csv(file_path)

      df_clean1= open(file_path, 'rb')
      st.download_button(label='Click to download',
                      data=df_clean1,
                      file_name=file_name,
                      key='download_df_clean')
      df_clean1.close()

       
  df_clean2 = df_file[col_clean].str.split('-', expand=True)
  if st.button('split by hyphen'):
      st.write(df_clean2)
            
      df_clean2 = pd.DataFrame(df_clean2)
      file_name = "clean_data.csv"
      file_path = f"./{file_name}"

      df_clean2.to_csv(file_path)

      df_clean2 = open(file_path, 'rb')
      st.download_button(label='Click to download',
                      data=df_clean2,
                      file_name=file_name,
                      key='download_df_clean')
      df_clean2.close()

                       
   df_clean3 = df_file[col_clean].str.split('_', expand=True)               
   if st.button('split by underscore'):
      st.write(df_clean3)
      df_clean3 = pd.DataFrame(df_clean3)
      file_name = "clean_data.csv"
      file_path = f"./{file_name}"

      df_clean3.to_csv(file_path)

      df_clean3 = open(file_path, 'rb')
      st.download_button(label='Click to download',
                       data=df_clean3,
                       file_name=file_name,
                       key='download_df_clean')
      df_clean3.close()

      
   df_clean4 = df_file[col_clean].str.split('/', expand=True)
   if st.button('split by backslash'):
      st.write(df_clean4)
      df_clean4 = pd.DataFrame(df_clean4)
      file_name = "clean_data.csv"
      file_path = f"./{file_name}"

      df_clean4.to_csv(file_path)

      df_clean4 = open(file_path, 'rb')
      st.download_button(label='Click to download',
                               data=df_clean4,
                               file_name=file_name,
                               key='download_df_clean')
      df_clean4.close()
       
   df_clean5 = df_file[col_clean].str.split(' ', expand=True)                
   if st.button('split by space'):
      st.write(df_clean5)
      df_clean5 = pd.DataFrame(df_clean5)
      file_name = "clean_data.csv"
      file_path = f"./{file_name}"

      df_clean5.to_csv(file_path)

      df_clean5 = open(file_path, 'rb')
      st.download_button(label='Click to download',
                           data=df_clean5,
                           file_name=file_name,
                           key='download_df_clean')
      df_clean5.close()

     
            
   df_clean6 = df_file[col_clean].str.split('/ ', expand=True)            
   if st.button('split by forwardslash'):
      st.write(df_clean6)
      df_clean6 = pd.DataFrame(df_clean6)
      file_name = "clean_data.csv"
      file_path = f"./{file_name}"

      df_clean6.to_csv(file_path)

      df_clean6 = open(file_path, 'rb')
      st.download_button(label='Click to download',
                               data=df_clean6,
                               file_name=file_name,
                               key='download_df_clean')
      df_clean6.close()
      
except:
  pass
                        
