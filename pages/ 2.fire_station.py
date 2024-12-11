import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import pandas as pd
import requests
import rarfile  # 確保正確導入

# 設定頁面配置
st.set_page_config(layout="wide")

# 頁面標題與側邊欄資訊
st.sidebar.title("About")
st.sidebar.info("A Streamlit map with SHP and Fire Station data.")
st.title("台南市消防局點位區圖")

# 創建地圖物件
m = leafmap.Map(center=[23.5, 121], zoom=7)  # 台灣範例中心點

# 1. 下載並解壓 SHP 壓縮檔 (RAR 格式)
url = "https://raw.github.com/tim9810/gis_final_exam/blob/main/tainung/%E5%8F%B0%E5%8D%97shp.rar"  # 替換為正確的 RAR 檔案路徑
local_rar = "tainung.rar"

try:
    # 下載 RAR 檔案
    with open(local_rar, "wb") as f:
        f.write(requests.get(url).content)

    # 解壓 RAR 檔案
    with rarfile.RarFile(local_rar) as rar_ref:
        rar_ref.extractall("tainung_data")

    # 使用 Geopandas 加載 SHP
    shapefile_path = "tainung_data/tainung.shp"
    gdf = gpd.read_file(shapefile_path)
    gdf = gdf.to_crs("EPSG:4326")  # 確保座標系統為 WGS84

    # 將資料加入地圖
    m.add_gdf(gdf, layer_name="區域界線")
except Exception as e:
    st.error(f"無法讀取或處理 SHP 檔案: {e}")

# 加載消防局點位資料 (CSV 檔案)
fire_station_csv = "https://raw.githubusercontent.com/tim9810/gis_final_exam/refs/heads/main/%E5%8F%B0%E5%8D%97%E6%B6%88%E9%98%B2%E5%B1%80wgs84%E5%BA%A7%E6%A8%99utf.csv"
try:
    df = pd.read_csv(fire_station_csv)
    if {"经度", "纬度", "地址"}.issubset(df.columns):
        m.add_points_from_xy(
            df,
            x="经度",
            y="纬度",
            popup=["地址"],
            icon_names=["fire"],
            spin=True,
            add_legend=True,
            layer_name="消防局點位",
        )
    else:
        st.error("CSV 檔案中缺少 'longitude', 'latitude', 或 'name' 欄位。")
except Exception as e:
    st.error(f"無法讀取消防局點位資料: {e}")

# 在 Streamlit 中顯示地圖
m.to_streamlit(height=700)

