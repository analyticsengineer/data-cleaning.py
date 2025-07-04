import streamlit as st
import pandas as pd
from PIL import Image
import os

# UI layout
col1, col2 = st.columns(2)
image = Image.open('gif.gif')

col1.header("Check For Missing Values In Your Data")
col1.write("Missing values create outliers in your data.")
col2.image(image)

# File uploader
uploaded_file = st.file_uploader("Upload your file:", type=['csv', 'xlsx', 'pickle'])

df = None

# File processing
if uploaded_file is not None:
    file_type = uploaded_file.name.split('.')[-1].lower()

    try:
        if file_type == 'csv':
            df = pd.read_csv(uploaded_file)
        elif file_type == 'xlsx':
            df = pd.read_excel(uploaded_file, engine='openpyxl')
        elif file_type == 'pickle':
            df = pd.read_pickle(uploaded_file)
        else:
            st.error("Unsupported file type.")
    except Exception as e:
        st.error(f"Error loading file: {e}")

    # Display data if successfully loaded
    if df is not None:
        st.markdown("### Your Data:")
        st.dataframe(df)

        # Show missing values
        if st.button('View Missing Values'):
            missing = df.isnull().sum()
            st.markdown("### Missing Values by Column:")
            st.write(missing)
else:
    st.info("Please upload a CSV, Excel, or Pickle file.")
