import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

def generate_boat_data(n_boats=50):
    random.seed(42)
    np.random.seed(42)

    # Indian Ocean regions: Bay of Bengal + Arabian Sea
    regions = {
        "Bay of Bengal": {"lat": (8.0, 22.0), "lon": (80.0, 92.0)},
        "Arabian Sea":   {"lat": (8.0, 22.0), "lon": (65.0, 77.0)},
        "Lakshadweep":   {"lat": (8.0, 14.0), "lon": (71.0, 74.0)},
    }

    boats = []
    for i in range(n_boats):
        region_name = random.choice(list(regions.keys()))
        region = regions[region_name]
        lat = np.random.uniform(*region["lat"])
        lon = np.random.uniform(*region["lon"])
        speed = np.random.uniform(0, 25)        # knots
        depth = np.random.uniform(10, 3000)     # meters
        wave_height = np.random.uniform(0.5, 8) # meters
        wind_speed = np.random.uniform(5, 60)   # km/h
        battery = np.random.randint(10, 100)    # %
        signal = np.random.choice(["Strong", "Moderate", "Weak"])
        last_seen = datetime.now() - timedelta(minutes=random.randint(1, 120))

        # Rule-based label for supervised learning
        if wave_height > 5.5 or wind_speed > 45 or battery < 20:
            status = "Danger"
        elif wave_height > 3.5 or wind_speed > 30 or battery < 40:
            status = "Warning"
        else:
            status = "Safe"

        boats.append({
            "boat_id": f"IND-{region_name[:3].upper()}-{1000+i}",
            "region": region_name,
            "latitude": round(lat, 4),
            "longitude": round(lon, 4),
            "speed_knots": round(speed, 1),
            "depth_m": round(depth, 1),
            "wave_height_m": round(wave_height, 2),
            "wind_speed_kmh": round(wind_speed, 1),
            "battery_pct": battery,
            "signal_strength": signal,
            "last_seen": last_seen.strftime("%Y-%m-%d %H:%M"),
            "status": status
        })

    return pd.DataFrame(boats)