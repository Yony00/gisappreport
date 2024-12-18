import folium
from streamlit_folium import st_folium

if "map_locator" not in st.session_state:
    st.session_state["map_locator"] = None
if "map_data" not in st.session_state:
    st.session_state["map_data"] = None
if "map_data" not in st.session_state:
    st.session_state["map_data"] = None
if "previous_point" not in st.session_state:
    st.session_state["previous_point"] = None


  map = folium.Map(location=[46.603354, 1.888334], zoom_start=5)  # Centered in France

  for _, row in location_counts.iterrows():
      folium.CircleMarker(
          location=(row["lat"], row["lon"]),
          radius=row["count"],  # Size relative to the count
          color="blue",
          fill=True,
          fill_color="blue",
          fill_opacity=0.6,
          tooltip=f"Location ID: {row['location_name']} - Count: {row['count']}",
      ).add_to(map)

  if (
      st.session_state["map_data"] is not None and st.session_state["map_data"]["last_clicked"] is not None   
  ):
      import logging

      logging.basicConfig(level=logging.INFO)  # You can set it to DEBUG for more detail
      logger = logging.getLogger(__name__)
      logger.info(st.session_state["map_data"])
      if st.session_state["map_data"]["last_clicked"]["lat"] != st.session_state["previous_point"]:
          clicked_lat = st.session_state["map_data"]["last_clicked"]["lat"]
          clicked_lon = st.session_state["map_data"]["last_clicked"]["lng"]
          st.session_state["map_locator"] = folium.Marker(
              location=[clicked_lat, clicked_lon],
              popup=f"New location marker at {clicked_lat} {clicked_lon}",
          )
          st.session_state["previous_point"] = clicked_lat

  if st.session_state["map_locator"] is not None:
      st.session_state["map_locator"].add_to(map)

  st.session_state["map_data"] = st_folium(map, width=700, height=500)
