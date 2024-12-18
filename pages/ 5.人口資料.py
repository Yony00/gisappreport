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
pop = 'data/臺南市人口資料.csv'
tainan_pop = pd.read_file(pop)

tainan = tainan.rename(columns={'TOWNNAME': '行政區'})
tainan = tainan.merge(tainan_pop, on="行政區", how="left")

tainan["人口數"] = pd.to_numeric(tainan["人口數"], errors="coerce")
tainan["面積"] = tainan.geometry.area / 1e6

tainan["人口數"] = tainan["人口數"].fillna(0)
tainan["面積"] = tainan["面積"].replace(0, pd.NA).fillna(1)

tainan["人口密度"] = tainan["人口數"] / tainan["面積"]

m = leafmap.Map(center=[23, 120.3], zoom=10)
m.add_gdf(tainan, layer_name="臺南行政區", style={"color": "blue", "weight": 1.5, "fillOpacity": 0.3})
m.to_streamlit(height=600)

col1,col2=st.columns([2,1])
with col1:
    fig, ax = plt.subplots(figsize=(8, 6))
    tainan.plot(column="人口密度", cmap="OrRd", ax=ax, legend=False)
    ax.set_title("臺南市人口密度面量圖(單位:人/平方公里)", fontproperties=font, fontsize=12)
    ax.axis('off')
    st.pyplot(fig)
with col2:
    pop_show = tainan[['行政區', '人口數', '人口密度']]
    st.dataframe(pop_show, height=600)

st.subheader("各行政區獨居老人數量長條圖")
fig, ax = plt.subplots(figsize=(8, 6))
tainan_pop[['老幼人數比例', '獨居老人人數', '低收入戶戶內人數']].plot(kind='bar', color=['green', 'blue'], ax=ax)
plt.xlabel("行政區")
plt.ylabel("人數")
plt.xticks(rotation=45)
plt.show()
