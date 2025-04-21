from flask import Flask, request, jsonify, send_from_directory
import pickle
import numpy as np
from study_utils import extract_features
import os

app = Flask(__name__, static_folder="../frontend")

# Load model
with open("backend/gmm_model.pkl", "rb") as f:
    gmm = pickle.load(f)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    focus_time = float(data["focus_time"])
    break_time = float(data["break_time"])
    distractions = int(data["distractions"])

    features = extract_features(focus_time, break_time, distractions)
    prediction = gmm.predict([features])[0]

    # Cluster label mapping (based on cluster means printed from train_model.py)
    cluster_map = {
    0: "Excellent focus. Keep it up!",                          # High productivity
    1: "Low productivity. Try reducing distractions.",          # Low productivity
    2: "Balanced session. Slight improvements can help."        # Medium
    }


    suggestion = cluster_map.get(prediction, "Unknown category.")
    return jsonify({
        "category": int(prediction),
        "suggestion": suggestion
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)