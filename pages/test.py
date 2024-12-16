import streamlit as st
import leafmap.foliumap as leafmap
import pydeck as pdk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd

st.title("測試用頁面")
m = leafmap.Map(center=[23.5, 121], zoom=7)

polygon = 'https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E9%84%89%E9%8E%AE%E5%B8%82%E5%8D%80%E7%95%8C/%E9%84%89(%E9%8E%AE%E3%80%81%E5%B8%82%E3%80%81%E5%8D%80)%E7%95%8C%E7%B7%9A(TWD97%E7%B6%93%E7%B7%AF%E5%BA%A6)1131028/TOWN_MOI_1131028.shp'
gdf = gpd.read_file(polygon)
gdf = gdf[gdf['COUNTYNAME'] == '臺南市']

m.add_gdf(
    gdf,
    layer_name="行政區界",
    info_mode="on_hover", 
)

m.to_streamlit(height=700)
