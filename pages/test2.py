import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import leafmap.foliumap as leafmap
import folium

st.title("測試用頁面")
m = leafmap.Map(center=[23.5, 121], zoom=7)
url="https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E6%A8%A1%E6%93%AC%E6%95%B8%E5%80%BC_%E8%87%BA%E5%8D%97.csv"
data = pd.read_csv(url)

selectable_columns = ['邏輯樹', 'AbrahamsonEtAl2014','BooreAtkinson2008','CampbellBozorgnia2008','ChiouYoungs2008','LinLee2008SInter']
options = st.selectbox('選擇一個GMPE呈現', selectable_columns)

m.add_heatmap(
    data,
    latitude="y",
    longitude="x",
    value="邏輯樹",
    name="邏輯樹",
    radius=15,
    pacity=0.7,
)
m.add_heatmap(
    data,
    latitude="y",
    longitude="x",
    value="AbrahamsonEtAl2014",
    name="AbrahamsonEtAl2014",
    radius=15,
    pacity=0.7,
)

if options=="邏輯樹":
    left_layer, right_layer = "邏輯樹", "AbrahamsonEtAl2014"
elif options=="AbrahamsonEtAl2014":
    left_layer, right_layer = "AbrahamsonEtAl2014", "邏輯樹"
m.split_map(left_layer=left_layer,right_layer=right_layer)
m.to_streamlit(height=700)
