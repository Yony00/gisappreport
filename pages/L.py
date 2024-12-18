import ipywidgets as widgets
import leafmap.maplibregl as leafmap
m = leafmap.Map(center=[-74.5, 40], zoom=9, style="streets")
m.clicked
output = widgets.Output()


def log_lng_lat(lng_lat):
    with output:
        output.clear_output()
        print(lng_lat.new)


m.observe(log_lng_lat, names="clicked")
output
