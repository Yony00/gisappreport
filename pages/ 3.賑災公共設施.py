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
# 篩選資料
if option:
    filtered = firestation_point[firestation_point["行政區"].isin(option)]
else:
    filtered = firestation_point

# 創建兩個區域，左邊放地圖，右邊放表格
col1, col2 = st.columns([3, 2])  # 調整比例，左邊地圖 3，右邊表格 2

with col1:
    st.subheader("地圖")
    m = leafmap.Map(center=[23, 120.3], zoom=10)
    m.add_points_from_xy(
        filtered, x='經度', y='緯度',
        popup=['地址', '行政區'],
        layer_name="消防局點位",
    )
    m.to_streamlit(height=500)

with col2:
    st.subheader("資料")
    if option:
        st.markdown("### 選取的行政區消防局資料")
        st.dataframe(filtered)
    else:
        st.markdown("### 所有行政區消防局資料")
        st.dataframe(firestation_point)

# 統計各行政區消防局數量並繪製長條圖(中文字體跑不出來)
st.subheader("各行政區消防局數量長條圖")
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
# 篩選資料
if option1:
    filtered1 = refuge_point[refuge_point["行政區"].isin(option1)]
else:
    filtered1 = refuge_point

# 避難所地圖與表格
tcol1, tcol2 = st.columns([3, 2])
with tcol1:
    st.subheader("地圖")
    m1 = leafmap.Map(center=[23, 120.3], zoom=10)
    m1.add_points_from_xy(
        filtered1, x='經度', y='緯度',
        popup=['收容所名稱', '地址', '行政區', '最大容納人數'],
        layer_name="避難所點位",
    )
    m1.to_streamlit(height=500)

with tcol2:
    st.subheader("資料")
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

# 添加顏色圖例，確保數值範圍正確
m2.add_colorbar(
    colors=["blue", "green", "yellow", "red"],
    vmin=refuge_point["最大容納人數"].min(),
    vmax=refuge_point["最大容納人數"].max(),
    caption="最大容納人數"
)

m2.to_streamlit(height=500)

#各行政區收容人數長條圖
st.subheader("各行政區收容人數")

# 計算各行政區的總收容人數
refuge_capacity = refuge_point.groupby('行政區')['最大容納人數'].sum().sort_values(ascending=False)

# 繪製長條圖
fig, ax = plt.subplots(figsize=(10, 6))
refuge_capacity.plot(kind='bar', color='orange', ax=ax)
plt.title("各行政區收容人數")
plt.xlabel("行政區")
plt.ylabel("最大收容人數(人)")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)


#警察局
st.subheader("警察點位資料")

police_point_csv = 'https://raw.githubusercontent.com/tim9810/gis_final_exam/refs/heads/main/PoliceAddress1_utf.csv'
police_point = pd.read_csv(police_point_csv)

option_list2 = police_point["行政區"].unique().tolist()
option2 = st.multiselect("選擇行政區", option_list2)
# 篩選資料
if option2:
    filtered2 = police_point[police_point["行政區"].isin(option2)]
else:
    filtered2 = police_point

# 創建兩個區域，左邊放地圖，右邊放表格
col3, col4 = st.columns([3, 2])  # 調整比例，左邊地圖 3，右邊表格 2

with col3:
    st.subheader("地圖")
    m3 = leafmap.Map(center=[23, 120.3], zoom=10)
    m3.add_points_from_xy(
        filtered2, x='x', y='y',
        popup=['中文單位名稱','地址', '行政區'],
        layer_name="警察局點位",
    )
    m3.to_streamlit(height=500)

with col4:
    st.subheader("資料")
    if option2:
        st.markdown("### 選取的行政區警察局資料")
        st.dataframe(filtered2)
    else:
        st.markdown("### 所有行政區警察局資料")
        st.dataframe(police_point)

# 統計各行政區警察局數量並繪製長條圖
st.subheader("各行政區警察局數量")
policetation_count = police_point['行政區'].value_counts()
fig, ax = plt.subplots(figsize=(10, 6))
policetation_count.plot(kind='bar', color='blue', ax=ax)
plt.title("各行政區警察局數量")
plt.xlabel("行政區")
plt.ylabel("警察局數量")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)
