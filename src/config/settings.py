import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "DocCheck"
APP_ENV = os.getenv('APP_ENV', 'development')

DATABASE = {
    'driver': os.getenv('DB_DRIVER', 'postgres'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', 5432),
    'username': os.getenv('DB_USERNAME', 'user'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME', 'doccheck'),
}

API_VERSION = os.getenv('API_VERSION', 'v1')
API_SECRET_KEY = os.getenv('API_SECRET_KEY', '22j12o02t')

LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'DEBUG')

MODEL_PATH = os.getenv('MODEL_PATH', './models/synthetic_model.pkl')

# Path settings for data files
DATA_PATH = os.getenv('DATA_PATH', './data/')

EMAIL_SETTINGS = {
    'smtp_server': os.getenv('SMTP_SERVER', 'smtp.example.com'),
    'smtp_port': int(os.getenv('SMTP_PORT', 587)),
    'email_username': os.getenv('EMAIL_USERNAME', 'email@example.com'),
    'email_password': os.getenv('EMAIL_PASSWORD'),
    'use_tls': bool(int(os.getenv('USE_TLS', 1))),
}

EXTERNAL_API_KEY = os.getenv('EXTERNAL_API_KEY', '1234567')
EXTERNAL_API_URL = os.getenv('EXTERNAL_API_URL', 'bla@bla.de')