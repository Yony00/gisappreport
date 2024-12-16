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
m = leafmap.Map(center=[23.0, 120.0], zoom=8)

# 匯出第一個熱力圖為瓦片圖層 (左側底圖)
heatmap_a_tile_url = leafmap.create_heatmap_tile(
    data,
    latitude="y",
    longitude="x",
    value="邏輯樹",
    radius=15,
    opacity=0.7,
)

# 匯出第二個熱力圖為瓦片圖層 (右側底圖)
heatmap_b_tile_url = leafmap.create_heatmap_tile(
    data,
    latitude="y",
    longitude="x",
    value="AbrahamsonEtAl2014",
    radius=15,
    opacity=0.7,
)

# 設定分屏地圖
m.split_map(
    left_layer={"url": heatmap_a_tile_url, "name": "邏輯樹熱力圖"},
    right_layer={"url": heatmap_b_tile_url, "name": "AbrahamsonEtAl2014熱力圖"},
)

# 顯示地圖於 Streamlit
m.to_streamlit(height=700)
