import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.graph_objects as go
from scipy.stats import norm

# UI Layout
col1, col2 = st.columns(2)
image = Image.open('gif.gif')

col1.header("Check Data Distribution")
col1.write("Visualize how your dataset aligns with a normal distribution.")
col2.image(image)

# File uploader
uploaded_file = st.file_uploader("Upload your file:", type=['csv', 'xlsx', 'pickle'])

df = None

# File reading based on type
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
        st.error(f"Failed to read file: {e}")

# If data is loaded
if df is not None:
    st.markdown("### Your Data:")
    st.dataframe(df)

    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

    if numeric_cols:
        selected_col = st.selectbox("Select a numeric column to analyze:", numeric_cols)

        if st.button("Check Data Normality"):
            data = df[selected_col].dropna()

            # Calculate mean and std
            mu, std = norm.fit(data)

            # Plot distribution
            fig = go.Figure()

            fig.add_trace(go.Histogram(
                x=data,
                histnorm='probability density',
                name='Data',
                marker_color='lightskyblue',
                opacity=0.75
            ))

            # Plot fitted normal curve
            x_vals = np.linspace(min(data), max(data), 100)
            pdf_vals = norm.pdf(x_vals, mu, std)

            fig.add_trace(go.Scatter(
                x=x_vals,
                y=pdf_vals,
                mode='lines',
                name='Fitted Normal Curve',
                line=dict(color='firebrick', width=2)
            ))

            fig.update_layout(
                title=f"Distribution of {selected_col}",
                xaxis_title=selected_col,
                yaxis_title='Density',
                bargap=0.1
            )

            st.plotly_chart(fig)
            st.success(f"Mean = {mu:.2f},  Std Dev = {std:.2f}")

    else:
        st.warning("No numeric columns found in the uploaded file.")
else:
    st.info("Upload a CSV, Excel, or Pickle file to begin.")
