from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import predict, PredictionLog
from django.db.models import Avg, Count
from django.db import connections
from django.db.utils import OperationalError
from django.utils import timezone
from django.db.models import Q
from django.http import JsonResponse
import time
import datetime
import psutil  # Optional, if using for CPU/Memory on local

# ✅ Home Page
def home(request):
    return render(request, 'home.html')

# ✅ Predict API
@api_view(['POST'])
def predict_view(request):
    input_data = request.data.get("features")
    if not input_data:
        return Response({"error": "Missing 'features'"}, status=400)

    start = time.time()
    prediction = predict(input_data)[0]
    latency = round((time.time() - start) * 1000, 2)

    # Log prediction
    PredictionLog.objects.create(
        input_data=input_data,
        prediction=float(prediction),
        latency_ms=latency
    )

    return Response({
        "prediction": prediction,
        "latency_ms": latency
    })



@api_view(['GET'])
def health_check_json(request):
    # Check database status
    try:
        connections['default'].cursor()
        db_status = "connected"
    except OperationalError:
        db_status = "unavailable"

    # Check model status by performing a dummy prediction
    try:
        dummy_input = [1,2,3,4]  # Adjust this input to suit your predict() function
        status=predict(dummy_input)[1]
        if status != 200:
            raise Exception("Model prediction failed")
        model_status = "ready"
    except Exception as e:
        model_status = f"error: {str(e)}"

    # Determine API overall status
    api_status = "ok" if db_status == "connected" and model_status == "ready" else "degraded"

    return Response({
        "status": api_status,
        "model": model_status,
        "database": db_status
    })

@api_view(['GET'])
def health_dashboard(request):
    # Check database status
    try:
        connections['default'].cursor()
        db_status = "connected"
    except OperationalError:
        db_status = "unavailable"

    # Check model status
    try:
        dummy_input = [1,2,3,4]  # Adjust this input to suit your predict() function
        status=predict(dummy_input)[1]
        if status != 200:
            raise Exception("Model prediction failed")
        model_status = "ready"
    except Exception as e:
        model_status = f"error: {str(e)}"

    # Determine API overall status
    api_status = "ok" if db_status == "connected" and model_status == "ready" else "degraded"

    return render(request, "health.html", {
        "status": api_status,
        "model": model_status,
        "database": db_status
    })


# ✅ Metrics JSON
@api_view(['GET'])
def metrics_json(request):
    total_requests = PredictionLog.objects.count()
    avg_latency = PredictionLog.objects.aggregate(avg=Avg('latency_ms'))['avg'] or 0

    now = timezone.now()
    one_minute_ago = now - datetime.timedelta(seconds=5)
    recent_logs = PredictionLog.objects.filter(timestamp__gte=one_minute_ago)

    # Requests per second over the last minute
    rps = round(recent_logs.count() / 5, 2)

    # Latency percentiles (using manual logic; PostgreSQL users can use percentile_cont)
    recent_latencies = list(recent_logs.values_list('latency_ms', flat=True))
    latency_p50 = latency_p90 = latency_p99 = 0
    if recent_latencies:
        sorted_latencies = sorted(recent_latencies)
        n = len(sorted_latencies)
        latency_p50 = round(sorted_latencies[int(n * 0.50)], 2)*100
        latency_p90 = round(sorted_latencies[int(n * 0.90) - 1], 2)*100
        latency_p99 = round(sorted_latencies[int(n * 0.99) - 1], 2)*100

    # Example error rate calculation: assuming prediction == -1 is an error
    total_errors = PredictionLog.objects.filter(prediction__lte=0).count()
    error_rate = round((total_errors / total_requests) * 100, 2) if total_requests else 0.0

    # CPU/Memory usage (Optional: use Kubernetes metrics for real usage)
    cpu_percent = psutil.cpu_percent()*100
    memory_mb = round(psutil.virtual_memory().used / (1024 * 1024), 2)

    return Response({
        "requests_count": total_requests,
        "average_latency_ms": round(avg_latency, 2),
        "rps": rps,
        "latency_p50": latency_p50,
        "latency_p90": latency_p90,
        "latency_p99": latency_p99,
        "cpu": cpu_percent,
        "memory": memory_mb,
        "error_rate": error_rate
    })

# ✅ Metrics HTML
def metrics_dashboard(request):
    total_requests = PredictionLog.objects.count()
    avg_latency = PredictionLog.objects.aggregate(avg=Avg('latency_ms'))['avg'] or 0

    return render(request, "metrics.html", {
        "requests_count": total_requests,
        "average_latency": round(avg_latency, 2),
        
    })
