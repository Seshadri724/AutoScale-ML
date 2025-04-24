from django.db import models
import joblib
import os

# Path to saved ML model
MODEL_PATH = "ml_api/model.joblib"
model = joblib.load(MODEL_PATH)  # Load once at server startup

def predict(input_features):
    # Take a list of input features and return the model's predictions
    return model.predict([input_features])[0]