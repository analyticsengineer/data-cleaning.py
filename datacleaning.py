import streamlit as st
import pandas as pd

# Adding Nav Bar
st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">',
            unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #FFFFFA;">
 <a class="navbar-brand" href="https://github.com/Designegycreatives/datacleaning-app.py" target="_blank">Github Page</a>
 <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false aria-label="Toggle navigation">
  <span class="navbar-toggler-icon"></span>
 </button>
 <div class="collapse navbar-collapse" id="navbarNav">
   <ul class="navbar-nav">
    <li> class="nav-item active">
     <a class="nav-link disabled" href="#">
 Home <span class="sr-only">(curent)</span></a>
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
