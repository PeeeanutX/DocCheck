import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def train_model(data, labels):
    """
    Trains a machine learning model and returns the trained model.

    Parameters:
    - data (DataFrame): The features used for training the model.
    - labels (Series): The target labels.

    Returns:
    - model: The trained machine learning model.
    """
    model = RandomForestClassifier(n_estimators=100)
    model.fit(data, labels)
    return model


def save_model(model, path):
    """
    Saves a trained machine learning model to a specified path.

    Parameters:
    - model: The machine learning model to save
    - path (str): The file path where the model should be saved.
    """
    with open(path, 'wb') as file:
        pickle.dump(model, file)


def load_model(path):
    """
    Loads a machine learning model from a specified path.

    Parameters:
    - path (str): The file path where the model is stored.

    Returns:
    - model: The loaded machine learning model.
    """
    with open(path, 'rb') as file:
        model = pickle.load(file)
    return model


def predict(model, data):
    """
    Uses a trained machine learning model to make predictions based on the input data.

    Parameters:
    - model: The machine learning model to use for predictions.
    - data (DataFrame): The data to predict on.

    Returns:
    - predictions: The predicted labels.
    """
    features_df = pd.DataFrame([data])

    predictions = model.predict(features_df)
    return predictions
