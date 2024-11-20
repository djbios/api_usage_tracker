from setuptools import setup, find_packages

setup(
    name='api-usage-tracker',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Django app to track API endpoint usage and mark deprecated endpoints',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/api-usage-tracker',
    author='Your Name',
    author_email='your.email@example.com',
    install_requires=[
        'Django>=4.2',
        'djangorestframework>=3.14',
        'drf-spectacular>=0.26',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
