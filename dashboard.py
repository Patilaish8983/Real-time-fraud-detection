import streamlit as st
import sqlite3
import pandas as pd
import time

st.set_page_config(page_title="FinShield AI Dashboard", layout="wide")

st.title("🛡️ FinShield AI - Real-Time Fraud Monitor")
st.write("This dashboard queries your local structured SQL database to display live streaming anomalies detected by the ML engine.")

# Setup layout columns
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📊 Pipeline Status")
    status_placeholder = st.empty()
    metric_placeholder = st.empty()

with col2:
    st.subheader("🚨 Critical Logs (Fetched from SQLite)")
    table_placeholder = st.empty()

# Live Loop to refresh data automatically
while True:
    try:
        # Read directly from your SQLite DB
        conn = sqlite3.connect("fraud_alerts.db")
        df = pd.read_sql_query("SELECT id, user_id, amount, location, timestamp FROM alerts ORDER BY id DESC", conn)
        conn.close()
        
        # Update metrics dynamically
        status_placeholder.success("🟢 Streaming Pipeline Active")
        metric_placeholder.metric(label="Total Anomalies Blocked", value=len(df))
        
        # Update the live table view
        if not df.empty:
            table_placeholder.dataframe(df, use_container_width=True)
        else:
            table_placeholder.info("Waiting for data ingestion stream alerts...")
            
    except Exception as e:
        status_placeholder.error(f"🔴 Connection Error: {e}")
        
    time.sleep(2) # Refresh data every 2 seconds to mimic a live Kafka stream