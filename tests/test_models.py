import pytest
from django.utils import timezone
from datetime import timedelta
from api_usage_tracker.models import APIEndpointUsage

@pytest.mark.django_db
class TestAPIEndpointUsage:
    def test_create_endpoint_usage(self):
        """Test creating an endpoint usage record"""
        usage = APIEndpointUsage.objects.create(
            view_name='test_view',
            method='GET'
        )
        assert usage.view_name == 'test_view'
        assert usage.method == 'GET'
        assert usage.total_calls == 1
        
    def test_is_deprecated_with_recent_usage(self):
        """Test endpoint is not deprecated when recently used"""
        usage = APIEndpointUsage.objects.create(
            view_name='test_view',
            method='GET',
            last_called=timezone.now()
        )
        assert not usage.is_deprecated()
        
    def test_is_deprecated_with_old_usage(self):
        """Test endpoint is deprecated when not used for a long time"""
        old_date = timezone.now() - timedelta(days=91)
        usage = APIEndpointUsage.objects.create(
            view_name='test_view',
            method='GET',
            last_called=old_date
        )
        assert usage.is_deprecated()
        
    def test_str_representation(self):
        """Test string representation of the model"""
        usage = APIEndpointUsage.objects.create(
            view_name='test_view',
            method='GET'
        )
        assert str(usage) == 'test_view (GET)'
