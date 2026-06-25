# Real-time-fraud-detection Pipeline
This  is a machine learning project where the algorithm checks every transaction, detect the  anomalies and give the alert message.
Real-Time ML Anomaly & Fraud Detection Pipeline

An end-to-end, zero-latency streaming simulation and machine learning pipeline built completely from scratch in Python. AuraStream intercepts high-risk financial transactions on-the-fly using unsupervised machine learning, logs threats into a structured SQL layer, and visualizes live system health via an interactive dashboard.

---

## 🚀 The Architecture at a Glance

[📡 Live Stream Generator] ---> [🧠 Isolation Forest ML Engine]
|
+---> (If Normal)    ---> [🍏 Log Terminal Only]
|
+---> (If Anomaly)   ---> [🚨 SQL Database Alert]
|
[🎨 Streamlit Dashboard] (Polls every 2s)


## ✨ Core Features

* **Continuous Stream Simulation:** A custom-engineered event generator mimicking live transactional payloads (`User_ID`, `Amount`, `Location`, `Timestamp`).
* **Intelligent Anomaly Detection:** Powered by an unsupervised **Isolation Forest** machine learning algorithm, tracking and flagging unusual expenditure outliers with low overhead.
* **Structured Persistence Layer:** Secure relational schema implementation utilizing **SQL (SQLite)** to automatically store and quarantine flagged transactions.
* **Live Monitoring Console:** A responsive **Streamlit** dashboard that queries the SQL layer dynamically every 2 seconds to reflect system-wide threat status and historical alerts.

---

## ⚡ Why This Project is Unique

Most standard portfolio projects run statically inside isolated Jupyter Notebooks on pre-cleaned CSV files. But  this is different.

1. **Systems-First Mindset:** It bridges the gap between pure data science and software engineering by focusing on data flow, state validation, and system integration.
2. **Decoupled Architecture:** Designed to handle independent execution pipelines. The core engine remains lightweight and high-throughput, while the analytical UI layer pulls asynchronously from storage without causing resource locks.
3. **Built Completely Solo:** Developed 100% independently from scratch, proving foundational competency in software design, backend algorithms, database schema creation, and frontend deployment.

---

## 🛠️ Tech Stack & Skills Highlighted

* **Languages:** Python, SQL
* **Libraries:** Scikit-Learn, Pandas, NumPy, SQLAlchemy / SQLite3
* **Frontend UI:** Streamlit Framework
* **Concepts:** Unsupervised Learning, Structural Logging, Data Pipeline Design (ETL), Performance Optimization
