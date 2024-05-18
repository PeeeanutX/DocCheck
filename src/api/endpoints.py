import pandas as pd
from flask import request, jsonify


def setup_routes(app, model):
    @app.route('/status', methods=['GET'])
    def get_status():
        # Dummy status check endpoint
        return jsonify({
            'status': 'running',
            'message': 'System is operational'
        })

    @app.route('/summary', methods=['POST'])
    def generate_summary():
        try:
            data_df = load_csv_data('data/raw/synthetic_data.csv')
            additional_data = request.get_json()
            if additional_data and isinstance(additional_data, list):
                additional_df = pd.DataFrame(additional_data)
                if not additional_df.empty:
                    data_df = pd.concat([data_df, additional_df], ignore_index=True, sort=False)

            summary = process_data_and_generate_summary(data_df)
            return jsonify({
                'summary': summary
            })
        except Exception as e:
            return jsonify({'error': str(e), 'type': str(type(e).__name__)}), 500


def process_data_and_generate_summary(df):
    avg_operation_time = df['OperationTime'].mean()
    avg_error_rate = df['ErrorRate'].mean()
    max_error_rate = df['ErrorRate'].max()
    min_error_rate = df['ErrorRate'].min()

    operational_count = df[df['Status'] == 1].shape[0]
    maintenance_count = df[df['Status'] == 0].shape[0]

    total_devices = df.shape[0]
    if total_devices > 0:
        operational_percentage = (operational_count / total_devices) * 100
    else:
        operational_percentage = 0

    summary = (
        f"Total Devices: {total_devices}\n"
        f"Operational Devices: {operational_count} ({operational_percentage:.2f}%)\n"
        f"Devices in Maintenace: {maintenance_count}\n"
        f"Average Operation Time: {avg_operation_time:.2f} seconds\n"
        f"Average Error Rate: {avg_error_rate:.3f}\n"
        f"Error Rate Change: {min_error_rate:.3f} to {max_error_rate:.3f}"
    )

    return summary


def load_csv_data(filepath):
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        raise Exception(f"Failed to load CSV: {str(e)}")
