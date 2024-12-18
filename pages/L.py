import streamlit as st
lat = st.text_input("lat")
lon = st.text_input("lon")

st.write("lat&lon:", lat,",",lon)
