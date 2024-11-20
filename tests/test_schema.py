import pytest
from django.utils import timezone
from datetime import timedelta
from api_usage_tracker.models import APIEndpointUsage
from api_usage_tracker.schema import DeprecationSchemaExtension
from rest_framework.views import APIView

@pytest.mark.django_db
class TestDeprecationSchema:
    def test_schema_marks_deprecated_endpoint(self):
        """Test that schema extension marks deprecated endpoints"""
        # Create a test view
        class TestView(APIView):
            pass
        
        # Create usage record for the view
        APIEndpointUsage.objects.create(
            view_name='tests.test_schema.TestView',
            method='GET',
            last_called=timezone.now() - timedelta(days=100)
        )
        
        # Initialize schema extension
        extension = DeprecationSchemaExtension()
        operation = {'description': 'Test operation'}
        
        # Test schema modification
        extension.get_schema_operation_parameters(None, operation, TestView)
        
        assert operation['deprecated'] is True
        assert 'DEPRECATED' in operation['description']
        
    def test_schema_active_endpoint(self):
        """Test that schema extension doesn't mark active endpoints as deprecated"""
        # Create a test view
        class TestView(APIView):
            pass
        
        # Create usage record for the view
        APIEndpointUsage.objects.create(
            view_name='tests.test_schema.TestView',
            method='GET',
            last_called=timezone.now()
        )
        
        # Initialize schema extension
        extension = DeprecationSchemaExtension()
        operation = {'description': 'Test operation'}
        
        # Test schema modification
        extension.get_schema_operation_parameters(None, operation, TestView)
        
        assert not operation.get('deprecated', False)
        assert 'DEPRECATED' not in operation['description']
        
    def test_schema_no_usage_record(self):
        """Test schema extension behavior when no usage record exists"""
        # Create a test view
        class TestView(APIView):
            pass
        
        # Initialize schema extension
        extension = DeprecationSchemaExtension()
        operation = {'description': 'Test operation'}
        
        # Test schema modification
        extension.get_schema_operation_parameters(None, operation, TestView)
        
        assert not operation.get('deprecated', False)
        assert operation['description'] == 'Test operation'
