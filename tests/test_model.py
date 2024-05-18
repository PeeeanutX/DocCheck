import pytest
from src.ai.model import train_model, predict
import pandas as pd
import numpy as np


def test_train_model():
    data = pd.DataFrame({
        'feature1': np.random.rand(10),
        'feature2': np.random.rand(10)
    })
    labels = pd.Series(np.random.randint(0, 2, size=10))

    model = train_model(data, labels)

    assert model is not None


def test_predict():
    data = pd.DataFrame({
        'feature1': [0.5, 0.6],
        'feature2': [0.5, 0.6]
    })
    labels = pd.Series([0, 1])
    model = train_model(data, labels)
    predictions = predict(model, data)

    assert predictions is not None
    assert len(predictions) == 2

