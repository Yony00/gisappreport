import streamlit as st
import leafmap.foliumap as leafmap
import pydeck as pdk
import pandas as pd
import numpy as np

st.title("測試用頁面")
url="https://raw.githubusercontent.com/liuchia515/gisappreport/refs/heads/main/data/%E6%AD%B7%E5%8F%B2%E8%B3%87%E6%96%99.csv"
data = pd.read_csv(url)

selected= st.slider("請依照需求自行調整範圍",5.0,7.3,(5.0,7.3))
def filterdata(df,selected_range):
  lower, upper = selected_range
  return df[(df["ML"]>=lower) & (df["ML"]<=upper)]
filtered_data = filterdata(data, selected)
m=leafmap.Map(center=[23.5, 121], zoom=7)
m.add_points_from_xy(
  filtered_data,
  x="lon",
  y="lat",
  color_column="region",
  icon_names=["gear", "map", "leaf", "globe"],
  spin=True,
  add_legend=True,
)
m.to_streamlit(height=700)
st.dataframe(filtered_data)
