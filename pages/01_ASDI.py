import solara
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(
        style="liberty",
        projection="globe",
        height="750px",
        center=[-100, 40],
        zoom=2.5,
        sidebar_visible=True,
    )
    url = "https://basemap.nationalmap.gov/arcgis/services/USGSImageryOnly/MapServer/WMSServer"
    first_symbol_id = m.find_first_symbol_layer()["id"]
    m.add_wms_layer(
        url, layers="0", name="USGS.Imagery", visible=True, before_id=first_symbol_id
    )
    m.add_stac_gui()
    m.add_draw_control()
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()
