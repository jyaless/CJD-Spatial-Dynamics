import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os

def normalize_to_parquet(raw_data: list, output_path: str):
    """
    Normalizes raw spatial telemetry into a high-performance Parquet Feature Store.
    RADAR Mapping: Optimizing feature engineering pipelines for scalability.
    """
    df = pd.DataFrame(raw_data)
    
    # Enforce Float64 for spatial precision
    spatial_cols = ['x_coord', 'y_coord', 'velocity_z']
    for col in spatial_cols:
        if col in df.columns:
            df[col] = df[col].astype('float64')

    # Convert to PyArrow Table for Registry-level schema enforcement
    table = pa.Table.from_pandas(df)
    
    if not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))
        
    pq.write_table(table, output_path)
    print(f"Feature Store Updated: {output_path}")
