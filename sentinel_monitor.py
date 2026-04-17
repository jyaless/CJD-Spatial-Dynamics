import numpy as np
from collections import deque

class DataStreamSentinel:
    """
    Monitors data streams for statistical drift and 'Opening Bell Noise.'
    """
    def __init__(self, window_size: int = 50, threshold_z: float = 3.0):
        self.buffer = deque(maxlen=window_size)
        self.threshold = threshold_z

    def is_anomalous(self, new_value: float) -> bool:
        """
        Detects spikes using a rolling Z-score. 
        Crucial for filtering sensor noise in retail environments.
        """
        if len(self.buffer) < 2:
            self.buffer.append(new_value)
            return False
            
        mean = np.mean(self.buffer)
        std = np.std(self.buffer)
        
        if std == 0: return False
        
        z_score = abs((new_value - mean) / std)
        self.buffer.append(new_value)
        
        # If z_score exceeds threshold, trigger 'Drift Alert'
        return z_score > self.threshold
