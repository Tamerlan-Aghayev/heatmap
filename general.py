import streamlit as st
import pandas as pd
import plotly.express as px
def showGeneral():
    st.title("Ərazi üzrə enerji sərfiyyatı")
    df_indexed=pd.read_csv("data_indexed.csv")
    df_indexed.set_index("location", inplace=True)
    df=pd.read_csv("data_new.csv")
    fig2 = px.scatter_mapbox(df, lat="latitude", lon="longitude", color="General consumption(kWs)", 
                        size="General consumption(kWs)", hover_name="location", zoom=6,
                        mapbox_style="carto-positron",size_max=60)

# Show the map
    fig2.update_layout(width=1000, height=700)
    st.plotly_chart(fig2)
    locs =("BAKU", "SUMGAYIT", "GANJA", "MINGHACHEVIR", "SIYAZAN", "SHIRVAN", "NAKHCHIVAN", "LANKARAN", "SHAMKIR", "SHAKI", "YEVLAKH", "KHACHMAZ", "AGHDAM", "JALILABAD", "KALBAJAR", "SHAMAKHI", "FUZULI", "SALYAN", "BARDA", "NEFTCHALA", "BOYUK HAMYA")
    country =st.selectbox("Ərazi",locs)
    ok=st.button("Enerji sərfiyyatı")
    if ok:
        val=df_indexed.loc[country, "General consumption(kWs)"]
        st.write("Ərazi üzrə enerji sərfiyyatı: "+str(round(val, 2))+"kW")