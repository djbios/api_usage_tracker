import os
import django
from django.conf import settings

# Configure Django settings before running tests
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')
django.setup()
