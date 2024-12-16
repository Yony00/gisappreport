import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import leafmap.foliumap as leafmap
import folium

st.title("測試用頁面")
m1 = leafmap.Map(center=[23, 120], zoom=8)
m2 = leafmap.Map(center=[23, 120], zoom=8)
url="https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E6%A8%A1%E6%93%AC%E6%95%B8%E5%80%BC_%E8%87%BA%E5%8D%97.csv"
data = pd.read_csv(url)

selectable_columns = ['邏輯樹', 'AbrahamsonEtAl2014','BooreAtkinson2008','CampbellBozorgnia2008','ChiouYoungs2008','LinLee2008SInter']
options = st.selectbox('選擇一個GMPE呈現', selectable_columns)

if options=="邏輯樹":
    m1.add_heatmap(
        data,
        latitude="y",
        longitude="x",
        value="邏輯樹",
        name="邏輯樹",
        radius=15,
        pacity=0.7,
    )
    m2.add_heatmap(
        data,
        latitude="y",
        longitude="x",
        value="AbrahamsonEtAl2014",
        name="AbrahamsonEtAl2014",
        radius=15,
        pacity=0.7,
    ) 
    col1, col2 = st.columns(2)

with col1:
    st.write("左側地圖：邏輯樹")
    m1.to_streamlit(height=700)

with col2:
    st.write("右側地圖：AbrahamsonEtAl2014")
    m2.to_streamlit(height=700)

