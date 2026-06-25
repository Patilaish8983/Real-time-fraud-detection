import time
import random
import datetime

def generate_transaction():
    """Generates a single random transaction dictionary."""
    locations = ["Pune", "Mumbai", "Kolkata", "Delhi", "New York"]
    
    # Normally transactions are small, but occasionally simulate a huge suspicious one
    is_suspicious = random.random() < 0.1  # 10% chance
    amount = round(random.uniform(5000, 100000), 2) if is_suspicious else round(random.uniform(10, 2000), 2)
    
    transaction = {
        "user_id": random.randint(1001, 1050),
        "amount": amount,
        "location": random.choice(locations),
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return transaction

if __name__ == "__main__":
    print("🚀 Starting Live Transaction Stream (Press Ctrl+C to stop)...")
    while True:
        tx = generate_transaction()
        print(f"📡 New Stream Event: {tx}")
        time.sleep(1) # Sends a new transaction every 1 second