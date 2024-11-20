from django.utils import timezone
from .models import APIEndpointUsage
from rest_framework.views import APIView

class APIUsageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process the request before view is called
        response = self.get_response(request)
        
        # Check if this is a DRF API view
        view = getattr(request, 'resolver_match', None)
        if view and hasattr(view, 'view_name'):
            try:
                # Get or create usage record
                usage, created = APIEndpointUsage.objects.get_or_create(
                    view_name=view.view_name,
                    method=request.method,
                    defaults={
                        'first_called': timezone.now(),
                        'last_called': timezone.now(),
                        'total_calls': 1
                    }
                )
                
                if not created:
                    # Update existing record
                    usage.last_called = timezone.now()
                    usage.total_calls += 1
                    usage.save(update_fields=['last_called', 'total_calls'])
            
            except Exception:
                # Silently handle any tracking errors
                pass
        
        return response
