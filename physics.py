import numpy as np
from scipy.stats import poisson

class SpatialPhysicsEngine:
    """
    Engine for calculating momentum vectors and collision probabilities 
    for physical assets in a coordinate field.
    """
    def __init__(self, entropy_coefficient: float = 0.42):
        self.beta = entropy_coefficient

    def calculate_chiral_momentum(self, positions: np.ndarray) -> float:
        """
        Calculates the 'z-score' of a particle's trajectory to determine 
        elasticity and mean reversion (due-ness).
        """
        mean_pos = np.mean(positions)
        std_pos = np.std(positions)
        if std_pos == 0: return 0.0
        
        # Chiral Tension (z)
        z_score = (positions[-1] - mean_pos) / std_pos
        return float(z_score)

    def collision_probability(self, intensity_lambda: float, events: int) -> float:
        """
        Uses Poisson Distribution to model the likelihood of a 'collision' 
        (e.g., RFID tag crossing a portal or ball-to-bat contact).
        """
        # P(k events in interval) = (lambda^k * e^-lambda) / k!
        prob = poisson.pmf(events, intensity_lambda)
        return float(prob * (1 - self.beta)) # Adjusted for environmental entropy

# Example usage for README/Notebook
if __name__ == "__main__":
    engine = SpatialPhysicsEngine()
    # Simulating a trajectory of a physical asset
    trajectory = np.array([10.2, 10.5, 11.0, 10.8, 12.5]) 
    print(f"Chiral Tension (z): {engine.calculate_chiral_momentum(trajectory)}")
