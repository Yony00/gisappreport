import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import leafmap.foliumap as leafmap
import folium

st.title("測試用頁面")
url = "https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E6%A8%A1%E6%93%AC%E6%95%B8%E5%80%BC_%E8%87%BA%E5%8D%97.csv"
data = pd.read_csv(url)

# 創建地圖
m = leafmap.Map(center=[23.0, 120.0], zoom=8)

# 添加第一個熱力圖到左側
m.add_heatmap(
    data,
    latitude="y",
    longitude="x",
    value="邏輯樹",
    name="Heatmap_A",
    radius=15,
    opacity=0.7,
)

# 添加第二個熱力圖到右側
m.add_heatmap(
    data,
    latitude="y",
    longitude="x",
    value="AbrahamsonEtAl2014",
    name="Heatmap_B",
    radius=15,
    opacity=0.7,
)

# 分屏顯示
m.split_map(
    left_layer="Heatmap_A",  # 左側顯示第一個熱力圖
    right_layer="Heatmap_B",  # 右側顯示第二個熱力圖
)

# 顯示地圖於 Streamlit
m.to_streamlit(height=700)
