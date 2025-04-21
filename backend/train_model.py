import numpy as np
from sklearn.mixture import GaussianMixture
import pickle
import pandas as pd
import os

# Simulated training data: [focus_time, break_time, distractions]
X = np.array([
    [50, 10, 1],
    [45, 15, 2],
    [60, 10, 0],
    [30, 20, 5],
    [35, 25, 4],
    [20, 30, 6],
])

# Fit the GMM
gmm = GaussianMixture(n_components=3, random_state=42)
gmm.fit(X)
y_pred = gmm.predict(X)

# Analyze the clusters (to know which label means what)
df = pd.DataFrame(X, columns=["focus", "break", "distractions"])
df["cluster"] = y_pred
print("Cluster Summary:")
print(df.groupby("cluster").mean())

# Save the model
model_path = os.path.join("backend", "gmm_model.pkl")
with open(model_path, "wb") as f:
    pickle.dump(gmm, f)

print("\nModel saved to:", model_path)