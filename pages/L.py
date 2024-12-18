import streamlit as st
lat = st.number_input("請填入經度",value=None,min_value=119.000,max_value=121.000)
lon = st.number_input("請填入緯度",value=None,min_value=20.000,max_value=23.000)

st.write("經度:", lon,",緯度:",lat)
