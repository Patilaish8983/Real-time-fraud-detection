import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import pickle

print("📦 Training anomaly detection model...")

# 1. Create a simple baseline dataset (Normal low amounts vs anomalous high amounts)
normal_transactions = np.random.normal(loc=500, scale=200, size=(1000, 1)) # standard shopping
fraud_transactions = np.random.normal(loc=75000, scale=10000, size=(50, 1)) # sudden spikes
X_train = np.vstack([normal_transactions, fraud_transactions])

# 2. Train the Isolation Forest Model
# contamination=0.05 means we expect roughly 5% anomalies
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(X_train)

# 3. Save the model locally as a file so our pipeline can use it
with open("anomaly_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained successfully and saved as 'anomaly_model.pkl'!")