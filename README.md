# 🛰️ DeepSea Watch

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green.svg)
![GIS](https://img.shields.io/badge/GIS-Folium-orange.svg)
![Status](https://img.shields.io/badge/Project-Active-success.svg)

## 🌊 Overview

DeepSea Watch is an AI/ML-powered GIS monitoring system designed to enhance maritime safety by tracking fishing boats across Indian Ocean regions. The platform provides real-time vessel monitoring, risk assessment, clustering analysis, and interactive map visualization to help identify potentially dangerous situations at sea.

The system combines Machine Learning, Geographic Information Systems (GIS), and interactive dashboards to deliver intelligent maritime monitoring and decision support.

---

## 🎯 Problem Statement

Fishing vessels operating in large ocean regions face challenges such as:

* Extreme weather conditions
* High wave activity
* Communication signal loss
* Low battery conditions
* Difficulty in monitoring vessel locations

DeepSea Watch addresses these challenges by providing an intelligent monitoring platform capable of identifying risk levels and visualizing vessel activity in real time.

---

## ✨ Key Features

### 🗺️ Interactive GIS Dashboard

* Real-time boat location visualization
* Dark-themed maritime monitoring interface
* Interactive Folium maps

### 🚢 Vessel Tracking

* Boat ID search functionality
* Live vessel status monitoring
* Region-wise filtering

### 🤖 AI-Powered Risk Prediction

* Random Forest Classification
* Automatic status prediction
* Confidence score generation

### 📊 Fleet Analytics

* Total fleet overview
* Safe vessel count
* Warning vessel count
* Danger vessel count

### 🔥 Heatmap Visualization

* Vessel density analysis
* High activity zone identification

### 📍 Cluster Detection

* DBSCAN clustering algorithm
* Detection of vessel groups
* Cluster boundary visualization

### 📈 Feature Importance Analysis

* Machine Learning feature ranking
* Risk factor interpretation

---

## 🌍 Monitored Regions

| Region        | Coverage               |
| ------------- | ---------------------- |
| Bay of Bengal | Eastern Indian Ocean   |
| Arabian Sea   | Western Indian Ocean   |
| Lakshadweep   | Southern Maritime Zone |

---

## 🧠 Machine Learning Architecture

### Classification Model

**Algorithm:** Random Forest Classifier

### Input Features

* Speed (Knots)
* Ocean Depth (Meters)
* Wave Height (Meters)
* Wind Speed (km/h)
* Battery Percentage

### Predicted Classes

* ✅ Safe
* ⚠️ Warning
* 🔴 Danger

### Confidence Score

The model generates prediction confidence values for each vessel to support decision-making.

---

## 📍 Clustering Architecture

### Algorithm

**DBSCAN (Density-Based Spatial Clustering)**

### Purpose

* Detect vessel clusters
* Identify high-density maritime activity
* Visualize grouped boat movements

---

## 🏗️ System Architecture

```text
Boat Data Generator
        │
        ▼
Data Processing Layer
        │
        ▼
Machine Learning Engine
(Random Forest)
        │
        ▼
Clustering Engine
(DBSCAN)
        │
        ▼
GIS Visualization Layer
(Folium)
        │
        ▼
Streamlit Dashboard
```

## 📂 Project Structure

```text
DeepSea-Watch/
│
├── app.py
├── data_generator.py
├── ml_model.py
├── map_builder.py
├── requirements.txt
│
└── README.md
```

## 🛠️ Technology Stack

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Random Forest
* DBSCAN

### Data Processing

* Pandas
* NumPy

### GIS & Mapping

* Folium
* Streamlit-Folium

### Dashboard

* Streamlit

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/DeepSea-Watch.git
cd DeepSea-Watch
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🚀 Usage

1. Launch the Streamlit dashboard.
2. View vessel locations on the GIS map.
3. Search vessels using Boat ID.
4. Filter by region and risk status.
5. Analyze ML predictions and confidence scores.
6. Explore heatmaps and cluster visualizations.
7. Monitor fleet statistics in real time.

---

## 📊 Risk Assessment Logic

### Danger

* Wave Height > 5.5 m
* Wind Speed > 45 km/h
* Battery < 20%

### Warning

* Wave Height > 3.5 m
* Wind Speed > 30 km/h
* Battery < 40%

### Safe

* Normal operating conditions

---

## 🔮 Future Enhancements

* Real-time AIS integration
* Satellite communication support
* Weather API integration
* SOS alert generation
* Mobile application
* Deep Learning prediction models
* Historical vessel route analysis
* Predictive maintenance monitoring

---

## 🎓 Academic Value

This project demonstrates practical applications of:

* Artificial Intelligence
* Machine Learning
* Geographic Information Systems (GIS)
* Data Visualization
* Maritime Safety Analytics
* Interactive Dashboard Development

---

## 📜 License

This project is developed for educational and research purposes.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

### 🛰️ DeepSea Watch

**AI/ML-Based GIS Monitoring System for Maritime Safety**
