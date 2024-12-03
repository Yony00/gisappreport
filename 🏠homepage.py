import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")
st.title("題目")

st.header("前言")
markedown1="流程(前言)內文"
st.markdown(markedown1)

st.header("分析")
markedown2="分析內文"
st.markdown(markedown2)

st.header("分工表")
work = {
  '學號':["s1043032","s1043038","s1043048"],
  '姓名':["楊宇農","劉家芸","蔡雨潔"]
  '項目':["a","b","c"]
}
df=pd.DataFrame(work)
st.table(df)
