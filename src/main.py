import os
from flask import Flask, jsonify, request
from ai.model import load_model, predict
from api.endpoints import setup_routes
from config.settings import APP_NAME, API_VERSION


def create_app():
    app = Flask(APP_NAME)
    model_path = os.getenv('MODEL_PATH', './models/synthetic_model.pkl')
    model = load_model(model_path)

    setup_routes(app, model)

    @app.route('/')
    def index():
        return f"Welcome to the {APP_NAME} API Version {API_VERSION}!"

    @app.route('/predict', methods=['POST'])
    def do_predict():
        # Example
        try:
            data = request.get_json(force=True)
            if not data:
                return jsonify({'error': 'No data provided'}), 400
            prediction = predict(model, data)
            return jsonify({
                'data': data,
                'prediction': prediction.tolist()
            })
        except Exception as e:
            app.logger.error(f"Error during prediction: {str(e)}")
            return jsonify({'error': str(e)}), 500

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
