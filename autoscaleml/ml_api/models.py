from django.db import models
import joblib
import os
import json

# Path to saved ML model
MODEL_PATH = "ml_api/model.joblib"
model = joblib.load(MODEL_PATH)  # Load once at server startup


class PredictionLog(models.Model):
    input_data = models.JSONField()
    prediction = models.FloatField()
    latency_ms = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['-timestamp']),  # Index for faster querying by timestamp
        ]


def predict(input_features):
    # Take a list of input features and return the model's predictions
    return (model.predict([input_features])[0],200)