import streamlit as st
import plotly.express as px
import pandas as pd
import general as g
import capita as c

page=st.sidebar.selectbox("Sərfiyyatın növü", ("Ümumi","Adam başına"))
if page=="Ümumi":
    g.showGeneral()
else :
    c.showPerCapita()
