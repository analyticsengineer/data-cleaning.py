import streamlit as st
import pandas as pd
from PIL import Image

# UI layout
col1, col2 = st.columns(2)
image = Image.open('gif.gif')

col1.header("Replace Missing DateTime In Your Data")
col1.write("Missing datetime values can lead to inconsistencies and outliers.")
col2.image(image)

# File uploader
uploaded_file = st.file_uploader("Upload your file:", type=['csv', 'xlsx', 'pickle'])
df = None

# Read uploaded file
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

# Main logic after file load
if df is not None:
    st.markdown("### Your Data:")
    st.dataframe(df)

    if st.button('View Missing Values'):
        st.markdown("### Missing Values by Column:")
        st.write(df.isnull().sum())

    # Extract datetime columns
    datetime_cols = df.select_dtypes(include=['datetime64[ns]', 'datetime64', 'datetime64[ns, UTC]'])

    if datetime_cols.empty:
        st.warning("No datetime columns found in the data.")
    else:
        st.markdown("### DateTime Columns:")
        st.dataframe(datetime_cols)

        if st.button("Replace Missing DateTime"):
            cleaned_df = datetime_cols.fillna(pd.Timestamp("2000-01-01"))  # default fill value
            st.success("Missing datetime values replaced with '2000-01-01'.")
            st.dataframe(cleaned_df)

            # Show remaining nulls
            if cleaned_df.isnull().sum().sum() == 0:
                st.info("All missing datetime values have been handled.")
            else:
                st.warning("Some missing values remain.")

            # Export to CSV
            csv_data = cleaned_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label='📥 Download Cleaned DateTime Data',
                data=csv_data,
                file_name="cleaned_datetime_data.csv",
                mime='text/csv'
            )
else:
    st.info("Please upload a CSV, Excel, or Pickle file to begin.")
