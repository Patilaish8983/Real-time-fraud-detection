import time
import pickle
import numpy as np
from streamer import generate_transaction
from database import insert_alert, init_db

# 1. Initialize DB and load the pre-trained ML model
init_db()
with open("anomaly_model.pkl", "rb") as f:
    model = pickle.load(f)

print("⚙️ Pipeline Engine Active. Waiting for streaming data...")

# 2. Infinite loop acting as our processing pipeline engine
try:
    while True:
        # Ingest from stream
        tx = generate_transaction()
        
        # Format feature data for the ML model (expects a 2D array)
        amount_feature = np.array([[tx["amount"]]])
        
        # Predict: Isolation forest outputs -1 for anomalies and 1 for normal data
        prediction = model.predict(amount_feature)[0]
        
        if prediction == -1:
            print(f"🚨 ALERT! Anomaly Detected: User {tx['user_id']} spent ₹{tx['amount']} at {tx['location']}!")
            # Save streaming alert to database
            insert_alert(tx, "CRITICAL_ANOMALY")
        else:
            print(f"🍏 Normal Transaction: User {tx['user_id']} spent ₹{tx['amount']}.")
            
        time.sleep(1) # Process incoming stream events every second

except KeyboardInterrupt:
    print("\n🛑 Pipeline gracefully stopped.")