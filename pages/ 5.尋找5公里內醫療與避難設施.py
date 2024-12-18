import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import pandas as pd
import folium
from matplotlib import rcParams
from matplotlib.font_manager import FontProperties
from folium.plugins import Draw

font_path = "data/jf-openhuninn-2.0.ttf"
font = FontProperties(fname = font_path)
rcParams['font.family'] = font.get_name()

st.set_page_config(layout="wide")

lon = st.number_input("請填入經度",value=None,min_value=119,max_value=123)
lat = st.number_input("請填入緯度",value=None,min_value=22,max_value=24)

if lat == None:
    st.write("經度:", lon,",緯度:",lat)
elif lon == None:
    st.write("經度:", lon,",緯度:",lat)
else:
    m = leafmap.Map(center=[23, 120.3], zoom=10)
    radius=5000
    folium.Circle(
        location=[lat, lon],
        radius=radius,
        color="cornflowerblue",
        fill=True,
        fill_opacity=0.6,
        opacity=1,
        popup="{} meters".format(radius)
        ).add_to(m)
    m.to_streamlit(height=600)
