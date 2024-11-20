from setuptools import setup, find_packages

# Read requirements
with open('requirements.txt') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='api-usage-tracker',
    version='0.1.0',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    license='MIT License',
    description='Django app to track API endpoint usage and mark deprecated endpoints',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/api-usage-tracker',
    author='Your Name',
    author_email='your.email@example.com',
    python_requires='>=3.8',
    install_requires=requirements,
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-django>=4.5.0',
            'pytest-cov>=4.0.0',
            'pylint>=2.17.0',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 4.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    project_urls={
        'Bug Reports': 'https://github.com/yourusername/api-usage-tracker/issues',
        'Source': 'https://github.com/yourusername/api-usage-tracker',
    },
)
