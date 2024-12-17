import matplotlib.pyplot as plt
import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import pandas as pd

st.set_page_config(layout="wide")
st.title("臺南市各消防局統計資料")
st.header("臺南市各消防局點位")
markdown = "（內容）"
st.markdown(markdown)

polygon = 'https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E9%84%89%E9%8E%AE%E5%B8%82%E5%8D%80%E7%95%8C/%E9%84%89(%E9%8E%AE%E3%80%81%E5%B8%82%E3%80%81%E5%8D%80)%E7%95%8C%E7%B7%9A(TWD97%E7%B6%93%E7%B7%AF%E5%BA%A6)1131028/TOWN_MOI_1131028.shp'
taiwan = gpd.read_file(polygon)
tainan = taiwan[taiwan['COUNTYNAME'] == '臺南市']

firestation_point_csv = 'https://raw.githubusercontent.com/tim9810/gis_final_exam/refs/heads/main/%E5%8F%B0%E5%8D%97%E6%B6%88%E9%98%B2%E5%B1%80wgs84%E5%BA%A7%E6%A8%99utf.csv'
firestation_point = pd.read_csv(firestation_point_csv)

option_list = firestation_point["行政區"].unique().tolist()
option = st.multiselect("選擇行政區", option_list)
filtered = firestation_point[firestation_point["行政區"].isin(option)]

m = leafmap.Map(center=[23, 120.3], zoom=10)
m.add_points_from_xy(
    filtered, x='經度', y='緯度',
    popup=['地址','行政區'],
    layer_name="消防局點位",
)
m.to_streamlit(height=400)



