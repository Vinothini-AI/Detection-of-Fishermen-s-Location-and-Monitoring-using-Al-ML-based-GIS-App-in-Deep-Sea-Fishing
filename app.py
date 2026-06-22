import streamlit as st
import pandas as pd
from streamlit_folium import st_folium

from data_generator import generate_boat_data
from ml_model import train_classifier, apply_clustering
from map_builder import build_map

# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="DeepSea Watch | India",
    page_icon="🛥️",
    layout="wide"
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Rajdhani:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Rajdhani', sans-serif; }
    .metric-card {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        border-radius: 10px; padding: 16px; text-align: center;
        border: 1px solid #00e5ff33; color: white;
    }
    .danger-badge  { background:#ff1744; color:white; padding:3px 10px; border-radius:12px; font-weight:bold; }
    .warning-badge { background:#ff9100; color:white; padding:3px 10px; border-radius:12px; font-weight:bold; }
    .safe-badge    { background:#00e676; color:black; padding:3px 10px; border-radius:12px; font-weight:bold; }
    .stButton>button { background: #00e5ff; color: black; font-weight:bold; border-radius:8px; }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("## 🛰️ DeepSea Watch — AI/ML Based GIS Monitoring System")
st.markdown("**Indian Ocean Fishermen Tracking | Bay of Bengal · Arabian Sea · Lakshadweep**")
st.markdown("---")

# ── Load & Process Data ───────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = generate_boat_data(50)
    df, clf, le = train_classifier(df)
    df = apply_clustering(df)
    return df

df = load_data()

# ── Sidebar Controls ──────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🔍 Search Boat")
    search_id = st.selectbox("Select Boat ID", ["None"] + sorted(df["boat_id"].tolist()))
    highlight = None if search_id == "None" else search_id

    st.markdown("### 🗂️ Filter by Region")
    regions = ["All"] + sorted(df["region"].unique().tolist())
    selected_region = st.selectbox("Region", regions)

    st.markdown("### 🚦 Filter by Status")
    selected_status = st.multiselect("Status", ["Safe", "Warning", "Danger"],
                                     default=["Safe", "Warning", "Danger"])

    st.markdown("---")
    st.markdown("### 📊 Fleet Summary")
    total    = len(df)
    safe_n   = len(df[df["status"]=="Safe"])
    warn_n   = len(df[df["status"]=="Warning"])
    danger_n = len(df[df["status"]=="Danger"])
    st.metric("Total Boats", total)
    st.metric("✅ Safe",    safe_n)
    st.metric("⚠️ Warning", warn_n)
    st.metric("🔴 Danger",  danger_n)

# ── Filtered Data ─────────────────────────────────────────────────────────────
filtered = df.copy()
if selected_region != "All":
    filtered = filtered[filtered["region"] == selected_region]
filtered = filtered[filtered["status"].isin(selected_status)]

# ── Search Result Panel ───────────────────────────────────────────────────────
if highlight and highlight != "None":
    boat = df[df["boat_id"] == highlight].iloc[0]
    st.markdown(f"### 🎯 Boat Found: `{boat['boat_id']}`")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("📍 Latitude",  boat["latitude"])
    c2.metric("📍 Longitude", boat["longitude"])
    c3.metric("🌊 Wave Ht",   f"{boat['wave_height_m']} m")
    c4.metric("⚡ Battery",   f"{boat['battery_pct']}%")
    badge_html = f"<span class='{boat['status'].lower()}-badge'>{boat['status']}</span>"
    st.markdown(f"**ML Prediction:** {badge_html} — Confidence: {int(boat['ml_confidence']*100)}%",
                unsafe_allow_html=True)
    st.markdown(f"**Region:** {boat['region']} | **Signal:** {boat['signal_strength']} | **Last Seen:** {boat['last_seen']}")
    st.markdown("---")

# ── Map ───────────────────────────────────────────────────────────────────────
st.markdown("### 🗺️ Live Ocean Tracking Map")
m = build_map(filtered, highlight_id=highlight)
st_folium(m, width=1200, height=580)

# ── Data Table ────────────────────────────────────────────────────────────────
st.markdown("### 📋 Fleet Data Table")
display_cols = ["boat_id","region","latitude","longitude",
                "wave_height_m","wind_speed_kmh","battery_pct",
                "signal_strength","ml_predicted","ml_confidence","last_seen"]

def color_status(val):
    colors = {"Danger": "background-color:#ff174440",
              "Warning":"background-color:#ff910040",
              "Safe":   "background-color:#00e67640"}
    return colors.get(val, "")

styled = filtered[display_cols].style.applymap(color_status, subset=["ml_predicted"])
st.dataframe(styled, use_container_width=True)

# ── Feature Importance ────────────────────────────────────────────────────────
st.markdown("### 🧠 ML Model — Feature Importance")
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

features = ["speed_knots","depth_m","wave_height_m","wind_speed_kmh","battery_pct"]
le2 = LabelEncoder()
clf2 = RandomForestClassifier(n_estimators=100, random_state=42)
clf2.fit(df[features], le2.fit_transform(df["status"]))

fig, ax = plt.subplots(figsize=(7, 3))
ax.barh(features, clf2.feature_importances_, color=["#00e5ff","#0077ff","#4caf50","#ff9100","#ff1744"])
ax.set_facecolor("#0d1117"); fig.patch.set_facecolor("#0d1117")
ax.tick_params(colors="white"); ax.xaxis.label.set_color("white")
ax.set_title("Feature Importance (Random Forest)", color="white")
st.pyplot(fig)

st.markdown("---")
st.caption("🛰️ DeepSea Watch v1.0 | AI/ML GIS System | Indian Ocean Fishermen Safety")