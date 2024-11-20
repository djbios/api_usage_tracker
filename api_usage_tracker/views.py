from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import F
from django.utils import timezone
from datetime import timedelta
from .models import APIEndpointUsage

class APIUsageListView(ListView):
    """
    View to display API endpoint usage statistics
    """
    model = APIEndpointUsage
    template_name = 'api_usage_tracker/usage_stats.html'
    context_object_name = 'endpoints'

    def get_queryset(self):
        """
        Annotate and order the queryset
        """
        return APIEndpointUsage.objects.annotate(
            is_deprecated=F('id')  # Placeholder for is_deprecated annotation
        ).order_by('-total_calls')

    def get_context_data(self, **kwargs):
        """
        Add additional context data
        """
        context = super().get_context_data(**kwargs)
        
        # Calculate additional statistics
        context['total_endpoints'] = APIEndpointUsage.objects.count()
        context['deprecated_endpoints'] = APIEndpointUsage.objects.filter(
            last_called__lt=timezone.now() - timedelta(days=90)
        ).count()
        context['most_used_endpoint'] = APIEndpointUsage.objects.order_by('-total_calls').first()
        context['least_used_endpoint'] = APIEndpointUsage.objects.order_by('total_calls').first()
        
        return context

def api_usage_dashboard(request):
    """
    Render API usage dashboard
    """
    return render(request, 'api_usage_tracker/dashboard.html', {
        'endpoints': APIEndpointUsage.objects.all(),
    })
