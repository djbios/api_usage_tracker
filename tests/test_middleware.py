import pytest
from django.test import Client
from api_usage_tracker.models import APIEndpointUsage

@pytest.mark.django_db
class TestAPIUsageMiddleware:
    def test_middleware_tracks_api_call(self, client):
        """Test that middleware tracks API calls"""
        response = client.get('/api/test/')
        assert response.status_code == 200
        
        usage = APIEndpointUsage.objects.first()
        assert usage is not None
        assert usage.view_name == 'test-list'
        assert usage.method == 'GET'
        assert usage.total_calls == 1
        
    def test_middleware_updates_existing_record(self, client):
        """Test that middleware updates existing records"""
        # Make first call
        client.get('/api/test/')
        
        # Make second call
        client.get('/api/test/')
        
        usage = APIEndpointUsage.objects.get(view_name='test-list', method='GET')
        assert usage.total_calls == 2
        
    def test_middleware_tracks_different_methods(self, client):
        """Test that middleware tracks different HTTP methods"""
        # Make GET request
        client.get('/api/test/')
        
        # Make POST request
        client.post('/api/test/')
        
        get_usage = APIEndpointUsage.objects.get(view_name='test-list', method='GET')
        post_usage = APIEndpointUsage.objects.get(view_name='test-list', method='POST')
        
        assert get_usage.total_calls == 1
        assert post_usage.total_calls == 1
        
    def test_middleware_tracks_detail_views(self, client):
        """Test that middleware tracks detail view calls"""
        response = client.get('/api/test/1/')
        assert response.status_code == 200
        
        usage = APIEndpointUsage.objects.get(view_name='test-detail', method='GET')
        assert usage.total_calls == 1
