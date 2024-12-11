import streamlit as st
import leafmap.foliumap as leafmap
import pydeck as pdk
import pandas as pd
import numpy as np

st.title("3D觀測值分布圖")
url="https://raw.githubusercontent.com/liuchia515/gisappreport/refs/heads/main/data/%E8%A7%80%E6%B8%AC%E5%80%BC.csv"
data = pd.read_csv(
    url,
    header=0,
    names=[
      "測站名稱",
      "震度值",
      "震央距(Km)",
      "垂直向(gal)",
      "南北向(gal)",
      "東西向(gal)",
      "縣市",
      "鄉鎮",
      "lat",
      "lon",
    ],
)
st.pydeck_chart(
    pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=23.5,
            longitude=121,
            zoom=7,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=data,
                get_position="[lon, lat]",
                radius=2000,
                elevation_scale=100,
                elevation_range=[0, 500],
                pickable=True,
                extruded=True,

            ),
        ],
        tooltip={"text": "{測站名稱}\nearthquake intensity: {震度值}"},
    )
)
