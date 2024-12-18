import streamlit as st
lat = st.number_input("請填入經度",value=None,min_value=119.990,max_value=120.750)
lon = st.number_input("請填入緯度",value=None,min_value=22.850,max_value=23.450)

st.write("經度:", lon,",緯度:",lat)
