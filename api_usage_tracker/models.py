from django.db import models
from django.utils import timezone
from django.conf import settings

class APIEndpointUsage(models.Model):
    """
    Model to track API endpoint usage
    """
    view_name = models.CharField(max_length=255, db_index=True)
    method = models.CharField(max_length=10)
    first_called = models.DateTimeField(auto_now_add=True)
    last_called = models.DateTimeField(auto_now=True)
    total_calls = models.PositiveIntegerField(default=1)
    
    class Meta:
        unique_together = ('view_name', 'method')
        verbose_name = 'API Endpoint Usage'
        verbose_name_plural = 'API Endpoint Usages'
    
    def is_deprecated(self):
        """
        Check if endpoint is deprecated based on last usage
        """
        deprecation_days = getattr(settings, 'API_USAGE_TRACKER', {}).get('DEPRECATION_DAYS', 90)
        if not self.last_called:
            return False
        return (timezone.now() - self.last_called).days > deprecation_days
    
    def __str__(self):
        return f"{self.view_name} ({self.method})"
