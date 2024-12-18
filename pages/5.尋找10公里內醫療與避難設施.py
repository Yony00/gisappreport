import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import pandas as pd
import folium
from matplotlib import rcParams
from matplotlib.font_manager import FontProperties

font_path = "data/jf-openhuninn-2.0.ttf"
font = FontProperties(fname = font_path)
rcParams['font.family'] = font.get_name()

st.set_page_config(layout="wide")
