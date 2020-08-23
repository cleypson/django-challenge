from settings.base import *

DEBUG = True

INTERNAL_IPS = ['localhost', '127.0.0.1', '0.0.0.0']

ALLOWED_HOSTS += INTERNAL_IPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_challenge',
        'USER': 'django_challenge',
        'PASSWORD': 'GT8XmPY2xvENgpGz',
        'HOST': 'db',
        'PORT': '5432',
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets'),
]

STATIC_URL = '/assets/'
# STATIC_ROOT = 'assets/'

MEDIA_URL = 'http://0.0.0.0:8000/assets/media/'
MEDIA_ROOT = 'assets/media/'

