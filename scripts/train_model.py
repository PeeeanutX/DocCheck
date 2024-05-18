import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ai.model import train_model, save_model
from src.ai.preprocess import preprocess_data

filepath = '../data/raw/synthetic_data.csv'

processed_data, encoders, scaler = preprocess_data(filepath)

features = processed_data[['OperationTime', 'ErrorRate']]
labels = processed_data['Status']

labels = labels.astype(int).apply(lambda x: 1 if x == -1 else x)

model = train_model(features, labels)

models_dir = os.path.abspath('../models')

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

model_path = os.path.join(models_dir, 'synthetic_model.pkl')
save_model(model, model_path)

print("Features type:", features.dtypes)
print("Labels type:", labels.dtype)
print("First few labels:", labels.head())
print("Unique label values before correction:", labels.unique())
