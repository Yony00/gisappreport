import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np
import geopandas as gpd
import leafmap.foliumap as leafmap
import folium
from folium.plugins import HeatMap

st.title("測試用頁面")
url = "https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E6%A8%A1%E6%93%AC%E6%95%B8%E5%80%BC_%E8%87%BA%E5%8D%97.csv"
data = pd.read_csv(url)


center = [data["y"].mean(), data["x"].mean()]
folium_map_a = folium.Map(location=center, zoom_start=8)
folium_map_b = folium.Map(location=center, zoom_start=8)

# 添加熱力圖到 folium 地圖 A
heatmap_a_data = data[["y", "x", "邏輯樹"]].values.tolist()
HeatMap(heatmap_a_data, radius=15, blur=10, max_zoom=8).add_to(folium_map_a)

# 添加熱力圖到 folium 地圖 B
heatmap_b_data = data[["y", "x", "AbrahamsonEtAl2014"]].values.tolist()
HeatMap(heatmap_b_data, radius=15, blur=10, max_zoom=8).add_to(folium_map_b)

# 使用 leafmap 將分屏顯示 folium 地圖
m = leafmap.Map(center=center, zoom=8)
m.split_map(
    left_layer={"url": folium_map_a._repr_html_(), "name": "邏輯樹熱力圖"},
    right_layer={"url": folium_map_b._repr_html_(), "name": "AbrahamsonEtAl2014熱力圖"},
)

# 顯示地圖於 Streamlit
m.to_streamlit(height=700)
