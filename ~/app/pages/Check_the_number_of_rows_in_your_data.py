import streamlit as st
import pandas as pd
from openpyxl import load_workbook
import datetime
import time
from PIL import Image 

col1, col2 = st.columns(2)
image = Image.open('gif.gif')

col1.header("Check For Missing Values In Your Data")
col1.write("Misisng Values Creates Outliers In Your Data")
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
  df = len(df_file)
  st.write("The number of rows in your data is {} ".format(df))
  st.write("If Number of rows is < 10,000 replace null values with Mean")
  st.write("If Number of rows is > 10,000 replace null values with Median")
  

except:
  pass
