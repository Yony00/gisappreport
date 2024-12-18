import streamlit as st
import leafmap.foliumap as leafmap
import pydeck as pdk
import pandas as pd
import numpy as np
st.title("模擬值熱圖")
url="https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E6%A8%A1%E6%93%AC%E6%95%B8%E5%80%BC_%E8%87%BA%E5%8D%97.csv"
data = pd.read_csv(
    url,
    header=0,
    names=[
      "id",
      "x",
      "y",
      "邏輯樹",
      "AbrahamsonEtAl2014",
      "BooreAtkinson2008",
      "CampbellBozorgnia2008",
      "ChiouYoungs2008",
      "LinLee2008SInter",
    ],
)

selectable_columns = ['邏輯樹', 'AbrahamsonEtAl2014','BooreAtkinson2008','CampbellBozorgnia2008','ChiouYoungs2008','LinLee2008SInter']
options = st.selectbox('選擇一種GMPE呈現', selectable_columns)
if options=="邏輯樹":
    st.pydeck_chart(
        pdk.Deck(
            initial_view_state=pdk.ViewState(
                latitude=23.15,
                longitude=120.3,
                zoom=9,
                pitch=30,
            ),
            layers=[
                pdk.Layer(
                    "HeatmapLayer",
                    data=data,
                    get_position="[x, y]",
                    get_weight="邏輯樹",
                    auto_highlight=True,
                    radius_pixels=50,
                    pickable=True,
                    extruded=True,
                    opacity=0.5
                ),
            ],
        )
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')
    with col2:
        st.image("此種模擬結果相對最接近觀測值")
    with col3:
        st.write(' ')
    
if options=="AbrahamsonEtAl2014":
    st.pydeck_chart(
        pdk.Deck(
            initial_view_state=pdk.ViewState(
                latitude=23.15,
                longitude=120.3,
                zoom=9,
                pitch=30,
            ),
            layers=[
                pdk.Layer(
                    "HeatmapLayer",
                    data=data,
                    get_position="[x, y]",
                    get_weight="AbrahamsonEtAl2014",
                    auto_highlight=True,
                    radius_pixels=50,
                    pickable=True,
                    extruded=True,
                    opacity=0.5
                ),
            ],
        )
    )
if options=="BooreAtkinson2008":
    st.pydeck_chart(
        pdk.Deck(
            initial_view_state=pdk.ViewState(
                latitude=23.15,
                longitude=120.3,
                zoom=9,
                pitch=30,
            ),
            layers=[
                pdk.Layer(
                    "HeatmapLayer",
                    data=data,
                    get_position="[x, y]",
                    get_weight="BooreAtkinson2008",
                    auto_highlight=True,
                    radius_pixels=50,
                    pickable=True,
                    extruded=True,
                    opacity=0.5
                ),
            ],
        )
    )
if options=="CampbellBozorgnia2008":
    st.pydeck_chart(
        pdk.Deck(
            initial_view_state=pdk.ViewState(
                latitude=23.15,
                longitude=120.3,
                zoom=9,
                pitch=30,
            ),
            layers=[
                pdk.Layer(
                    "HeatmapLayer",
                    data=data,
                    get_position="[x, y]",
                    get_weight="CampbellBozorgnia2008",
                    auto_highlight=True,
                    radius_pixels=50,
                    pickable=True,
                    extruded=True,
                    opacity=0.5
                ),
            ],
        )
    )
if options=="ChiouYoungs2008":
    st.pydeck_chart(
        pdk.Deck(
            initial_view_state=pdk.ViewState(
                latitude=23.15,
                longitude=120.3,
                zoom=9,
                pitch=30,
            ),
            layers=[
                pdk.Layer(
                    "HeatmapLayer",
                    data=data,
                    get_position="[x, y]",
                    get_weight="ChiouYoungs2008",
                    auto_highlight=True,
                    radius_pixels=50,
                    pickable=True,
                    extruded=True,
                    opacity=0.5
                ),
            ],
        )
    )
if options=="LinLee2008SInter":
    st.pydeck_chart(
        pdk.Deck(
            initial_view_state=pdk.ViewState(
                latitude=23.15,
                longitude=120.3,
                zoom=9,
                pitch=30,
            ),
            layers=[
                pdk.Layer(
                    "HeatmapLayer",
                    data=data,
                    get_position="[x, y]",
                    get_weight="LinLee2008SInter",
                    auto_highlight=True,
                    radius_pixels=50,
                    pickable=True,
                    extruded=True,
                    opacity=0.5
                ),
            ],
        )
    )
