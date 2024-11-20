from drf_spectacular.extensions import OpenApiViewExtension
from .models import APIEndpointUsage
from django.utils import timezone
from datetime import timedelta

class DeprecationSchemaExtension(OpenApiViewExtension):
    """
    Custom schema extension to mark endpoints as deprecated
    based on usage tracking
    """
    target_class = 'rest_framework.views.APIView'
    match_subclasses = True
    priority = 1
    
    def view_replacement(self):
        """
        Modify the schema for deprecated endpoints
        """
        class ExtendedView(self.target_class):
            def get_schema(self):
                schema = super().get_schema()
                
                try:
                    # Get view name
                    view_name = f"{self.__module__}.{self.__class__.__name__}"
                    usage = APIEndpointUsage.objects.filter(
                        view_name=view_name
                    ).first()
                    
                    if usage and usage.is_deprecated():
                        schema['deprecated'] = True
                        if 'description' in schema:
                            schema['description'] += "\n\n**DEPRECATED**: This endpoint has not been used for over 90 days."
                        else:
                            schema['description'] = "**DEPRECATED**: This endpoint has not been used for over 90 days."
                except Exception:
                    pass
                    
                return schema
                
        return ExtendedView
