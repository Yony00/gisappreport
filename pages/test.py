import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np
st.title("測試用頁面")

url = "https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E6%A8%A1%E6%93%AC%E6%95%B8%E5%80%BC_%E8%87%BA%E5%8D%97.csv"
data = pd.read_csv(
    url,
    header=0,
    names=[
        "id", "x", "y", "邏輯樹", "AbrahamsonEtAl2014", "BooreAtkinson2008", 
        "CampbellBozorgnia2008", "ChiouYoungs2008", "LinLee2008SInter"
    ]
)

# 可選擇的GMPE欄位
selectable_columns = ['邏輯樹', 'AbrahamsonEtAl2014', 'BooreAtkinson2008', 'CampbellBozorgnia2008', 'ChiouYoungs2008', 'LinLee2008SInter']
options = st.selectbox('選擇一個GMPE呈現', selectable_columns)

# 顏色映射函數
def color_map(value):
    """ 根據邏輯樹的數值來設置顏色 """
    # 假設邏輯樹值範圍在0到1之間，將其映射為顏色
    return [
        int(min(255, value * 255)),  # red channel
        0,                           # green channel
        int(min(255, 255 - value * 255)),  # blue channel
        255                          # alpha channel
    ]

# 將顏色映射應用到每個「邏輯樹」數據點
data['color'] = data['邏輯樹'].apply(color_map)

# 顯示選擇的GMPE資料
if options == "邏輯樹":
    st.pydeck_chart(
        pdk.Deck(
            initial_view_state=pdk.ViewState(
                latitude=23.15,
                longitude=120.3,
                zoom=9,
                pitch=30,
            ),
            layers=[
                pdk.Layer(
                    "HeatmapLayer",
                    data=data,
                    get_position="[x, y]",
                    get_weight="邏輯樹",  # 使用邏輯樹作為權重
                    auto_highlight=True,
                    radius_pixels=50,
                    pickable=True,
                    extruded=True,
                    opacity=0.5,
                    get_color="color"  # 使用顏色列來設定顏色
                ),
            ],
        )
    )

    # 手動添加圖例
    st.markdown("""
    ### 圖例說明：
    - **顏色映射：**
        - 藍色代表低值，紅色代表高值，顏色強度與「邏輯樹」的數值成正比。
    """)
