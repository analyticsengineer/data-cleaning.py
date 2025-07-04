import streamlit as st
import pandas as pd
from PIL import Image

# Layout
col1, col2 = st.columns(2)
image = Image.open('gif.gif')

col1.header("Replace Object Null Values with Mode")
col1.write("This reduces the number of outliers in your data.")
col2.image(image)

# File uploader
uploaded_file = st.file_uploader("Upload your file:", type=['csv', 'xlsx', 'pickle'])
df = None

# Read the uploaded file based on extension
if uploaded_file:
    file_ext = uploaded_file.name.split('.')[-1].lower()

    try:
        if file_ext == 'csv':
            df = pd.read_csv(uploaded_file)
        elif file_ext == 'xlsx':
            df = pd.read_excel(uploaded_file, engine='openpyxl')
        elif file_ext == 'pickle':
            df = pd.read_pickle(uploaded_file)
        else:
            st.error("Unsupported file type.")
    except Exception as e:
        st.error(f"Error loading file: {e}")

# Main logic
if df is not None:
    st.markdown("### Your Data:")
    st.dataframe(df)

    if st.button('View Missing Values'):
        st.markdown("### Missing Values by Column:")
        st.write(df.isnull().sum())

    if st.button('Clean Data'):
        object_cols = df.select_dtypes(include=['object', 'category']).columns
        for column in object_cols:
            if df[column].isnull().any():
                mode_val = df[column].mode().iloc[0]
                df[column].fillna(mode_val, inplace=True)

        st.success("Missing values in object columns replaced with mode.")
        st.dataframe(df)

        # Enable CSV download
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label='📥 Download Cleaned CSV',
            data=csv,
            file_name='clean_data.csv',
            mime='text/csv'
        )
else:
    st.info("Please upload a CSV, Excel, or Pickle file to begin.")
