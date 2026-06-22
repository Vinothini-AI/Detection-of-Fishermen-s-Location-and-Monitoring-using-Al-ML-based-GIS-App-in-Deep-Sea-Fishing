import folium
from folium.plugins import MarkerCluster, HeatMap
import pandas as pd

STATUS_COLORS = {"Safe": "green", "Warning": "orange", "Danger": "red"}
STATUS_ICONS  = {"Safe": "anchor", "Warning": "exclamation-sign", "Danger": "fire"}

def build_map(df, highlight_id=None):
    center_lat = df["latitude"].mean()
    center_lon = df["longitude"].mean()

    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=5,
        tiles="CartoDB dark_matter"
    )

    # Heatmap layer
    heat_data = df[["latitude", "longitude"]].values.tolist()
    HeatMap(heat_data, radius=18, blur=15, min_opacity=0.3).add_to(m)

    # Cluster layer
    marker_cluster = MarkerCluster(name="Boat Clusters").add_to(m)

    for _, row in df.iterrows():
        is_highlight = (row["boat_id"] == highlight_id)
        color = "blue" if is_highlight else STATUS_COLORS.get(row["status"], "gray")
        icon_name = "star" if is_highlight else STATUS_ICONS.get(row["status"], "info-sign")

        popup_html = f"""
        <div style='font-family:monospace;min-width:200px'>
        <b style='color:{color}'>{row['boat_id']}</b><br>
        📍 {row['latitude']}, {row['longitude']}<br>
        🌊 Wave: {row['wave_height_m']}m | 💨 Wind: {row['wind_speed_kmh']} km/h<br>
        ⚡ Battery: {row['battery_pct']}% | 🚀 Speed: {row['speed_knots']} kts<br>
        📶 Signal: {row['signal_strength']}<br>
        🧠 ML Status: <b>{row['ml_predicted']}</b> ({int(row['ml_confidence']*100)}%)<br>
        🕐 Last seen: {row['last_seen']}
        </div>
        """

        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=folium.Popup(popup_html, max_width=280),
            tooltip=row["boat_id"],
            icon=folium.Icon(color=color, icon=icon_name, prefix="glyphicon")
        ).add_to(marker_cluster if not is_highlight else m)

    # Draw cluster boundaries
    cluster_ids = df[df["cluster"] != -1]["cluster"].unique()
    for cid in cluster_ids:
        group = df[df["cluster"] == cid]
        center = [group["latitude"].mean(), group["longitude"].mean()]
        folium.Circle(
            location=center,
            radius=40000,
            color="cyan",
            fill=True,
            fill_opacity=0.05,
            tooltip=f"Cluster {cid} — {len(group)} boats"
        ).add_to(m)

    folium.LayerControl().add_to(m)
    return m