import matplotlib.pyplot as plt
import matplotlib
import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import pandas as pd
import requests

matplotlib.font_manager.fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
matplotlib.rc('font', family='Taipei Sans TC Beta')

st.set_page_config(layout="wide")
st.title("臺南市各賑災公共設施統計資料")
st.header("臺南市各消防局點位")

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
m.to_streamlit(height=500)

if option:
    st.markdown("### 選取的行政區消防局資料")
    st.dataframe(filtered)
else:
    st.markdown("### 所有行政區消防局資料")
    st.dataframe(firestation_point)

# 統計各行政區消防局數量並繪製長條圖(中文字體跑不出來)
st.subheader("各行政區消防局數量")
firestation_count = firestation_point['行政區'].value_counts()
fig, ax = plt.subplots(figsize=(10, 6))
firestation_count.plot(kind='bar', color='green', ax=ax)
plt.title("各行政區消防局數量")
plt.xlabel("行政區")
plt.ylabel("消防局數量")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

st.subheader("避難所點位資料")

refuge_point_csv = 'https://raw.githubusercontent.com/tim9810/gis_final_exam/refs/heads/main/%E5%8F%B0%E5%8D%97%E9%81%BF%E9%9B%A3%E6%89%80utf.csv'
refuge_point = pd.read_csv(refuge_point_csv)

option_list1 = refuge_point["行政區"].unique().tolist()
option1 = st.multiselect("選擇行政區", option_list1)
filtered1 = refuge_point[refuge_point["行政區"].isin(option1)]

m1 = leafmap.Map(center=[23, 120.3], zoom=10)
m1.add_points_from_xy(
    filtered1, x='經度', y='緯度',
    popup1=['收容所名稱','地址','行政區','最大容納人數'],
    layer_name1="避難所點位",
)
m1.to_streamlit(height=500)

if option1:
    st.markdown("### 選取的行政區避難所資料")
    st.dataframe(filtered1)
else:
    st.markdown("### 所有行政區避難所資料")
    st.dataframe(refuge_point)

#做收容人數熱區圖
st.subheader("收容人數熱區圖")


m2 = leafmap.Map(center=[23.1, 120.3], zoom=10)
m2.add_heatmap(
            refuge_point_csv,
            latitude="緯度",
            longitude="經度",
            value="最大容納人數",
            name='熱區圖',
            radius=20,
        )


m2.to_streamlit(height=500)
