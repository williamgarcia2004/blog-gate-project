from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / 'media'

# ? Auth
LOGIN_REDIRECT_URL = 'core:post_list'
LOGIN_URL = 'custom_auth:login'
LOGOUT_URL = 'custom_auth:logout_done'

# ? Sesiones 
"""
    Si el usuario está activo y hace una request, el contador se reinicia y la sesión se extiende y no se desloguea
"""

SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_AGE = 86400