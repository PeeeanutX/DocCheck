from flask import request, jsonify


def validate_json(required_keys):
    """
    Decorator to validate JSON requests in Flask routes.
    Ensures that the JSON contains all required keys.

    Parameters:
    - required_keys: List of strings representing keys that must be present in the JSOn request

    Returns:
    - Decorated Function
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = request.get_json()
            if not data:
                return jsonify({'error': 'Request must be JSON'}), 400
            missing_keys = [key for key in required_keys if key not in data]
            if missing_keys:
                return jsonify({'error': 'Missing keys in JSON data', 'missing_keys': missing_keys}), 400
            return func(*args, **kwargs)
        wrapper.__name__ = func.__name__
        return wrapper
    return decorator


def response_with_error(message, status_code=400):
    """
    Helper function to create error responses.

    Parameters:
    - message: Error message to be returned in the response
    - status_code: HTTP status code to be used for the response (default is 400)

    Returns:
    - JSON response with error message
    """
    return jsonify({'error': message}), status_code


def parse_json_data(data):
    """
    Helper function to parse JSON data and handle common data extraction.

    Parameters:
    - data: JSON object from which to extract information

    Returns:
    - Parsed data or None if there's an error
    """
    try:
        #TODO: Implement parsing logic based on app's reqs
        processed_data = data # Placeholder for actual processing logic
        return processed_data
    except Exception as e:
        return None
