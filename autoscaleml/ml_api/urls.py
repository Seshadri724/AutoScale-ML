from django.urls import path
from .views import predict_view
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', predict_view),
]