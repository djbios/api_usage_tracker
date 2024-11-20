from drf_spectacular.extensions import OpenApiSchemaExtension
from .models import APIEndpointUsage
from django.utils import timezone
from datetime import timedelta

class DeprecationSchemaExtension(OpenApiSchemaExtension):
    """
    Custom schema extension to mark endpoints as deprecated
    based on usage tracking
    """
    target_class = 'rest_framework.views.APIView'
    
    def get_schema_operation_parameters(self, auto_schema, operation, view_class):
        """
        Add deprecation information to schema
        """
        # Get view name 
        view_name = f"{view_class.__module__}.{view_class.__name__}"
        
        # Check usage tracking
        try:
            usage = APIEndpointUsage.objects.filter(
                view_name=view_name
            ).first()
            
            if usage and usage.is_deprecated():
                operation['deprecated'] = True
                operation['description'] += "\n\n**DEPRECATED**: This endpoint has not been used for over 90 days."
        
        except Exception:
            # Silently handle any errors
            pass
        
        return []
