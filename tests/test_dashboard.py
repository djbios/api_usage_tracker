import pytest
from django.urls import reverse
from api_usage_tracker.models import APIEndpointUsage
from django.utils import timezone
from datetime import timedelta

@pytest.mark.django_db
class TestAPIUsageDashboard:
    def test_dashboard_view(self, client):
        """Test that dashboard view works"""
        response = client.get(reverse('api_usage_dashboard'))
        assert response.status_code == 200
        assert 'endpoints' in response.context
        
    def test_stats_view(self, client):
        """Test that stats view works"""
        response = client.get(reverse('api_usage_stats'))
        assert response.status_code == 200
        assert 'endpoints' in response.context
        
    def test_dashboard_shows_correct_stats(self, client):
        """Test that dashboard shows correct statistics"""
        # Create some test data
        APIEndpointUsage.objects.create(
            view_name='active_view',
            method='GET',
            total_calls=10,
            last_called=timezone.now()
        )
        
        APIEndpointUsage.objects.create(
            view_name='deprecated_view',
            method='POST',
            total_calls=5,
            last_called=timezone.now() - timedelta(days=100)
        )
        
        response = client.get(reverse('api_usage_dashboard'))
        context = response.context
        
        assert context['total_endpoints'] == 2
        assert context['deprecated_endpoints'] == 1
        assert context['most_used_endpoint'].total_calls == 10
        assert context['least_used_endpoint'].total_calls == 5
