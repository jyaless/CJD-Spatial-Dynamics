import math

class EntropyManager:
    """
    Applies corrective weighting to models based on environmental uncertainty.
    """
    def __init__(self, beta_coefficient: float = 0.42):
        self.beta = beta_coefficient

    def adjust_for_entropy(self, raw_probability: float, sample_size: int) -> float:
        """
        Adjusts prediction confidence based on 'Noise' levels.
        Formula: P_adj = P * (1 - (Beta / sqrt(N)))
        """
        if sample_size == 0: return 0.0
        
        # Penalize confidence when sample size is low or entropy (beta) is high
        penalty = self.beta / math.sqrt(sample_size)
        adjusted_p = raw_probability * (1 - penalty)
        
        return max(0.0, min(1.0, adjusted_p))

    def calculate_shannon_entropy(self, probabilities: list) -> float:
        """
        Standard Shannon Entropy calculation to measure dataset 'chaos'.
        """
        return -sum(p * math.log2(p) for p in probabilities if p > 0)
