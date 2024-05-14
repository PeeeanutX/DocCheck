import pandas as pd
import numpy as np


def generate_data(num_samples):
    np.random.seed(42)
    data = {
        'DeviceID': range(num_samples),
        'OperationTime': np.random.normal(loc=150, scale=50, size=num_samples),
        'ErrorRate': np.random.uniform(0, 0.1, size=num_samples),
        'Status': np.random.choice([0, 1], size=num_samples)
    }
    df = pd.DataFrame(data)
    return df


df = generate_data(100)
df.to_csv('data/raw/synthetic_data.csv', index=False)
