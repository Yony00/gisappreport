import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import folium
from math import radians, sin, cos, sqrt, atan2
st.set_page_config(layout="wide")

st.title("尋找5公里內醫療與避難設施")

firestation_csv = 'https://raw.githubusercontent.com/tim9810/gis_final_exam/refs/heads/main/%E5%8F%B0%E5%8D%97%E6%B6%88%E9%98%B2%E5%B1%80wgs84%E5%BA%A7%E6%A8%99utf.csv'
firestation = pd.read_csv(firestation_csv)
hospital_csv = 'https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E8%87%BA%E5%8D%97%E5%B8%82%E9%86%AB%E7%99%82%E9%99%A2%E6%89%80%E9%BB%9E%E4%BD%8D%E8%B3%87%E6%96%99.csv'
hospital = pd.read_csv(hospital_csv)
refuge_csv = 'https://raw.githubusercontent.com/liuchia515/gisappreport/refs/heads/main/data/%E5%8F%B0%E5%8D%97%E9%81%BF%E9%9B%A3%E6%89%80utf.csv'
refuge = pd.read_csv(refuge_csv)

firestation['經度'] = pd.to_numeric(firestation['經度'], errors='coerce')
firestation['緯度'] = pd.to_numeric(firestation['緯度'], errors='coerce')
hospital['經度'] = pd.to_numeric(hospital['經度'], errors='coerce')
hospital['緯度'] = pd.to_numeric(hospital['緯度'], errors='coerce')
refuge['經度'] = pd.to_numeric(refuge['經度'], errors='coerce')
refuge['緯度'] = pd.to_numeric(refuge['緯度'], errors='coerce')
col1,col2=st.columns(2)
with col1:
    lon = st.number_input("請填入經度", value=None, min_value=119.500, max_value=122.500)
with col2:
    lat = st.number_input("請填入緯度", value=None, min_value=22.000, max_value=24.000)

if lat is not None and lon is not None:
    radius = 5000
    def haversine(lat1, lon1, lat2, lon2):
        R = 6371000  # 地球半徑（公尺）
        phi1, phi2 = radians(lat1), radians(lat2)
        delta_phi = radians(lat2 - lat1)
        delta_lambda = radians(lon2 - lon1)
        a = sin(delta_phi/2)**2 + cos(phi1) * cos(phi2) * sin(delta_lambda/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        return R * c
    # 到輸入位置的距離
    firestation['距離(m)'] = firestation.apply(
        lambda row: haversine(lat, lon, row['緯度'], row['經度']), axis=1
    )
    hospital['距離(m)'] = hospital.apply(
        lambda row: haversine(lat, lon, row['緯度'], row['經度']), axis=1
    )
    refuge['距離(m)'] = hospital.apply(
        lambda row: haversine(lat, lon, row['緯度'], row['經度']), axis=1
    )
    # 篩選出在半徑範圍內
    nearby_firestations = firestation[firestation['距離(m)'] <= radius]
    nearby_hospitals = hospital[hospital['距離(m)'] <= radius]
    nearby_refuge = refuge[refuge['距離(m)'] <= radius]

    m = leafmap.Map(center=[lat, lon], zoom=12)
    folium.Marker(
        location=[lat, lon],
        popup=f"使用者位置\n經度: {lon}, 緯度: {lat}",
        icon=folium.Icon(color='blue', icon='star')
    ).add_to(m)

    folium.Circle(
        location=[lat, lon],
        radius=radius,
        color="cornflowerblue",
        fill=True,
        fill_opacity=0.6,
        opacity=1,
        popup="{} meters".format(radius)
    ).add_to(m)

    # 在地圖上標記範圍內的消防站
    for _, row in nearby_firestations.iterrows():
        folium.Marker(
            location=[row['緯度'], row['經度']],
            popup=row['地址'],
            icon=folium.Icon(color='red', icon='fire')
        ).add_to(m)

    for _, row in nearby_hospitals.iterrows():
        folium.Marker(
            location=[row['緯度'], row['經度']],
            popup=row['地址'],
            icon=folium.Icon(color='green', icon='plus-sign')
        ).add_to(m)
    for _, row in nearby_refuge.iterrows():
        folium.Marker(
            location=[row['緯度'], row['經度']],
            popup=row['地址'],
        ).add_to(m)

    m.to_streamlit(height=600)
    st.write("範圍內的消防站：")
    st.table(nearby_firestations[['地址', '經度', '緯度', '距離(m)']])
    st.write("範圍內的醫療院所：")
    st.table(nearby_hospitals[['機構名稱','地址', '經度', '緯度', '距離(m)']])
    st.write("範圍內的避難所：")
    st.table(nearby_refuge[['收容所名稱','地址', '經度', '緯度', '距離(m)']])

else:
    st.write("請填入有效的經緯度")



