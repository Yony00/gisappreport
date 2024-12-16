import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np

st.title("觀測值散佈圖")
url="https://raw.githubusercontent.com/liuchia515/gisappreport/refs/heads/main/data/%E8%A7%80%E6%B8%AC%E5%80%BC.csv"
data = pd.read_csv(url)
col1,col2=st.columns([2,1])
width = None
height = 800
tiles = None

data['color'] = data['震度值'].apply(lambda x: [255, 255 - (x*x+25), 10 + (x*x)])
data['radius'] = data['震度值']*250

with col1:
    optiona = data["鄉鎮"].unique().tolist()
    optionb = st.multiselect("選擇行政區（多選）", optiona)
    if optionb:
        filtered = data[data["鄉鎮"].isin(optionb)]
        scatterplot_layer = pdk.Layer(
            'ScatterplotLayer',
            data=filtered,
            get_position='[lon, lat]',
            get_radius='radius',
            get_fill_color='color', 
            auto_highlight=True,
            pickable=True,
        )
        view_state = pdk.ViewState(
            latitude=23.15,
            longitude=120.3,
            zoom=9,
            pitch=50,
            bearing=0,
        )
        deck = pdk.Deck(
            layers=[scatterplot_layer],
            initial_view_state=view_state,
            tooltip={"text": "測站名稱: {測站名稱}\n震度: {震度值}"},
        )
        st.pydeck_chart(deck,on_select="rerun")
    else:
        scatterplot_layer = pdk.Layer(
            'ScatterplotLayer',
            data=data,
            get_position='[lon, lat]',
            get_radius='radius',
            get_fill_color='color', 
            auto_highlight=True,
            pickable=True,
        )
        view_state = pdk.ViewState(
            latitude=23.15,
            longitude=120.3,
            zoom=9,
            pitch=50,
            bearing=0,
        )
        deck = pdk.Deck(
            layers=[scatterplot_layer],
            initial_view_state=view_state,
            tooltip={"text": "測站名稱: {測站名稱}\n震度: {震度值}"},
        )
        st.pydeck_chart(deck,on_select="rerun")

with col2:
    if optionb:
        st.markdown("選取區資料表格")
        st.dataframe(filtered) 
    else:
        st.markdown("所有測站資料表格")
        df = pd.read_csv(url)
        st.dataframe(df)    
