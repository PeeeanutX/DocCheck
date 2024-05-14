import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder


def load_data(filepath):
    """
    Loads data from a CSV file into a pandas DataFrame.

    Parameters:
    - filepath (str): The path to the CSV file.

    Returns:
    - DataFrame: The loaded data.
    """
    return pd.read_csv(filepath)


def clean_data(data):
    """
    Performs initial cleaning operations on the data, such as removing duplicates,
    handling missing values, and potentially dropping irrelevant columns.

    Parameters:
    - data (DataFrame): The data to clean.

    Returns:
    - DataFrame: The cleaned data.
    """
    data.drop_duplicates(inplace=True)
    data.ffill(inplace=True)
    # Extended soon
    return data


def encode_features(data):
    """
    Encodes categorical features using Label Encoding or a similar method.

    Parameters:
    - data (DataFrame): The data with categorical features to encode.

    Returns:
    - DataFrame: The data with encoded features.
    """
    label_encoders = LabelEncoder()
    for column in data.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le
    return data, label_encoders


def scale_features(data):
    """
    Scales numerical features to have zero mean and unit variance.

    Parameters:
    - data (DataFrame): The data with numerical features to scale.

    Returns:
    - DataFrame: The scaled data.
    """
    scaler = StandardScaler()
    numerical_columns = data.select_dtypes(include=['float64', 'int']).columns
    data[numerical_columns] = scaler.fit_transform(data[numerical_columns])
    return data, scaler


def preprocess_data(filepath):
    """
    Full preprocessing pipeline integrating loading, cleaning, encoding, and scaling data.

    Parameters:
    - filepath (str): Path to the data file.

    Returns:
    - DataFrame: The fully preprocessed data.
    """
    data = load_data(filepath)
    data = clean_data(data)
    data, encoders = encode_features(data)
    data, scaler = scale_features(data)
    return data, encoders, scaler
