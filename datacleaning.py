import streamlit as st
import pandas as pd
import base64
from st_aggrid import AgGrid
from openpyxl import load_workbook


# Adding Nav Bar
st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">',
            unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #291720;">
 <a class="navbar-brand" href="https://bit.ly/pinkdatahub" target="_blank">Pink Data Hub</a>
 <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false aria-label="Toggle navigation">
  <span class="navbar-toggler-icon"></span>
 </button>
   <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item active">
           <a class="nav-link disabled" href="#">Home<span class="sr-only">(curent)</span></a>
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

# App Header
st.markdown('''# **Data Cleaning Web App**
A simple Data Cleaning Web Application.
''')

file_ = open("image.png", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="dashboard gif">',
     unsafe_allow_html=True
)

# Styling side bar with image
st.sidebar.image("gif.gif", use_column_width=True)


# Multipage checkbox
page = st.sidebar.selectbox('Select Page', ['Choose','Check Missing Value', 'Remove Duplicate Value', 'Replace With Mean'
                                            ,'Replace With Median', 'Replace With Mode', 'Replace With Standard Deviation', 'Splitting Column'])

# Check missing value
if page == 'Check Missing Value':

    df_file = st.file_uploader("Upload your file: ", type=['csv', 'xlsx', 'pickle'])
    try:
        df_file = pd.read_csv(df_file)
        st.markdown("Your Data Record: ")
        AgGrid(df_file, editable=True)
    except:
        st.write("Upload A CSV, EXCEL OR PICKLE FILE")

        # Open Excel File
    try:
        df_file = pd.read_excel(df_file, engine='openpyxl')
        st.markdown("Your Data Record: ")
        AgGrid(df_file, editable=True)
    except:
        pass

        # Read Pickle File
    try:
        df_file = pd.read_pickle(df_file)
        st.markdown("Your Data Record: ")
        AgGrid(df_file, editable=True)
    except:
        pass

    try:
        df = df_file.isnull().sum()
        if st.button('View Missing Values'):
            st.write(df)

    except:
        pass

if page == 'Remove Duplicate Value':

    df_file = st.file_uploader("Upload your file: ", type=['csv', 'xlsx', 'pickle'])
    try:
        df_file = pd.read_csv(df_file)
        st.markdown("Your Data Record: ")
        AgGrid(df_file, editable=True)
    except:
        st.write("Upload A CSV, EXCEL OR PICKLE FILE")

        # Open Excel File
    try:
        df_file = pd.read_excel(df_file, engine='openpyxl')
        st.markdown("Your Data Record: ")
        AgGrid(df_file, editable=True)
    except:
        pass

        # Read Pickle File
    try:
        df_file = pd.read_pickle(df_file)
        st.markdown("Your Data Record: ")
        AgGrid(df_file, editable=True)
    except:
        pass

    try:
        df = df_file[df_file.duplicated()]
        if st.button("Check Duplicate Column"):
                        st.write(df)
    except:
        pass
    try:
        clean_data = st.multiselect("Choose Column:",options=df_file.columns)
                        
        df = df_file.drop_duplicates(subset=clean_data, keep='first', inplace=False)
        if st.button('Clean Data'):
            st.write(df)

     
            df = pd.DataFrame(df)
            file_name = "clean_data.csv"
            file_path = f"./{file_name}"

            df.to_csv(file_path)

            df = open(file_path, 'rb')
            st.download_button(label='Click to download',
                               data=df,
                               file_name=file_name,
                               key='download_df')
            df.close()


    except:
        pass

# Replace Null Value Mean
if page == 'Replace With Mean':

    df_file = st.file_uploader("Upload your file: ", type=['csv', 'xlsx', 'pickle'])
    try:
        df_file = pd.read_csv(df_file)
        st.markdown("Your Data Record: ")
        AgGrid(df_file, editable=True)
    except:
        st.write("Upload A CSV, EXCEL OR PICKLE FILE")

        # Open Excel File
    try:
        df_file = pd.read_excel(df_file, engine='openpyxl')
        st.markdown("Your Data Record: ")
        AgGrid(df_file, editable=True)
    except:
        pass

        # Read Pickle File
    try:
        df_file = pd.read_pickle(df_file)
        st.markdown("Your Data Record: ")
        AgGrid(df_file, editable=True)
    except:
        pass

    try:
        df = df_file.fillna(df_file.mean().round(0))
        if st.button('Clean Data'):
            st.write(df)

        df1 = df.isnull().sum()
        if st.button('View Null Value'):
            st.write(df1)

            df = pd.DataFrame(df)
            file_name = "clean_data.csv"
            file_path = f"./{file_name}"

            df.to_csv(file_path)

            df = open(file_path, 'rb')
            st.download_button(label='Click to download',
                               data=df,
                               file_name=file_name,
                               key='download_df')
            df.close()


    except:
        pass

