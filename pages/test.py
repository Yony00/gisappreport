import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np
import leafmap.foliumap as leafmap
st.title("測試用頁面")

#臺南市醫院資訊
hos_url="https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E9%86%AB%E7%99%82%E9%99%A2%E6%89%80%E6%95%B8%E9%87%8F/%E8%87%BA%E5%8D%97%E5%B8%82%E9%86%AB%E7%99%82%E9%99%A2%E6%89%80%E9%BB%9E%E4%BD%8D%E8%B3%87%E6%96%99.csv"
hos = pd.read_csv(hos_url)
m = leafmap.Map(center=[23.5, 121], zoom=7)
m.add_points_from_xy(
  hos,
  x="經度",
  y="緯度",
  spin=True,
  add_legend=True,
  layer_name="臺南市醫院資訊",
)
m.to_streamlit(height=700)
st.dataframe(hos)
