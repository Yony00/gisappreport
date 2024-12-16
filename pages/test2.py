import pandas as pd
import folium
from folium.plugins import HeatMap, DualMap
import streamlit as st

# 讀取數據
url = "https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E6%A8%A1%E6%93%AC%E6%95%B8%E5%80%BC_%E8%87%BA%E5%8D%97.csv"
data = pd.read_csv(url)

# 創建 DualMap 分屏地圖對象
center = [data["y"].mean(), data["x"].mean()]
dual_map = DualMap(location=center, zoom_start=8)

# 左側地圖：添加熱力圖 A
heatmap_a_data = data[["y", "x", "邏輯樹"]].values.tolist()
HeatMap(heatmap_a_data, radius=15, blur=10, max_zoom=8).add_to(dual_map.m1)

# 右側地圖：添加熱力圖 B
heatmap_b_data = data[["y", "x", "AbrahamsonEtAl2014"]].values.tolist()
HeatMap(heatmap_b_data, radius=15, blur=10, max_zoom=8).add_to(dual_map.m2)

# 將分屏地圖嵌入 Streamlit
st.components.v1.html(dual_map._repr_html_(), height=700)
