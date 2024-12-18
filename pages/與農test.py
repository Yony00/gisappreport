import folium
from streamlit_folium import st_folium
import streamlit as st
import geopandas as gpd
from shapely.geometry import Point

# 模擬設施資料（真實應使用 CSV 或資料庫）
data = {
    "設施名稱": ["設施1", "設施2", "設施3", "設施4"],
    "經度": [120.2, 120.3, 120.25, 120.4],
    "緯度": [23.0, 23.1, 23.05, 23.2]
}
facilities = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data["經度"], data["緯度"]))

# Streamlit 配置
st.title("地圖標點與範圍內設施計算")
st.write("在地圖上手動標點，計算指定半徑內的設施數量。")

# 地圖設定
m = folium.Map(location=[23.1, 120.3], zoom_start=12)

# 在地圖上顯示設施
for _, row in facilities.iterrows():
    folium.Marker(
        location=[row.geometry.y, row.geometry.x],
        popup=row["設施名稱"]
    ).add_to(m)

# 在 Streamlit 中嵌入地圖
st_map = st_folium(m, width=700, height=500)

# 用戶手動標點
if st_map and "last_clicked" in st_map:
    user_lat, user_lon = st_map["last_clicked"]["lat"], st_map["last_clicked"]["lng"]
    st.write(f"你標記的點：經度 {user_lon}, 緯度 {user_lat}")

    # 設定半徑
    radius = st.slider("選擇半徑 (公尺)", 100, 5000, 1000)

    # 繪製用戶標點與範圍
    folium.CircleMarker(
        location=[user_lat, user_lon],
        radius=10,
        color="blue",
        fill=True,
        fill_color="blue"
    ).add_to(m)

    folium.Circle(
        location=[user_lat, user_lon],
        radius=radius,
        color="red",
        fill=True,
        fill_opacity=0.2
    ).add_to(m)

    # 計算範圍內的設施數量
    user_point = Point(user_lon, user_lat)
    facilities["距離"] = facilities.geometry.distance(user_point) * 111000  # 轉換為公尺
    within_radius = facilities[facilities["距離"] <= radius]

    st.write(f"範圍內的設施數量：{len(within_radius)}")
    st.dataframe(within_radius)

    # 更新地圖
    st_folium(m, width=700, height=500)
