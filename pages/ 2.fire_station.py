import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd

# 設定頁面配置
st.set_page_config(layout="wide")

# 頁面標題與側邊欄資訊
st.sidebar.title("About")
st.sidebar.info("A Streamlit map with SHP and Fire Station data.")
st.title("台南市消防局點位區圖")

# 創建地圖物件
m = leafmap.Map(center=[23.5, 121], zoom=7)  # 台灣範例中心點

# 1. 加載 GeoJSON 檔案
geojson_url = "https://raw.githubusercontent.com/tim9810/gis_final_exam/refs/heads/main/tainung/arcgis_geojeson.json"
try:
    # 將 GeoJSON 文件的 URL 傳遞給地圖
    m.add_geojson(geojson_url, layer_name="區域界線")
except Exception as e:
    st.error(f"無法讀取或處理 GeoJSON 檔案: {e}")

# 2. 加載消防局點位資料 (CSV 檔案)
fire_station_csv = "https://raw.githubusercontent.com/tim9810/gis_final_exam/refs/heads/main/%E5%8F%B0%E5%8D%97%E6%B6%88%E9%98%B2%E5%B1%80wgs84%E5%BA%A7%E6%A8%99utf.csv"
try:
    # 加載 CSV 檔案
    df = pd.read_csv(fire_station_csv)
    if {"经度", "纬度", "地址"}.issubset(df.columns):
        # 將消防局點位加入地圖
        m.add_points_from_xy(
            df,
            x="经度",
            y="纬度",
            popup=["地址"],  # 點擊顯示名稱
            icon_names=["fire"],  # 使用火焰圖示
            spin=True,  # 圖示旋轉效果
            add_legend=True,
            layer_name="消防局點位",
        )
    else:
        st.error("CSV 檔案中缺少 '经度', '纬度', 或 '地址' 欄位。")
except Exception as e:
    st.error(f"無法讀取消防局點位資料: {e}")

# 在 Streamlit 中顯示地圖
m.to_streamlit(height=700)


