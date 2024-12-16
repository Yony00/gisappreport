import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np

st.title("3D觀測值分布圖")
url="https://raw.githubusercontent.com/liuchia515/gisappreport/refs/heads/main/data/%E8%A7%80%E6%B8%AC%E5%80%BC.csv"
data = pd.read_csv(url)

data['color'] = data['震度值'].apply(lambda x: [255, 255 - x * 28, 10 + x * 25])  # 根據震度值設定顏色
data['elevation'] = data['震度值'] * 10000  # 根據震度值設定高度
data['radius'] = data['震度值']*300
required_columns = ['lat', 'lon', '震度值', '震央距(Km)', 'color', 'elevation', 'radius']
if all(col in data.columns for col in required_columns):
    # 使用 ScatterplotLayer 繪製 3D 散佈圖
    scatterplot_layer = pdk.Layer(
        'ScatterplotLayer',
        data=data,  # 資料來源
        get_position='[lon, lat]',  # 經緯度位置
        get_radius='radius',  # 根據震央距(Km)設定半徑
        get_fill_color='color',  # 使用預處理的顏色欄位
        get_elevation='震度值',  # 使用預處理的高度欄位
        auto_highlight=True,  # 高亮選中點
        extruded=True,
    )

    # 設定地圖視角
    view_state = pdk.ViewState(
        latitude=23.15,  # 設定地圖中心的緯度
        longitude=120.3,  # 設定地圖中心的經度
        zoom=9,  # 地圖縮放級別
        pitch=50,  # 地圖傾斜角度
        bearing=0  # 地圖旋轉角度
    )

    # 創建 Deck
    deck = pdk.Deck(
        layers=[scatterplot_layer],
        initial_view_state=view_state,
    )

    # 顯示地圖
    st.pydeck_chart(deck)
else:
    st.error("資料中缺少必要的欄位。")
st.markdown("所有測站資料表格")
df = pd.read_csv(url)
st.dataframe(df)
