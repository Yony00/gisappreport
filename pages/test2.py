import streamlit as st
import leafmap.foliumap as leafmap
import pydeck as pdk
import pandas as pd
import numpy as np

st.title("3D觀測值分布圖")
url="https://raw.githubusercontent.com/liuchia515/gisappreport/refs/heads/main/data/%E8%A7%80%E6%B8%AC%E5%80%BC.csv"
data = pd.read_csv(url)

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
                data=data,
                get_position="[lon, lat]",
                get_radius="震央距(Km)",
                get_fill_color='[255, 255 -震度 * 25, 0]',
                get_elevation='震度 * 10',
                auto_highlight=True,
            ),
        ],
    )
)
st.markdown("所有測站資料表格")
df = pd.read_csv(url)
st.dataframe(df)
