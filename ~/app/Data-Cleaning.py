import streamlit as st
import pandas as pd
from openpyxl import load_workbook
import datetime
import time
from PIL import Image

# Load Bootstrap CSS for Navbar
st.markdown('''
<link rel="stylesheet" 
      href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" 
      integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" 
      crossorigin="anonymous">
''', unsafe_allow_html=True)

# Navigation Bar
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #291720;">
  <a class="navbar-brand" href="https://bit.ly/pinkdatahub" target="_blank">Pink Data Hub</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
    aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://github.com/Designegycreatives/datacleaning-app.py" target="_blank">GitHub</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://www.linkedin.com/in/anuoluwapo-abiodun-balogun-64b977186/" target="_blank">LinkedIn</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

# Space for navbar
st.markdown("<br><br><br><br>", unsafe_allow_html=True)

# App Header Layout
col1, col2 = st.columns(2)
image = Image.open('image.png')

with col1:
    st.markdown("## **Data Cleaning Web App**")
    st.write("A simple Data Cleaning Web Application.")
    st.write("This Web Application is best for data wrangling.")
    st.write("""
        Data cleaning is a time-consuming and tedious task. But it's essential to make sure your data is accurate and consistent before you can analyze it or share it with others.
        
        Our data cleaning web application makes it easy to clean your data quickly and easily. Simply upload your data, select the cleaning tasks you want to perform, and click the **Clean** button. Our application will do the rest — automatically identifying and correcting errors in your data.
    """)

with col2:
    col2.image(image)
