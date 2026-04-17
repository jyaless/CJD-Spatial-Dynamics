import asyncio
import random

async def monitor_rfid_stream():
    """
    Simulates a high-velocity RFID/Sensor stream with real-time observation.
    Uses asynchronous polling to prevent blocking the main ML thread.
    """
    sentinel = DataStreamSentinel()
    
    print("Sentinel Active: Monitoring Stream...")
    
    while True:
        # Simulate a real-time sensor reading
        raw_val = random.uniform(10, 12)
        
        # Randomly inject a 'Sensor Malfunction' (Anomaly)
        if random.random() > 0.95:
            raw_val = 50.0 
            
        if sentinel.is_anomalous(raw_val):
            print(f" ALERT: Anomaly Detected! Value: {raw_val} - Protocol: Filter & Log")
        else:
            # Process 'Clean' data
            pass
            
        await asyncio.sleep(0.5) # Poll every 500ms

if __name__ == "__main__":
    try:
        asyncio.run(monitor_rfid_stream())
    except KeyboardInterrupt:
        print("Sentinel Deactivated.")
