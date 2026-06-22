from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import LabelEncoder
import numpy as np

def train_classifier(df):
    features = ["speed_knots", "depth_m", "wave_height_m", "wind_speed_kmh", "battery_pct"]
    le = LabelEncoder()
    X = df[features].values
    y = le.fit_transform(df["status"])
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)
    proba = clf.predict_proba(X)
    df["ml_confidence"] = proba.max(axis=1).round(2)
    df["ml_predicted"] = le.inverse_transform(clf.predict(X))
    return df, clf, le

def apply_clustering(df):
    coords = df[["latitude", "longitude"]].values
    coords_rad = np.radians(coords)
    db = DBSCAN(eps=0.05, min_samples=2, algorithm='ball_tree', metric='haversine')
    df["cluster"] = db.fit_predict(coords_rad)
    return df