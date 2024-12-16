import streamlit as st
import leafmap.foliumap as leafmap
import pydeck as pdk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd

# 創建地圖
m = leafmap.Map(center=[37.7749, -122.4194], zoom=10)

# 示例數據
data = pd.DataFrame({
    "lat": [37.7749, 34.0522, 40.7128],
    "lon": [-122.4194, -118.2437, -74.0060],
    "weight": [0.8, 0.6, 0.9]
})

# 添加熱力圖
m.add_heatmap(data, lat="lat", lon="lon", value="weight")
m.to_streamlit()



st.title("測試用頁面")
m = leafmap.Map(center=[23.5, 121], zoom=7)

polygon = 'https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E9%84%89%E9%8E%AE%E5%B8%82%E5%8D%80%E7%95%8C/%E9%84%89(%E9%8E%AE%E3%80%81%E5%B8%82%E3%80%81%E5%8D%80)%E7%95%8C%E7%B7%9A(TWD97%E7%B6%93%E7%B7%AF%E5%BA%A6)1131028/TOWN_MOI_1131028.shp'
gdf = gpd.read_file(polygon)
gdf = gdf[gdf['COUNTYNAME'] == '臺南市']

url="https://raw.githubusercontent.com/liuchia515/gisappreport/refs/heads/main/data/%E6%A8%A1%E6%93%AC%E6%95%B8%E5%80%BC.csv"
data = pd.read_csv(url)
selectable_columns = ['邏輯樹', 'AbrahamsonEtAl2014','BooreAtkinson2008','CampbellBozorgnia2008','ChiouYoungs2008','LinLee2008SInter']
options = st.selectbox('選擇一個GMPE呈現', selectable_columns)

if options=="邏輯樹":
    url="https://raw.githubusercontent.com/liuchia515/gisappreport/refs/heads/main/data/%E6%A8%A1%E6%93%AC%E6%95%B8%E5%80%BC.csv"
    m.add_gdf(
        gdf,
        layer_name="行政區界",
        info_mode="on_hover", 
    )
    m.add_heatmap(
        url,
        latitude="x",
        lontitude="y",
        value="邏輯樹",
        name="邏輯樹",
        radius=100,
    )
    m.to_streamlit(height=700)

