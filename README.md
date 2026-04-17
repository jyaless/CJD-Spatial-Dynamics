# CJD-Spatial-Dynamics
High-Precision Physical Asset Mapping &amp; Predictive Modeling

CJD-Spatial-Dynamics is a domain-agnostic machine learning framework designed to ingest, harmonize, and model high-velocity telemetry data from physical environments. While utilizing MLB Statcast (GPS/Radar) data as a primary dataset, the engine is architected to solve the core challenge of Digital-to-Physical Precision: tracking, locating, and predicting the movement of "particles" (players, products, or sensors) within a defined spatial field.
RADAR Relevance
This project serves as a production-grade proxy for retail RFID/Computer Vision systems. It demonstrates the ability to:
Process high-frequency spatial coordinates in real-time.
Manage temporal data drift and sensor noise.
Apply stochastic modeling to predict physical outcomes based on momentum vectors.
Technical Architecture
1. The Ingestion & Normalization Layer
JIT API Integration: Automated ingestion of real-time spatial "Bit Tapes" (GPS coordinates and velocity vectors).
Parquet-Based Feature Store: Implemented a three-layer schema (Registry, Gold Metrics, Sabermetric) using Apache Parquet to ensure high-performance I/O and schema enforcement.
Data Integrity: Automated Float64 tensor enforcement and Mean-Imputation to stabilize high-entropy datasets.
2. The Stochastic Collision Engine (Modeling)
The core predictive engine utilizes non-linear dynamics to determine the probability of "collisions" or state changes within the spatial field.
Poisson Distribution (
λ
λ
): Used to model intensity and event frequency within specific spatial sectors.
Chiral Momentum (
z
z
): A proprietary corrective weighting logic used for regression-to-the-mean analysis on physical assets.
K-Medoids Convergence: Rather than relying on simple means, the system runs 10,000+ simulations to isolate the "Medoid" (the most representative peak probability state), effectively bypassing outliers caused by environmental noise.
3. MLOps & Observability
The Sentinel Logic: A monitoring module that detects "Temporal Displacement"—identifying when API feeds desync from the physical event clock.
Entropy Adjustment: A Beta Coefficient (0.42) applied to adjust model confidence in real-time based on historical variance.
CI/CD Logic: Strict enforcement of "Axiomatic Confirmation" before code execution, ensuring mathematical validity at every deployment stage.
Tech Stack
Languages: Python 3.12+
ML Libraries: PyTorch (Tensors), Scikit-Learn (K-Medoids), NumPy, Pandas.
Data Engineering: Apache Parquet, JSON/CSV Feature Mapping.
Infrastructure: Asynchronous API Polling, urllib3 legacy cipher overrides for secure enterprise environments.
Mathematical Axioms Applied
Stochastic Collision Frequency (
λ
λ
): 
P
(
k
 events in interval
)
=
λ
k
e
−
λ
k
!
P(k events in interval)= 
k!
λ 
k
 e 
−λ
 
​
 
Z-Score Mean Reversion: Identifying "due-ness" in physical asset performance through statistical elasticity.
Spatial Bit Tapes: Mapping the order-book depth of a physical field into a linear digital sequence for model ingestion.
How to Use
Clone the Repo: git clone https://github.com/yourusername/cjd-spatial-dynamics
Install Dependencies: pip install -r requirements.txt
Run Sentinel: python sentinel_monitor.py to begin real-time data ingestion and drift detection.
Execute Simulation: python run_simulation.py --iterations 10000 to observe K-Medoids convergence on the current spatial field.
Author
Justin Donner
Machine Learning Engineer & Spatial Data Architect
[www.linkedin.com/in/justin-donner-wa-nd-mn-ca] | [https://tinyurl.com/44fv3tdf]
"Building the future of physical-to-digital precision with a lifetime of code and a mission-driven heart."

EXAMPLE of SPATIAL MAPPING using MLB DATA:
<img width="1524" height="1222" alt="image" src="https://github.com/user-attachments/assets/2a189e9b-a586-45fd-8efa-dcecf873aa42" />
