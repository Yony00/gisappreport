import streamlit as st
import pandas as pd
import numpy as np
import leafmap.foliumap as leafmap
import pydeck as pdk

st.set_page_config(layout="wide")
st.title("地震災害防治分析—以美濃地震為例")

st.header("環境介紹")
st.subheader("📌歷史地震點位展示")
st.write("下方圖台為1973年1月至2024年9月為止規模5以上的地震震央點位及相關資料")
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

st.subheader("🗺️2016.02.06美濃地震觀測值散佈圖")
st.write("下圖為美濃地震觀測值散佈圖之互動式地圖，可以照行政區找尋特定測站之資料（多選）")
url="https://raw.githubusercontent.com/liuchia515/gisappreport/refs/heads/main/data/%E8%A7%80%E6%B8%AC%E5%80%BC.csv"
data = pd.read_csv(url)
col1,col2=st.columns([2,1])
width = None
height = 800
tiles = None

data['color'] = data['震度值'].apply(lambda x: [255-(x*x), 255 - (x*x*5), x*x*5])
data['radius'] = data['震度值'].apply(lambda x:x*x*x*10)

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
