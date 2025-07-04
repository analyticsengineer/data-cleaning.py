import streamlit as st
import pandas as pd
from PIL import Image

# Layout
col1, col2 = st.columns(2)
image = Image.open('gif.gif')

col1.header("Remove Duplicate Values In Your Data")
col1.write("Duplicate values can create misleading outliers and inflate results.")
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
        st.error(f"Error reading file: {e}")

# Display and operations
if df is not None:
    st.markdown("### Uploaded Data")
    st.dataframe(df)

    # View missing values
    if st.button('View Missing Values'):
        missing = df.isnull().sum()
        st.markdown("### Missing Values by Column:")
        st.write(missing)

    # View duplicate rows
    if st.button("Check Duplicate Rows"):
        duplicates = df[df.duplicated()]
        if not duplicates.empty:
            st.markdown("### Duplicate Rows Found:")
            st.dataframe(duplicates)
        else:
            st.success("No duplicate rows found.")

    # Drop duplicates by selected columns
    st.markdown("### Select Columns to Identify Duplicates")
    selected_cols = st.multiselect("Choose column(s):", options=df.columns)

    if selected_cols and st.button("Remove Duplicates"):
        cleaned_df = df.drop_duplicates(subset=selected_cols)
        st.success(f"Removed duplicates based on: {', '.join(selected_cols)}")
        st.dataframe(cleaned_df)

        # Optional download
        csv = cleaned_df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Cleaned Data", data=csv, file_name="cleaned_data.csv", mime="text/csv")
else:
    st.info("Upload a CSV, Excel, or Pickle file to get started.")
