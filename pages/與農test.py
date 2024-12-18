import streamlit as st
import folium
import pandas as pd

# Initialize session state
if "markers" not in st.session_state:
    st.session_state.markers = []
    
# Create sample data for the circle markers
location_counts = pd.DataFrame({
    'location_name': ['Paris', 'Lyon', 'Marseille'],
    'lat': [48.8566, 45.7640, 43.2965],
    'lon': [2.3522, 4.8357, 5.3698],
    'count': [10, 5, 8]
})

st.title("Interactive Map Marker Creator")

# Create the base map centered on France
m = folium.Map(location=[46.603354, 1.888334], zoom_start=5)

# Add existing circle markers
for _, row in location_counts.iterrows():
    folium.CircleMarker(
        location=(row["lat"], row["lon"]),
        radius=row["count"],
        color="blue",
        fill=True,
        fill_color="blue",
        fill_opacity=0.6,
        tooltip=f"Location ID: {row['location_name']} - Count: {row['count']}",
    ).add_to(m)

# Add existing markers from session state
for marker in st.session_state.markers:
    folium.Marker(
        location=marker["location"],
        popup=marker["popup"]
    ).add_to(m)

# Get map data from user interaction
map_data = st_folium(m, width=700, height=500, key="map")

# Handle map clicks
if map_data["last_clicked"]:
    clicked_lat = map_data["last_clicked"]["lat"]
    clicked_lon = map_data["last_clicked"]["lng"]
    
    # Create a button to confirm marker placement
    if st.button("Add marker at selected location"):
        new_marker = {
            "location": [clicked_lat, clicked_lon],
            "popup": f"New location at {clicked_lat:.4f}, {clicked_lon:.4f}"
        }
        st.session_state.markers.append(new_marker)
        st.rerun()

# Display current markers information
if st.session_state.markers:
    st.write("### Current Markers:")
    for i, marker in enumerate(st.session_state.markers, 1):
        st.write(f"{i}. Location: {marker['location'][0]:.4f}, {marker['location'][1]:.4f}")

# Add a button to clear all markers
if st.button("Clear all markers"):
    st.session_state.markers = []
    st.rerun()
