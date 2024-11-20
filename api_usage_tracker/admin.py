from django.contrib import admin
from .models import APIEndpointUsage

@admin.register(APIEndpointUsage)
class APIEndpointUsageAdmin(admin.ModelAdmin):
    """
    Admin configuration for API Endpoint Usage
    """
    list_display = ('view_name', 'method', 'first_called', 'last_called', 'total_calls', 'is_deprecated')
    list_filter = ('method',)
    search_fields = ('view_name',)
    readonly_fields = ('first_called', 'last_called', 'total_calls')
    
    def is_deprecated(self, obj):
        """
        Display deprecation status in admin
        """
        return obj.is_deprecated()
    is_deprecated.boolean = True
    is_deprecated.short_description = 'Deprecated'
