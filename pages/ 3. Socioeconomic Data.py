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

polygon = 'https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E9%84%89%E9%8E%AE%E5%B8%82%E5%8D%80%E7%95%8C/%E9%84%89(%E9%8E%AE%E3%80%81%E5%B8%82%E3%80%81%E5%8D%80)%E7%95%8C%E7%B7%9A(TWD97%E7%B6%93%E7%B7%AF%E5%BA%A6)1131028/TOWN_MOI_1131028.shp'
taiwan = gpd.read_file(polygon)
tainan = taiwan[taiwan['COUNTYNAME'] == '臺南市']

hospital_point_csv = 'https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E8%87%BA%E5%8D%97%E5%B8%82%E9%86%AB%E7%99%82%E9%99%A2%E6%89%80%E9%BB%9E%E4%BD%8D%E8%B3%87%E6%96%99.csv'
hospital_point = pd.read_csv(hospital_point_csv)

col1,col2=st.columns([2,1])
with col1:
            option_list = hospital_point["行政區"].unique().tolist()
            option = st.multiselect("選擇行政區", option_list)
            filtered = hospital_point[hospital_point["行政區"].isin(option)]
            
            m = leafmap.Map(center=[23.2, 120.3], zoom=10)
            m.add_points_from_xy(
                        filtered,
                        x='經度',
                        y='緯度',
                        popup=['機構名稱', '行政區', '地址'],
                        icon_names=["red cross"],
                        spin=True,
                        add_legend=True,
                        layer_name="醫院點位",
                        )
m.to_streamlit(height=700)


with col2:
    if option:
        st.markdown("選取行政區醫院位置")
        st.dataframe(filtered) 
    else:
        st.markdown("所有醫院位置")
        df = pd.read_csv(url)
        st.dataframe(df)

st.header("各行政區救護車數量")
markdown = "（內容）"
st.markdown(markdown)

ambulance_csv = 'https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E8%87%BA%E5%8D%97%E5%B8%82%E6%95%91%E8%AD%B7%E8%BB%8A%E8%B3%87%E6%96%99.csv'
ambulance = pd.read_csv(ambulance_csv)
count_data = ambulance.groupby('行政區').size()
tainan['count'] = tainan['TOWNNAME'].map(count_data)
tainan['count'] = tainan['count'].fillna(0)

fig, ax = plt.subplots(figsize = (10, 6))
tainan.plot(column = 'count',cmap='OrRd', ax = ax, legend=True)
plt.axis('off')
st.pyplot(fig)
