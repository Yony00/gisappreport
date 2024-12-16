import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np
import leafmap.foliumap as leafmap
st.title("測試用頁面")

#臺南市醫院資訊
st.subheader("臺南市醫院資訊")
hos_url="https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E9%86%AB%E7%99%82%E9%99%A2%E6%89%80%E6%95%B8%E9%87%8F/%E8%87%BA%E5%8D%97%E5%B8%82%E9%86%AB%E7%99%82%E9%99%A2%E6%89%80%E9%BB%9E%E4%BD%8D%E8%B3%87%E6%96%99.csv"
hos = pd.read_csv(hos_url)
m = leafmap.Map(center=[23.15, 120.3], zoom=9)
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

#各行政區醫療院所數量&每千人擁有病床數&救護車數量
st.subheader("各行政區醫療院所數量&每千人擁有病床數&救護車數量")
hosdata_url="https://raw.githubusercontent.com/liuchia515/gisappreport/refs/heads/main/data/%E9%86%AB%E7%99%82%E9%99%A2%E6%89%80%E6%95%B8%E9%87%8F/104%E5%B9%B412%E6%9C%88%E8%A1%8C%E6%94%BF%E5%8D%80%E9%86%AB%E7%99%82%E9%99%A2%E6%89%80%E7%B5%B1%E8%A8%88_%E9%84%89%E9%8E%AE%E5%B8%82%E5%8D%80_%E8%87%BA%E5%8D%97%E5%B8%82.csv"
hosdata=pd.read_csv(hosdata_url)
st.dataframe(hosdata)


#獨居老人數、中低收入戶人數
st.subheader("獨居老人數、中低收入戶人數")
old_url="https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E7%8D%A8%E5%B1%85%E8%80%81%E4%BA%BA%E4%BA%BA%E6%95%B8/104%E5%B9%B4%E8%A1%8C%E6%94%BF%E5%8D%80%E5%B9%B4%E5%BA%95%E5%88%97%E5%86%8A%E9%9C%80%E9%97%9C%E6%87%B7%E4%B9%8B%E7%8D%A8%E5%B1%85%E8%80%81%E4%BA%BA%E4%BA%BA%E6%95%B8%E7%B5%B1%E8%A8%88_%E9%84%89%E9%8E%AE%E5%B8%82%E5%8D%80_%E8%87%BA%E5%8D%97%E5%B8%82.csv"
low_url="https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E4%B8%AD%E4%BD%8E%E6%94%B6%E5%85%A5%E6%88%B6%E7%B5%B1%E8%A8%88/104%E5%B9%B412%E6%9C%88%E8%A1%8C%E6%94%BF%E5%8D%80%E4%B8%AD%E4%BD%8E%E6%94%B6%E5%85%A5%E6%88%B6%E7%B5%B1%E8%A8%88%E6%8C%87%E6%A8%99_%E9%84%89%E9%8E%AE%E5%B8%82%E5%8D%80_%E8%87%BA%E5%8D%97%E5%B8%82.csv"


