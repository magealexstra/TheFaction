# Template for secrets.py
# Copy this file to secrets.py and fill in your values
# DO NOT commit secrets.py to version control

# Django Secret Key
# Generate a new one for production using: 
# python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
SECRET_KEY = 'your-secret-key-here'

# Database credentials
DB_NAME = 'thefaction_db'
DB_USER = 'your_db_username'
DB_PASSWORD = 'your_db_password'
DB_HOST = 'localhost'
DB_PORT = '5432'

# Email settings
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_email_password'

# API Keys
GITHUB_API_KEY = 'your_github_api_key'