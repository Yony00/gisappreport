import folium

m = folium.Map(location=[-27.5717, -48.6256], zoom_start=9)

radius = 10000
folium.Circle(
    location=[-27.551667, -48.478889],
    radius=radius,
    color="black",
    weight=1,
    fill_opacity=0.6,
    opacity=1,
    fill_color="green",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius),
    tooltip="I am in meters",
).add_to(m)

m
