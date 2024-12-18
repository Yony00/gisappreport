import streamlit as st
import pandas as pd
import numpy as np
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")
st.title("地震災害防治分析—以美濃地震為例")

st.header("前言")
markedown1="流程(前言)內文"
st.markdown(markedown1)

st.header("分析")
markedown2="分析內文"
st.markdown(markedown2)

st.header("分工表")
work = {
  '學號':["s1043032","s1043038","s1043048"],
  '姓名':["楊宇農","劉家芸","蔡雨潔"],
  '項目':["賑災公共設施","環境介紹、模擬結果","醫療資源"],
}
df=pd.DataFrame(work)
st.table(df)

st.header("歷史地震點位展示")
st.write("下方圖台為1973~2024年9月為止規模5以上的地震震央點位")
url="https://raw.githubusercontent.com/liuchia515/gisappreport/refs/heads/main/data/%E6%AD%B7%E5%8F%B2%E8%B3%87%E6%96%99.csv"
data = pd.read_csv(url)

cola,colb=st.columns([2,1])
width = None
height = 800
tiles = None

with cola:
  selected= st.slider("請依照需求自行調整範圍",5.0,7.3,(5.0,7.3))
  def filterdata(df,selected_range):
    lower, upper = selected_range
    return df[(df["ML"]>=lower) & (df["ML"]<=upper)]
  filtered_data = filterdata(data, selected)
  st.map(filtered_data, size=20, color="#0044ff")
with colb:
  st.write("選定規模範圍內地震資料")
  st.dataframe(filtered_data)
