import matplotlib.pyplot as plt
import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import pandas as pd
from matplotlib import rcParams
from matplotlib.font_manager import FontProperties
from folium import Marker
from folium.map import Icon


font_path = "data/jf-openhuninn-2.0.ttf"
font = FontProperties(fname = font_path)
rcParams['font.family'] = font.get_name()

st.set_page_config(layout="wide")

st.title("臺南市各行政區人口統計資料")
st.header("各行政區人口密度")
markdown = "（內容）"
st.markdown(markdown)

polygon = 'https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E9%84%89%E9%8E%AE%E5%B8%82%E5%8D%80%E7%95%8C/%E9%84%89(%E9%8E%AE%E3%80%81%E5%B8%82%E3%80%81%E5%8D%80)%E7%95%8C%E7%B7%9A(TWD97%E7%B6%93%E7%B7%AF%E5%BA%A6)1131028/TOWN_MOI_1131028.shp'
taiwan = gpd.read_file(polygon)
tainan = taiwan[taiwan['COUNTYNAME'] == '臺南市']

m = leafmap.Map(center=[23, 120.3], zoom=10)
m.add_gdf(tainan, layer_name="臺南行政區", style={"color": "blue", "weight": 1.5, "fillOpacity": 0.3})
for _, row in tainan.iterrows():
    centroid = row.geometry.centroid
    Marker(
        location=[centroid.y, centroid.x], 
        icon=Icon(icon="info-sign", color="red"), 
        popup=row["TOWNNAME"],
    ).add_to(m)
m.to_streamlit(height=400)
