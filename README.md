# API Usage Tracker

[![PyPI version](https://badge.fury.io/py/api-usage-tracker.svg)](https://badge.fury.io/py/api-usage-tracker)
[![CI/CD](https://github.com/yourusername/api-usage-tracker/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/api-usage-tracker/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/yourusername/api-usage-tracker/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/api-usage-tracker)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Django app that automatically tracks API endpoint usage and helps manage endpoint deprecation.

## Features
- Middleware to track API endpoint usage
- Web interface to view API usage statistics
- Automatic deprecation marking for unused endpoints
- OpenAPI/Swagger integration via DRF Spectacular
- Configurable deprecation thresholds

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

### Dashboard Features
- Overview of all API endpoints
- Usage statistics and trends
- Deprecated endpoint highlighting
- Last usage timestamps
- Total call counts

### OpenAPI Integration
The app automatically marks deprecated endpoints in your OpenAPI/Swagger documentation when using DRF Spectacular.

## Development

### Setup Development Environment

1. Clone the repository:
```bash
git clone https://github.com/yourusername/api-usage-tracker.git
cd api-usage-tracker
```

2. Install development dependencies:
```bash
pip install -e ".[dev]"
```

### Running Tests
```bash
pytest tests/
```

### Code Quality
```bash
pylint api_usage_tracker tests
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
