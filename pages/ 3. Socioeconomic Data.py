import matplotlib.pyplot as plt
import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import pandas as pd

st.set_page_config(layout="wide")

st.title("臺南市社會經濟資料")
st.header("臺南市各醫院位置")
markdown = "（內容）"
st.markdown(markdown)

m = leafmap.Map(center=[23.5, 121], zoom=7)

#polygon = 'https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E9%84%89%E9%8E%AE%E5%B8%82%E5%8D%80%E7%95%8C/%E9%84%89(%E9%8E%AE%E3%80%81%E5%B8%82%E3%80%81%E5%8D%80)%E7%95%8C%E7%B7%9A(TWD97%E7%B6%93%E7%B7%AF%E5%BA%A6)1131028/TOWN_MOI_1131028.shp'
#gdf = gpd.read_file(polygon)
#gdf = gdf[gdf['COUNTYNAME'] == '臺南市']

hospital_point_csv = 'https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E8%87%BA%E5%8D%97%E5%B8%82%E9%86%AB%E7%99%82%E9%99%A2%E6%89%80%E9%BB%9E%E4%BD%8D%E8%B3%87%E6%96%99.csv'
hospital_point = pd.read_csv(hospital_point_csv)

m.add_points_from_xy(
            hospital_point,
            x='經度',
            y='緯度',
            popup=["地址"],
            icon_names=["red cross"],
            spin=True,
            add_legend=True,
            layer_name="醫院點位",
        )
m.to_streamlit(height=700)

st.header("各行政區救護車數量")
markdown = "（內容）"
st.markdown(markdown)
