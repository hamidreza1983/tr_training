from config.settings import *

SECRET_KEY = 'django-insecure-4-#ye^gtr($87s=)3^x%&x7^49*s426or!)b%twh_h6jd5f5+a'



DEBUG = True
#INSTALLED_APPS += [
#    'debug_toolbar',
#]

ALLOWED_HOSTS = []
SITE_ID = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR.joinpath('/static')
MEDIA_ROOT = BASE_DIR.joinpath('media')

STATICFILES_DIRS = [
    BASE_DIR/'static',
]

MAINTENANCE_MODE = False