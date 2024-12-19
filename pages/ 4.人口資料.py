import matplotlib.pyplot as plt
import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import pandas as pd
from matplotlib import rcParams
from matplotlib.font_manager import FontProperties
import requests

font_path = "data/jf-openhuninn-2.0.ttf"
font = FontProperties(fname = font_path)
rcParams['font.family'] = font.get_name()

#matplotlib.font_manager.fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
#matplotlib.rc('font', family='Taipei Sans TC Beta')

st.set_page_config(layout="wide")

st.title("臺南市各行政區人口統計資料")
st.header("各行政區人口")
markdown1 = """
將游標移動至地圖上各行政區，可獲得行政區人口資料，如：各行政區戶、人口數、男性人口數、女性人口數、0-14歲人口數、15-64歲人口數、65歲以上人口數、老幼人數比例、獨居老人人數、低收入戶戶內人數等。
"""
st.markdown(markdown1)

polygon = 'https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E9%84%89%E9%8E%AE%E5%B8%82%E5%8D%80%E7%95%8C/%E9%84%89(%E9%8E%AE%E3%80%81%E5%B8%82%E3%80%81%E5%8D%80)%E7%95%8C%E7%B7%9A(TWD97%E7%B6%93%E7%B7%AF%E5%BA%A6)1131028/TOWN_MOI_1131028.shp'
taiwan = gpd.read_file(polygon)
tainan = taiwan[taiwan['COUNTYNAME'] == '臺南市']
pop = 'data/臺南市人口資料pro.csv'
tainan_pop = pd.read_csv(pop)

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

markdown2 = """
下方是台南市各行政區在地震時較須受到幫助的弱勢群體比例與人數長條圖。
"""
st.markdown(markdown2)

st.subheader("各行政區老幼人數比例長條圖")
fig, ax = plt.subplots(figsize=(6, 4))
tainan_pop.set_index('行政區', inplace=True)
sorted_data_1 = tainan_pop.sort_values(by='老幼人數比例', ascending=False)
sorted_data_1[['老幼人數比例']].plot(kind='bar', color='lightgreen', ax=ax, legend=False)
ax.legend(prop=font, fontsize=8)
plt.xlabel("行政區", fontproperties=font, fontsize=8)
plt.ylabel("比例", fontproperties=font, fontsize=8)
plt.xticks(fontproperties=font, fontsize=8, rotation=45)
plt.yticks(fontproperties=font, fontsize=8, rotation=45)
st.pyplot(fig)

tainan_pop_2 = pd.read_csv(pop)
option_list = tainan_pop_2["行政區"].unique().tolist()
option = st.multiselect("選擇行政區", option_list)
filtered = tainan_pop_2[tainan_pop_2["行政區"].isin(option)]
if option:
    for index, row in filtered.iterrows():
        labels = ["幼年人口", "壯年人口", "老年人口"]
        sizes = [row["幼年人口比例"], row["壯年人口比例"], row["老年人口比例"]]
        colors = ["#FFD700", "#FF8C00", "#8B0000"]

        fig, ax = plt.subplots(figsize=(4, 3))
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        ax.set_title(f"{row['行政區']} 幼年、壯年、老年人口比例", fontsize=14, fontproperties=font)
        st.pyplot(fig)
else:
    st.markdown("### 請選擇至少一個行政區")

st.subheader("各行政區獨居老人人數長條圖")
fig, ax = plt.subplots(figsize=(6, 4))
sorted_data_2 = tainan_pop.sort_values(by='獨居老人人數', ascending=False)
sorted_data_2[['獨居老人人數']].plot(kind='bar', color='lightblue', ax=ax, legend=False)
ax.legend(prop=font, fontsize=8)
plt.xlabel("行政區", fontproperties=font, fontsize=8)
plt.ylabel("人數", fontproperties=font, fontsize=8)
plt.xticks(fontproperties=font, fontsize=8, rotation=45)
plt.yticks(fontproperties=font, fontsize=8, rotation=45)
st.pyplot(fig)

st.subheader("各行政區低收入戶戶內人數長條圖")
fig, ax = plt.subplots(figsize=(6, 4))
sorted_data_3 = tainan_pop.sort_values(by='低收入戶戶內人數', ascending=False)
sorted_data_3[['低收入戶戶內人數']].plot(kind='bar', color='lightpink', ax=ax, legend=False)
ax.legend(prop=font, fontsize=8)
plt.xlabel("行政區", fontproperties=font, fontsize=8)
plt.ylabel("人數", fontproperties=font, fontsize=8)
plt.xticks(fontproperties=font, fontsize=8, rotation=45)
plt.yticks(fontproperties=font, fontsize=8, rotation=45)
st.pyplot(fig)
