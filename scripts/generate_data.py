import os.path

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


base_dir = os.path.abspath('DocCheck/data/raw')

if not os.path.exists(base_dir):
    os.makedirs(base_dir)

df = generate_data(100)

file_path = os.path.join(base_dir, 'synthetic_data.csv')
df.to_csv(file_path, index=False)
