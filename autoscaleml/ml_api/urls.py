from django.urls import path
from .views import (
    home,
    predict_view,
    health_check_json,
    health_dashboard,
    metrics_json,
    metrics_dashboard
)

urlpatterns = [
    path('', home, name='home'),

    # Prediction API
    path('predict/', predict_view, name='predict_view'),

    # Health endpoints
    path('health/json/', health_check_json, name='health_check_json'),     # JSON API
    path('health/', health_dashboard, name='health_dashboard'),            # Web UI

    # Metrics endpoints
    path('metrics/json/', metrics_json, name='metrics_json'),             # JSON API
    path('metrics/', metrics_dashboard, name='metrics_dashboard'),        # Web UI
]
