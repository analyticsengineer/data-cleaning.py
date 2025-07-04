import streamlit as st
import pandas as pd
from PIL import Image

# Header section
col1, col2 = st.columns(2)
image = Image.open('gif.gif')

col1.header("Split a Column into Multiple Columns")
col1.write("This helps structure your data by breaking up values in a column.")
col2.image(image)

# Upload data
uploaded_file = st.file_uploader("Upload your file:", type=['csv', 'xlsx', 'pickle'])
df = None

# Load file
if uploaded_file:
    ext = uploaded_file.name.split('.')[-1].lower()
    try:
        if ext == 'csv':
            df = pd.read_csv(uploaded_file)
        elif ext == 'xlsx':
            df = pd.read_excel(uploaded_file, engine='openpyxl')
        elif ext == 'pickle':
            df = pd.read_pickle(uploaded_file)
    except Exception as e:
        st.error(f"File loading error: {e}")

# Show data and actions
if df is not None:
    st.markdown("### Your Data")
    st.dataframe(df)

    if st.button("View Missing Values"):
        st.write(df.isnull().sum())

    col_to_split = st.selectbox("Select the column to split", df.columns)

    delimiters = {
        "Comma ( , )": ",",
        "Hyphen ( - )": "-",
        "Underscore ( _ )": "_",
        "Space ( )": " ",
        "Forward Slash ( / )": "/",
        "Backslash ( \\ )": "\\"
    }

    delimiter_label = st.selectbox("Choose a delimiter to split by", list(delimiters.keys()))
    delimiter = delimiters[delimiter_label]

    if st.button("Split Column"):
        try:
            split_df = df[col_to_split].astype(str).str.split(delimiter, expand=True)
            st.markdown("### Split Result")
            st.dataframe(split_df)

            # Save for download
            csv = split_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Split Data",
                data=csv,
                file_name="split_data.csv",
                mime="text/csv",
                key='download-split'
            )
        except Exception as e:
            st.error(f"Error during split: {e}")
else:
    st.info("Upload a CSV, Excel, or Pickle file to begin.")
