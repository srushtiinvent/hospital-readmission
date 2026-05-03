<<<<<<< HEAD
# hospital-readmission
=======
# Hospital Readmission Prediction System

A comprehensive machine learning system for predicting hospital readmission risks and analyzing patient data.

## Project Structure

```
hospital-readmission/
├── data/                    # Data files
│   ├── raw_data.csv        # Original dataset
│   └── cleaned_data.csv    # Preprocessed dataset
│
├── notebooks/              # Jupyter notebooks
│   ├── 0_setup.ipynb       # Project setup and configuration
│   ├── 1_preprocessing.ipynb # Data cleaning and preparation
│   ├── 2_classification.ipynb # Readmission risk prediction
│   ├── 3_clustering.ipynb   # Patient segmentation
│   ├── 4_association_rules.ipynb # Pattern discovery
│   └── 5_regression.ipynb   # Length of stay prediction
│
├── models/                  # Trained ML models
│   ├── classification_model.pkl
│   ├── cluster_model.pkl
│   └── regression_model.pkl
│
├── backend/                 # Flask API
│   ├── app.py              # Main Flask application
│   ├── predict.py          # Model inference utilities
│   └── requirements.txt    # Python dependencies
│
└── frontend/                # React frontend
    ├── src/
    │   ├── App.jsx
    │   ├── pages/
    │   │   ├── Dashboard.jsx
    │   │   ├── RiskAssessor.jsx
    │   │   ├── ClusterExplorer.jsx
    │   │   └── RulesExplorer.jsx
    │   └── index.js
    └── package.json
```

## Quick Start

### 1. Backend Setup

```bash
cd backend
pip install -r requirements.txt
python app.py
```

The Flask API will start on `http://localhost:5000`

### 2. Frontend Setup

```bash
cd frontend
npm install
npm start
```

The React app will open on `http://localhost:3000`

### 3. Running Notebooks

First, ensure Jupyter is installed:
```bash
pip install jupyter
```

Then start Jupyter:
```bash
cd notebooks
jupyter notebook
```

## Notebooks Overview

### 0_setup.ipynb
Sets up the project environment, installs dependencies, and configures paths.

### 1_preprocessing.ipynb
Cleans raw data, handles missing values, and performs feature engineering.

### 2_classification.ipynb
Builds and trains classification models for readmission risk prediction.

### 3_clustering.ipynb
Performs patient clustering analysis using K-means.

### 4_association_rules.ipynb
Discovers association rules in patient readmission patterns.

### 5_regression.ipynb
Predicts hospital length of stay using regression models.

## API Endpoints

- `GET /health` - Health check
- `POST /api/predict/readmission` - Predict readmission risk
- `POST /api/predict/cluster` - Assign patient to cluster
- `GET /api/data/summary` - Get dataset summary

## Frontend Pages

- **Dashboard** - Overview of dataset statistics
- **Risk Assessor** - Predict readmission risk for individual patients
- **Cluster Explorer** - Assign patients to clusters
- **Rules Explorer** - View association rules and patterns

## Requirements

### Backend
- Python 3.8+
- Flask 2.3.0
- pandas 2.0.0
- scikit-learn 1.2.0
- numpy 1.24.0

### Frontend
- Node.js 14+
- React 18.2.0
- npm or yarn

## License

This project is open source and available under the MIT License.
>>>>>>> 04038f9 (Initial commit)
