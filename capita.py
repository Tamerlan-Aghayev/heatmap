from sklearn.preprocessing import PolynomialFeatures
import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
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
    locs =("BAKU", "SUMGAYIT", "GANJA", "MINGHACHEVIR", "SIYAZAN", "SHIRVAN", "NAKHCHIVAN", "LANKARAN", "SHAMKIR", "SHAKI", "YEVLAKH", "KHACHMAZ", "AGHDAM", "JALILABAD", "KALBAJAR", "SHAMAKHI", "FUZULI", "SALYAN", "BARDA", "NEFTCHALA", "BOYUK HAMYA", "ZARAT")
    country =st.selectbox("Ərazi",locs)
    ok=st.button("Enerji sərfiyyatı və proqnoz")
    if ok:
        val=df_indexed.loc[country, "Consumption per capita(kWs)"]
        lat=df_indexed.loc[country, "latitude"]
        lon=df_indexed.loc[country, "longitude"]
        st.write("Adam başına düşən enerji sərfiyyatı: "+str(round(val, 2))+"kW")
        st.write('latitude: '+str(lat))
        st.write('longitude: '+str(lon))
        model = pickle.load(open('model.pkl', 'rb'))
    
    
        dtf=pd.DataFrame({'latitude':[float(lat)], 'longitude':[float(lon)]})
        transformer=PolynomialFeatures(degree=2)
        dtf=transformer.fit_transform(dtf)
        val=model.predict(dtf).sum()
        st.write("Proqnoz olunan enerji: "+str(round(val,2))+"kWs")