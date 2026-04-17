import numpy as np
from src.medoid_engine import ConvergenceEngine
from src.uncertainty import EntropyManager

def run_stochastic_simulation():
    engine = ConvergenceEngine()
    manager = EntropyManager(beta_coefficient=0.42)

    print("Executing 10,000-run Monte Carlo Simulation...")
    
    # Generate high-entropy mock data (e.g., predicted asset locations or market prices)
    # Centered at 100 with high variance (noise)
    raw_outcomes = np.random.normal(loc=100, scale=25, size=10000)
    
    # Find the 'Signal' in the 'Noise' via K-Medoids
    medoid_state = engine.find_convergence_point(raw_outcomes)
    
    # Apply Entropy Adjustment to the final prediction
    final_prediction = manager.adjust_for_entropy(float(medoid_state), len(raw_outcomes))
    
    print(f"Raw Mean: {np.mean(raw_outcomes):.2f}")
    print(f"K-Medoid (True Signal): {float(medoid_state):.2f}")
    print(f"Entropy-Adjusted Prediction: {final_prediction:.2f}")
    print(f"System State: Converged & Adjusted.")

if __name__ == "__main__":
    run_stochastic_simulation()
