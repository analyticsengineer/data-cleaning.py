import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Layout
col1, col2 = st.columns(2)
image = Image.open('gif.gif')

col1.header("Replace Null Values with Column Median")
col1.write("This reduces the number of outliers in your data.")
col2.image(image)

# File uploader
uploaded_file = st.file_uploader("Upload your file:", type=['csv', 'xlsx', 'pickle'])
df = None

# Read the uploaded file once
if uploaded_file:
    ext = uploaded_file.name.split('.')[-1].lower()
    try:
        if ext == 'csv':
            df = pd.read_csv(uploaded_file)
        elif ext == 'xlsx':
            df = pd.read_excel(uploaded_file, engine='openpyxl')
        elif ext == 'pickle':
            df = pd.read_pickle(uploaded_file)
        else:
            st.error("Unsupported file type.")
    except Exception as e:
        st.error(f"Error loading file: {e}")

# Main logic
if df is not None:
    st.markdown("### Your Data:")
    st.dataframe(df)

    # Show missing values
    if st.button('View Missing Values'):
        st.markdown("### Missing Values by Column:")
        st.write(df.isnull().sum())

    # Clean nulls with median
    if st.button('Clean Data'):
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        df[numeric_cols] = df[numeric_cols].apply(lambda col: col.fillna(col.median().round(0)))

        st.success("Missing values in numeric columns replaced with median.")
        st.markdown("### Cleaned Data:")
        st.dataframe(df)

        # Show remaining missing values
        remaining_nulls = df.isnull().sum()
        if remaining_nulls.sum() == 0:
            st.info("No more missing values.")
        else:
            st.warning("Some missing values still remain.")
            st.write(remaining_nulls)

        # Download cleaned file
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label='📥 Download Cleaned Data',
            data=csv,
            file_name="clean_data.csv",
            mime='text/csv'
        )
else:
    st.info("Please upload a CSV, Excel, or Pickle file to begin.")
