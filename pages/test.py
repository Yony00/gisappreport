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
polygon = 'https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E9%84%89%E9%8E%AE%E5%B8%82%E5%8D%80%E7%95%8C/%E9%84%89(%E9%8E%AE%E3%80%81%E5%B8%82%E3%80%81%E5%8D%80)%E7%95%8C%E7%B7%9A(TWD97%E7%B6%93%E7%B7%AF%E5%BA%A6)1131028/TOWN_MOI_1131028.shp'
gdf = gpd.read_file(polygon)
gdf = gdf[gdf['COUNTYNAME'] == '臺南市']
url="https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E6%A8%A1%E6%93%AC%E6%95%B8%E5%80%BC_%E8%87%BA%E5%8D%97.csv"
data = pd.read_csv(url)

selectable_columns = ['邏輯樹', 'AbrahamsonEtAl2014','BooreAtkinson2008','CampbellBozorgnia2008','ChiouYoungs2008','LinLee2008SInter']
options = st.selectbox('選擇一個GMPE呈現', selectable_columns)
a= m.add_heatmap(
    data,
    latitude="y",
    longitude="x",
    value="邏輯樹",
    name="邏輯樹",
    radius=15,
    pacity=0.7,
)
b= m.add_heatmap(
    data,
    latitude="y",
    longitude="x",
    value="AbrahamsonEtAl2014",
    name="AbrahamsonEtAl2014",
    radius=15,
    pacity=0.7,
)

if options=="邏輯樹":
    url="https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E6%A8%A1%E6%93%AC%E6%95%B8%E5%80%BC_%E8%87%BA%E5%8D%97.csv"
    data = pd.read_csv(url)
    m.add_gdf(
        gdf,
        layer_name="行政區界",
        info_mode="on_hover", 
    )
    m.add_heatmap(
        data,
        latitude="y",
        longitude="x",
        value="邏輯樹",
        name="邏輯樹",
        radius=15,
        pacity=0.7,
    )
    m.to_streamlit(height=700)

if options=="AbrahamsonEtAl2014":
    url="https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E6%A8%A1%E6%93%AC%E6%95%B8%E5%80%BC_%E8%87%BA%E5%8D%97.csv"
    data = pd.read_csv(url)
    m.add_gdf(
        gdf,
        layer_name="行政區界",
        info_mode="on_hover", 
    )
    m.split_map(
        left_layer="a",right_layer="b",
    )
    m.to_streamlit(height=700)

if options=="BooreAtkinson2008":
    url="https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E6%A8%A1%E6%93%AC%E6%95%B8%E5%80%BC_%E8%87%BA%E5%8D%97.csv"
    data = pd.read_csv(url)
    m.add_gdf(
        gdf,
        layer_name="行政區界",
        info_mode="on_hover", 
    )
    m.add_heatmap(
        data,
        latitude="y",
        longitude="x",
        value="BooreAtkinson2008",
        name="BooreAtkinson2008",
        radius=15,
        pacity=0.7,
    )
    m.to_streamlit(height=700)

if options=="CampbellBozorgnia2008":
    url="https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E6%A8%A1%E6%93%AC%E6%95%B8%E5%80%BC_%E8%87%BA%E5%8D%97.csv"
    data = pd.read_csv(url)
    m.add_gdf(
        gdf,
        layer_name="行政區界",
        info_mode="on_hover", 
    )
    m.add_heatmap(
        data,
        latitude="y",
        longitude="x",
        value="CampbellBozorgnia2008",
        name="CampbellBozorgnia2008",
        radius=15,
        pacity=0.7,
    )
    m.to_streamlit(height=700)

if options=="ChiouYoungs2008":
    url="https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E6%A8%A1%E6%93%AC%E6%95%B8%E5%80%BC_%E8%87%BA%E5%8D%97.csv"
    data = pd.read_csv(url)
    m.add_gdf(
        gdf,
        layer_name="行政區界",
        info_mode="on_hover", 
    )
    m.add_heatmap(
        data,
        latitude="y",
        longitude="x",
        value="ChiouYoungs2008",
        name="ChiouYoungs2008",
        radius=15,
        pacity=0.7,
    )
    m.to_streamlit(height=700)

if options=="LinLee2008SInter":
    url="https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E6%A8%A1%E6%93%AC%E6%95%B8%E5%80%BC_%E8%87%BA%E5%8D%97.csv"
    data = pd.read_csv(url)
    m.add_gdf(
        gdf,
        layer_name="行政區界",
        info_mode="on_hover", 
    )
    m.add_heatmap(
        data,
        latitude="y",
        longitude="x",
        value="LinLee2008SInter",
        name="LinLee2008SInter",
        radius=15,
        pacity=0.7,
    )
    m.to_streamlit(height=700)

