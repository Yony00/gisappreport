import streamlit as st
import leafmap.foliumap as leafmap
import pydeck
import pandas as pd

st.title("測試頁1")
url="https://raw.githubusercontent.com/liuchia515/gisappreport/refs/heads/main/data/%E8%A7%80%E6%B8%AC%E5%80%BC.csv"
capitals = pd.read_csv(
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
point_layer = pydeck.Layer(
    "ScatterplotLayer",
    data=capitals,
    id="earthquake",
    get_position=["lon", "lat"],
    get_color="[255, 75, 75]",
    pickable=True,
    auto_highlight=True,
    get_radius="震度值",
)
view_state = pydeck.ViewState(
    latitude=23.5, longitude=121, controller=True, zoom=7, pitch=30
)

chart = pydeck.Deck(
    point_layer,
    initial_view_state=view_state,
)

st.pydeck_chart(chart, on_select="rerun", selection_mode="multi-object")
