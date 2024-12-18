import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import folium
from math import radians, sin, cos, sqrt, atan2

st.set_page_config(layout="wide")

firestation_csv = 'https://raw.githubusercontent.com/tim9810/gis_final_exam/refs/heads/main/%E5%8F%B0%E5%8D%97%E6%B6%88%E9%98%B2%E5%B1%80wgs84%E5%BA%A7%E6%A8%99utf.csv'
firestation = pd.read_csv(firestation_csv)

firestation['經度'] = pd.to_numeric(firestation['經度'], errors='coerce')
firestation['緯度'] = pd.to_numeric(firestation['緯度'], errors='coerce')

lon = st.number_input("請填入經度", value=None, min_value=119.500, max_value=122.500)
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
    # 計算消防站到輸入位置的距離
    firestation['距離'] = firestation.apply(
        lambda row: haversine(lat, lon, row['緯度'], row['經度']), axis=1
    )
    # 篩選出在半徑範圍內的消防站
    nearby_firestations = firestation[firestation['距離'] <= radius]
    m = leafmap.Map(center=[23, 120.3], zoom=10)
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
            popup=row['行政區'],
            icon=folium.Icon(color='red', icon=':fire_engine:')
        ).add_to(m)
    m.to_streamlit(height=600)
    st.write("範圍內的消防站：")
    st.dataframe(nearby_firestations[['行政區','地址', '經度', '緯度', '距離']])
else:
    st.write("請填入有效的經緯度")



