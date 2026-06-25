import sqlite3

def init_db():
    """Creates a local SQLite database and a table for fraud alerts."""
    conn = sqlite3.connect("fraud_alerts.db")
    cursor = conn.cursor()
    
    # Create structured table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            amount REAL,
            location TEXT,
            timestamp TEXT,
            prediction_label TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_alert(tx, label):
    """Inserts a flagged transaction anomaly into the SQL database."""
    conn = sqlite3.connect("fraud_alerts.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO alerts (user_id, amount, location, timestamp, prediction_label)
        VALUES (?, ?, ?, ?, ?)
    ''', (tx['user_id'], tx['amount'], tx['location'], tx['timestamp'], label))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("🗄️ SQL Database initialized as 'fraud_alerts.db'.")