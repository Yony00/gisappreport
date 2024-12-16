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
      "鄉鎮",
      "lat",
      "lon",
    ],
)
col1,col2=st.columns([2,1])
width = None
height = 800
tiles = None

with col1:
    optiona = data["鄉鎮"].unique().tolist()
    optionb = st.multiselect("選擇行政區（多選）", optiona)
    if optionb:
        filtered = data[data["鄉鎮"].isin(optionb)]
        st.pydeck_chart(
            pdk.Deck(
                initial_view_state=pdk.ViewState(
                    latitude=23.1,
                    longitude=120.1,
                    zoom=9,
                    pitch=50,
                ),
                layers=[
                    pdk.Layer(
                        "HexagonLayer",
                        data=filtered,
                        get_position="[lon, lat]",
                        get_radius="震度值",
                        auto_highlight=True,
                        elevation_scale=10,
                        pickable=True,
                        extruded=True,
                        get_weight="震度值",
                    ),
                ],
            )
        )
    else:
        st.pydeck_chart(
            pdk.Deck(
                initial_view_state=pdk.ViewState(
                    latitude=23.15,
                    longitude=120.2,
                    zoom=9,
                    pitch=50,
                ),
                layers=[
                    pdk.Layer(
                        "HexagonLayer",
                        data=data,
                        get_position="[lon, lat]",
                        get_radius="震度值",
                        auto_highlight=True,
                        elevation_scale=10,
                        pickable=True,
                        extruded=True,
                        get_weight="震度值",                        
                    ),
                ],
            )
        )
with col2:
    if optionb:
        st.markdown("選取區資料表格")
        st.dataframe(filtered) 
    else:
        st.markdown("所有測站資料表格")
        df = pd.read_csv(url)
        st.dataframe(df)
