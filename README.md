
# AI-Based Disease Prediction System

This project is a simple AI/ML-based system that predicts a disease based on symptoms selected by the user. It uses a Random Forest Classifier trained on dummy health data.

## Features
- Predicts disease based on user input (symptoms)
- Uses Streamlit for interactive UI
- Trained with scikit-learn RandomForest model

## How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
streamlit run app.py
```

## Files
- `app.py` - Streamlit app UI
- `model.pkl` - Trained ML model
- `disease_data.csv` - Sample training dataset
