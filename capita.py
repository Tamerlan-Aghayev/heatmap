import streamlit as st
import pandas as pd
import plotly.express as px
def showPerCapita():
    st.title("Adam başına düşən enerji sərfiyyatı")
    df_indexed=pd.read_csv("data_indexed.csv")
    df_indexed.set_index("location", inplace=True)
    df=pd.read_csv("data_new.csv")
    df["Consumption per capita(kWs)"]=round(df["Consumption per capita(kWs)"], 2)
    fig1 = px.scatter_mapbox(df, lat="latitude", lon="longitude", color="Consumption per capita(kWs)",
                            size="Consumption per capita(kWs)", hover_name="location", zoom=6,
                            mapbox_style="carto-positron",size_max=50)

    fig1.update_layout(width=1000, height=700)

    st.plotly_chart(fig1)
    locs =("BAKU", "SUMGAYIT", "GANJA", "MINGHACHEVIR", "SIYAZAN", "SHIRVAN", "NAKHCHIVAN", "LANKARAN", "SHAMKIR", "SHAKI", "YEVLAKH", "KHACHMAZ", "AGHDAM", "JALILABAD", "KALBAJAR", "SHAMAKHI", "FUZULI", "SALYAN", "BARDA", "NEFTCHALA", "BOYUK HAMYA")
    country =st.selectbox("Ərazi",locs)
    ok=st.button("Enerji sərfiyyatı")
    if ok:
        val=df_indexed.loc[country, "Consumption per capita(kWs)"]
        st.write("Adam başına düşən enerji sərfiyyatı: "+str(round(val, 2))+"kW")