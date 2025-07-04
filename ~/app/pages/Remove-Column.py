import streamlit as st
import pandas as pd
import time
from PIL import Image

# UI layout
col1, col2 = st.columns(2)
image = Image.open('gif.gif')

col1.header("Split Your Data Into Columns")
col1.write("This makes your data look organized.")
col2.image(image)

# File uploader
uploaded_file = st.file_uploader("Upload your file:", type=['csv', 'xlsx', 'pickle'])

df = None

# Load data only once
if uploaded_file:
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

# If data is loaded
if df is not None:
    st.markdown("### Your Data:")
    st.dataframe(df)

    # Select columns to drop
    columns_to_drop = st.multiselect("Choose columns to drop:", options=df.columns)

    if st.button('Generate New Data'):
        cleaned_df = df.drop(columns=columns_to_drop)

        st.markdown("### Cleaned Data:")
        st.dataframe(cleaned_df)

        # Convert to CSV and enable download
        csv_data = cleaned_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Cleaned CSV",
            data=csv_data,
            file_name="clean_data.csv",
            mime='text/csv'
        )
else:
    st.info("Please upload a CSV, Excel, or Pickle file to begin.")
