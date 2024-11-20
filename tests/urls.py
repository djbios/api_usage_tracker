from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .test_views import TestViewSet

router = DefaultRouter()
router.register('test', TestViewSet, basename='test')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-usage/', include('api_usage_tracker.urls')),
]
