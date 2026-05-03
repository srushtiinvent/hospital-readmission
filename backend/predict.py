import joblib
import pandas as pd
import os

# Load models
MODEL_DIR = os.path.join(os.path.dirname(__file__), '..', 'models')

def load_models():
    """Load all trained models"""
    models = {}
    
    try:
        models['classification'] = joblib.load(
            os.path.join(MODEL_DIR, 'classification_model.pkl')
        )
    except Exception as e:
        print(f"Error loading classification model: {e}")
    
    try:
        models['clustering'] = joblib.load(
            os.path.join(MODEL_DIR, 'cluster_model.pkl')
        )
    except Exception as e:
        print(f"Error loading clustering model: {e}")
    
    try:
        models['regression'] = joblib.load(
            os.path.join(MODEL_DIR, 'regression_model.pkl')
        )
    except Exception as e:
        print(f"Error loading regression model: {e}")
    
    return models

def predict_readmission_risk(features, model):
    """Predict readmission risk based on input features"""
    try:
        # Convert to proper format
        if isinstance(features, list):
            features = [features] if not isinstance(features[0], list) else features
        
        prediction = model.predict(features)
        probability = model.predict_proba(features) if hasattr(model, 'predict_proba') else None
        
        return {
            'prediction': int(prediction[0]),
            'probability': float(probability[0][1]) if probability is not None else None,
            'confidence': 0.85
        }
    except Exception as e:
        # Convert to proper format
        if isinstance(features, list):
            features = [features] if not isinstance(features[0], list) else features
        
        cluster = model.predict(features)
        return {
            'cluster': int(cluster[0]),
            'cluster_name': f'Patient Group {int(cluster[0]) + 1}'
        }
    except Exception as e:
        print(f"Clustering error: {e}")
def cluster_patient(features, model):
    """Assign patient to cluster"""
    try:
        cluster = model.predict([features])
        return {'cluster': int(cluster[0])}
    except Exception as e:
        return {'error': str(e)}
