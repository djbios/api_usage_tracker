# API Usage Tracker

## Features
- Middleware to track API endpoint usage
- Web interface to view API usage statistics
- Automatic deprecation marking for unused endpoints

## Installation

1. Install the package:
```bash
pip install api-usage-tracker
```

2. Add to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'api_usage_tracker',
    'rest_framework',
    'drf_spectacular',
]
```

3. Add middleware:
```python
MIDDLEWARE = [
    ...
    'api_usage_tracker.middleware.APIUsageMiddleware',
]
```

4. Configure settings:
```python
# Optional settings with defaults
API_USAGE_TRACKER = {
    'DEPRECATION_DAYS': 90,  # Mark as deprecated after 90 days of no usage
}
```

## Usage

The app automatically tracks API endpoint usage. Access the usage dashboard at `/api-usage/`.
