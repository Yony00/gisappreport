import matplotlib.pyplot as plt
import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import pandas as pd

st.set_page_config(layout="wide")

st.sidebar.title("About")
st.sidebar.info("A Streamlit map with Socioeconomic data.")
st.title("臺南市社會經濟資料")

m = leafmap.Map(center=[23.5, 121], zoom=7)

polygon = 'https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E9%84%89%E9%8E%AE%E5%B8%82%E5%8D%80%E7%95%8C/%E9%84%89(%E9%8E%AE%E3%80%81%E5%B8%82%E3%80%81%E5%8D%80)%E7%95%8C%E7%B7%9A(TWD97%E7%B6%93%E7%B7%AF%E5%BA%A6)1131028/TOWN_MOI_1131028.shp'
gdf = gpd.read_file(polygon)
gdf = gdf[gdf['COUNTYNAME'] == '臺南市']

hospital_csv = 'https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E9%86%AB%E7%99%82%E9%99%A2%E6%89%80%E6%95%B8%E9%87%8F/104%E5%B9%B412%E6%9C%88%E8%A1%8C%E6%94%BF%E5%8D%80%E9%86%AB%E7%99%82%E9%99%A2%E6%89%80%E7%B5%B1%E8%A8%88_%E9%84%89%E9%8E%AE%E5%B8%82%E5%8D%80_%E8%87%BA%E5%8D%97%E5%B8%82.csv'
hospital_data = pd.read_csv(hospital_csv)

gdf = gdf.merge(hospital_data, left_on='TOWNNAME', right_on='TOWN', how='left')
m.add_gdf(
    gdf,
    layer_name="臺南市行政區醫院數量",
    info_mode='on_hover',
    style={"fillOpacity": 0.6, "weight": 0.5},
    color_column="醫療院所家數",
    cmap="Oranges",
)
m.to_streamlit(height=700)
