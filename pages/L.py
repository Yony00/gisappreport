import streamlit as st

with st.popover("Open popover"):
    lat,lon = st.text_input("lat","lon")

st.write("lat&lon:", lat,lon)
