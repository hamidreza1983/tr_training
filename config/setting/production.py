from config.settings import *
SECRET_KEY = 'django-insecure-4-#ye^gtr($87s=)3^x%&x7^49*s426or!)b%twh_h6jd5f5+a'
DEBUG = False
ALLOWED_HOSTS = ['learningpy.ir', 'www.learningpy.ir']
SITE_ID = 1
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'learningpy',
        'USER': 'admin',
        'PASSWORD': 'H@midreza62',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
STATIC_ROOT = BASE_DIR.joinpath('/static')
MEDIA_ROOT = BASE_DIR.joinpath('media')

STATICFILES_DIRS = [
    BASE_DIR/'static',
]

#CSRF_COOKIE_SECURE = True
#CSRF_COOKIE_SAMESITE = 'Strict'
#SESSION_COOKIE_SECURE = True
#SECURE_BROWSER_XSS_FILTER = True
#SECURE_CONTENT_TYPE_NOSNIFF = True
#SECURE_SSL_REDIRECT = True
#X_FRAME_OPTIONS = 'DENY'
#SECURE_HSTS_SECONDS = 15768000  # set low, but when site is ready for deployment, set to at least 15768000 (6 months)
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#SECURE_HSTS_PRELOAD = True
#CSP_DEFAULT_SRC = ("'none'",)
#CSP_STYLE_SRC = ("'self'",)
#CSP_SCRIPT_SRC = ("'self'",)
#CSP_FONT_SRC = ("'self'",)
#CSP_IMG_SRC = ("'self'",)