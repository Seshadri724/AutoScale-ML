from django.contrib import admin
from .models import PredictionLog

@admin.register(PredictionLog)
class PredictionLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'prediction', 'latency_ms')
    list_filter = ('timestamp',)
    search_fields = ('input_data',)
    ordering = ('-timestamp',)
