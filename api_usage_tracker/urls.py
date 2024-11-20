from django.urls import path
from .views import APIUsageListView, api_usage_dashboard

urlpatterns = [
    path('', api_usage_dashboard, name='api_usage_dashboard'),
    path('stats/', APIUsageListView.as_view(), name='api_usage_stats'),
]
