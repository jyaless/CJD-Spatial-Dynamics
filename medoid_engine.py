import numpy as np
from sklearn_extra.cluster import KMedoids

class ConvergenceEngine:
    """
    Isolates the 'Medoid' (most representative state) from high-entropy datasets.
    RADAR Mapping: Finding the most likely location of an asset amidst sensor noise.
    """
    def __init__(self, n_clusters: int = 1):
        self.model = KMedoids(n_clusters=n_clusters, metric='manhattan', init='k-medoids++')

    def find_convergence_point(self, simulation_results: np.ndarray) -> np.ndarray:
        """
        Runs K-Medoids clustering on 10,000+ simulation outcomes to find 
        the single most representative 'Medoid' state.
        """
        # Reshape for sklearn compatibility if 1D
        data = simulation_results.reshape(-1, 1) if simulation_results.ndim == 1 else simulation_results
        
        self.model.fit(data)
        
        # The cluster_centers_ are the actual 'Medoids' (real observed outcomes)
        return self.model.cluster_centers_[0]

    def calculate_variance_decay(self, data: np.ndarray) -> float:
        """
        Measures how quickly the simulation converges to a stable state.
        """
        return float(np.var(data))
