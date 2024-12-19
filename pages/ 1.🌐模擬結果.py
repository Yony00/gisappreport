import streamlit as st
import leafmap.foliumap as leafmap
import pydeck as pdk
import pandas as pd
import numpy as np
st.title("模擬值熱區圖")
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
st.markdown("以下為不同衰減式模擬之地震災害模擬，請選擇一種查看各地區的災害風險模擬熱區圖")
selectable_columns = ['LinLee2008', 'AbrahamsonEtAl2014','BooreAtkinson2008','CampbellBozorgnia2008','ChiouYoungs2008']
options = st.selectbox('選擇一種衰減式呈現', selectable_columns)
if options=="LinLee2008":
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
    st.markdown(":gray-background[此種模擬結果相對最接近觀測值]")
    
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
