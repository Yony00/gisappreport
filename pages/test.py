import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np
import leafmap.foliumap as leafmap
st.title("測試用頁面")

import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.font_manager import FontProperties
import streamlit as st
import geopandas as gpd

# 設定中文字型
font_path = "data/jf-openhuninn-2.0.ttf"  # 替換為你的字型路徑
font = FontProperties(fname = font_path)
rcParams['font.family'] = font.get_name()

# 建立範例圖表
fig, ax = plt.subplots()
data = {'中西區': 15, '東區': 10, '南區': 20}
ax.bar(data.keys(), data.values())
ax.set_title("臺南市救護車分佈", fontproperties=font)
ax.set_xlabel("行政區", fontproperties=font)
ax.set_ylabel("救護車數量", fontproperties=font)

# 在 Streamlit 中顯示圖表
st.pyplot(fig)
