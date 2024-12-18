import streamlit as st
lat = st.number_input("lat",value=None,min_value=20,max_value=23)
lon = st.number_input("lat",value=None,min_value=119,max_value=121)

st.write("lat&lon:", lat,",",lon)