# Replace with Average
if page == 'Replace With Median':

    df_file = st.file_uploader("Upload your file: ", type=['csv', 'xlsx', 'pickle'])
    try:
        df_file = pd.read_csv(df_file)
        st.markdown("Your Data Record: ")
        AgGrid(df_file, editable=True)
    except:
        st.write("Upload A CSV, EXCEL OR PICKLE FILE")

        # Open Excel File
    try:
        df_file = pd.read_excel(df_file, engine='openpyxl')
        st.markdown("Your Data Record: ")
        AgGrid(df_file, editable=True)
    except:
        pass

        # Read Pickle File
    try:
        df_file = pd.read_pickle(df_file)
        st.markdown("Your Data Record: ")
        AgGrid(df_file, editable=True)
    except:
        pass

    try:
        df = df_file.fillna(df_file.median().round(0))
        if st.button('Clean Data'):
            st.write(df)

        df1 = df.isnull().sum()
        if st.button('View Null Value'):
            st.write(df1)

            df = pd.DataFrame(df)
            file_name = "clean_data.csv"
            file_path = f"./{file_name}"

            df.to_csv(file_path)

            df = open(file_path, 'rb')
            st.download_button(label='Click to download',
                               data=df,
                               file_name=file_name,
                               key='download_df')
            df.close()


    except:
        pass

# Replace With Mode
if page == 'Replace With Mode':

    df_file = st.file_uploader("Upload your file: ", type=['csv', 'xlsx', 'pickle'])
    try:
        df_file = pd.read_csv(df_file)
        st.markdown("Your Data Record: ")
        AgGrid(df_file, editable=True)
    except:
        st.write("Upload A CSV, EXCEL OR PICKLE FILE")

        # Open Excel File
    try:
        df_file = pd.read_excel(df_file, engine='openpyxl')
        st.markdown("Your Data Record: ")
        AgGrid(df_file, editable=True)
    except:
        pass

        # Read Pickle File
    try:
        df_file = pd.read_pickle(df_file)
        st.markdown("Your Data Record: ")
        AgGrid(df_file, editable=True)
    except:
        pass

    try:
        df1 = df_file.fillna(df_file.mode().round(2))
        if st.button('Clean Data'):
            st.write(df1)

        df2 = df1.isnull().sum()
        if st.button('View Null Value'):
            st.write(df2)

            df1 = pd.DataFrame(df1)
            file_name = "clean_data.csv"
            file_path = f"./{file_name}"

            df1.to_csv(file_path)

            df1 = open(file_path, 'rb')
            st.download_button(label='Click to download',
                               data=df1,
                               file_name=file_name,
                               key='download_df')
            df1.close()


    except:
        pass

# Replace With Standard Deviation
if page == 'Replace With Standard Deviation':

    df_file = st.file_uploader("Upload your file: ", type=['csv', 'xlsx', 'pickle'])
    try:
        df_file = pd.read_csv(df_file)
        st.markdown("Your Data Record: ")
        AgGrid(df_file, editable=True)
    except:
        st.write("Upload A CSV, EXCEL OR PICKLE FILE")

        # Open Excel File
    try:
        df_file = pd.read_excel(df_file, engine='openpyxl')
        st.markdown("Your Data Record: ")
        AgGrid(df_file, editable=True)
    except:
        pass

        # Read Pickle File
    try:
        df_file = pd.read_pickle(df_file)
        st.markdown("Your Data Record: ")
        AgGrid(df_file, editable=True)
    except:
        pass

    try:
        df = df_file.fillna(df_file.std().round(0))
        if st.button('Clean Data'):
            st.write(df)

        df1 = df.isnull().sum()
        if st.button('View Null Value'):
            st.write(df1)

            df = pd.DataFrame(df)
            file_name = "clean_data.csv"
            file_path = f"./{file_name}"

            df.to_csv(file_path)

            df = open(file_path, 'rb')
            st.download_button(label='Click to download',
                               data=df,
                               file_name=file_name,
                               key='download_df')
            df.close()


    except:
        pass


if page == 'Splitting Column':

    df_file = st.file_uploader("Upload your file: ", type=['csv', 'xlsx', 'pickle'])
    try:
        df_file = pd.read_csv(df_file)
        st.markdown("Your Data Record: ")
        AgGrid(df_file, editable=True)
    except:
        st.write("Upload A CSV, EXCEL OR PICKLE FILE")

        # Open Excel File
    try:
        df_file = pd.read_excel(df_file, engine='openpyxl')
        st.markdown("Your Data Record: ")
        AgGrid(df_file, editable=True)
    except:
        pass

        # Read Pickle File
    try:
        df_file = pd.read_pickle(df_file)
        st.markdown("Your Data Record: ")
        AgGrid(df_file, editable=True)
    except:
        pass

    try:
       col = st.multiselect("Choose Column:",options=df_file.columns)
       df_clean = df_file[col].str.split(',', expand=True)
       if st.button('View Data'):
            AgGrid(df_file, editable=True)

                        
        
            df_clean = pd.DataFrame(df_clean)
            file_name = "clean_data.csv"
            file_path = f"./{file_name}"

            df_clean.to_csv(file_path)

            df_clean = open(file_path, 'rb')
            st.download_button(label='Click to download',
                               data=df_clean,
                               file_name=file_name,
                               key='download_df_clean')
            df_clean.close()


    except:
        pass

