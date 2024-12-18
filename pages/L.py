import streamlit as st
lat = st.number_input("lat",value=None,min_value=20.000,max_value=23.000)
lon = st.number_input("lat",value=None,min_value=119.000,max_value=121.000)

st.write("lat&lon:", lat,",",lon)
