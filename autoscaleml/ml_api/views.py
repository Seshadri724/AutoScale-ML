from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import predict, PredictionLog
import time
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

@api_view(['POST'])
def predict_view(request):
    # get input features from request body
    input_data = request.data.get("features")

    # if no features, return error message
    if not input_data:
        return Response({"error": "Missing 'features'"}, status=400)

    # measure latency
    start = time.time()
    prediction = predict(input_data)
    latency = round((time.time() - start) * 1000, 2)

    # Log the prediction
    PredictionLog.objects.create(
        input_data=input_data,
        prediction=float(prediction),
        latency_ms=latency
    )

    return Response({
        "prediction": prediction,
        "latency_ms": latency
    })