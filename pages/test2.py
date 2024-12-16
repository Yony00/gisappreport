import streamlit as st
import leafmap.foliumap as leafmap
import pydeck as pdk
import pandas as pd
import numpy as np

st.title("3D觀測值分布圖")
url="https://raw.githubusercontent.com/liuchia515/gisappreport/refs/heads/main/data/%E8%A7%80%E6%B8%AC%E5%80%BC.csv"
data = pd.read_csv(url)
col1,col2=st.columns([2,1])
width = None
height = 800
tiles = None

def get_color(震度值):
    if 震度值 == 4:
        return [255, 255, 204,255]  # 淡黃色
    elif 震度值 == 5:
        return [255, 255, 0,255]    # 黃色
    elif 震度值 == 6:
        return [255, 153, 51,255]   # 橙色
    else:
        return [255, 0, 0,255]      # 紅色
data['color'] = data['震度值'].apply(get_color)

st.pydeck_chart(
    pdk.Deck(
        initial_view_state=pdk.ViewState(
            latitude=23.15,
            longitude=120.3,
            zoom=9,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data,
                get_position="[lon, lat]",
                get_radius="震度值",
                auto_highlight=True,
                elevation_scale=10,
                extruded=True,
                get_fill_color="[200, 30, 0, 160]",
                radius_scale=10,
            ),
        ],
    )
)
st.markdown("所有測站資料表格")
df = pd.read_csv(url)
st.dataframe(df)
