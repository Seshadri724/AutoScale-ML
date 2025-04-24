"""
A simple Logistic Regression (Multi-class Classification) model trained on the iris flower dataset

Dataset Details:
- 150 flower samples
- 4 features:
    - Sepal length
    - Sepal width
    - Petal length
    - Petal width
- 3 flower classes:
    - 0: Setosa
    - 1: Versicolor
    - 2: Virginica

Model learns decision boundaries over 200 iterations to seperate 3 flower types based on 4 features and outputs a class type.

Example inputs to the model:
- 0: Setosa:
    - { "features": [5.1, 3.5, 1.4, 0.2] }
- 1: Versicolor:
    - { "features": [6.0, 2.9, 4.5, 1.5] }
- 2: Virginica:
    - { "features": [6.5, 3.0, 5.8, 2.2] }
"""
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import joblib

X, y = load_iris(return_X_y=True)
model = LogisticRegression(max_iter=200)
model.fit(X, y)
joblib.dump(model, 'ml_api/model.joblib')