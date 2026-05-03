from flask import Flask, request, jsonify
from flask_cors import CORS
from predict import load_models, predict_readmission_risk, cluster_patient
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

# Load models at startup
models = load_models()

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'service': 'Hospital Readmission API'})

@app.route('/api/predict/readmission', methods=['POST'])
def predict_readmission():
    """Predict readmission risk"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        features = data.get('features', [1, 2, 3])
        
        if not features or not isinstance(features, list):
            return jsonify({'error': 'Invalid features format'}), 400
        
        if 'classification' not in models or models['classification'] is None:
            return jsonify({'error': 'Classification model not loaded'}), 500
        
        result = predict_readmission_risk(features, models['classification'])
        
        if 'error' in result:
            return jsonify(result), 400
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        features = data.get('features', [1, 2, 3])
        
        if not features or not isinstance(features, list):
            return jsonify({'error': 'Invalid features format'}), 400
        
        if 'clustering' not in models or models['clustering'] is None:
            return jsonify({'error': 'Clustering model not loaded'}), 500
        
        result = cluster_patient(features, models['clustering'])
        
        if 'error' in result:
            return jsonify(result), 400
            
        return jsonify(result)
    
    except Exception as e:
        print(f"Error in predict_cluster: {e}")
        return jsonify({'error': str(e)}), 5
    try:
        data = request.get_json()
        features = data.get('features', [])
        
        if 'clustering' not in models or models['clustering'] is None:
            return jsonify({'error': 'Clustering model not loaded'}), 500
        
        result = cluster_patient(features, models['clustering'])
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/data/summary', methods=['GET'])
def get_data_summary():
    """Get dataset summary statistics"""
    try:
        data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'cleaned_data.csv')
        
        if not os.path.exists(data_path):
            return jsonify({'error': 'Data file not found'}), 404
        
        df = pd.read_csv(data_path)
        
        summary = {
            'total_records': len(df),
            'features': list(df.columns),
            'shape': [len(df), len(df.columns)],
            'missing_values': df.isnull().sum().to_dict()
        }
        
        return jsonify(summary)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
