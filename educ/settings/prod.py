import os
from .base import *

DEBUG = False
ADMINS = [
    ('Fatemeh S', 'fatemehsoleymani69@yahoo.com'),
]
ALLOWED_HOSTS = ['.educproject.com']
CSRF_TRUSTED_ORIGINS = [
    'https://educproject.com',
    'https://www.educproject.com',
    'http://educproject.com',  # Add this if used during development
    'http://www.educproject.com',
]

SECRET_KEY = 'aaaaml73%x^fzbz&ky(hl#b@howgdvui#@!m2e@m%*z^g07xy#8f6r'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}


REDIS_URL = 'redis://cache:6379'
CACHES['default']['LOCATION'] = REDIS_URL
CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]


CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = False
SECURE_HSTS_SECONDS = 31536000  # Enforce HTTPS for 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True