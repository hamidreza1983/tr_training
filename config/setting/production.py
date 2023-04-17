from config.settings import *
SECRET_KEY = 'dhujx8&d=7=mmh(@2bmo8v%zzkc-i&!s6=68qy79@fkv*2mnq0'
DEBUG = False
ALLOWED_HOSTS = ['learningpy.ir', 'www.learningpy.ir']
SITE_ID = 1
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'learnin2_learningpy',
        'USER': 'learnin2_hamid',
        'PASSWORD': 'H@midreza62',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
STATIC_ROOT = '/home/learnin2/public_html/static'
MEDIA_ROOT = '/home/learnin2/public_html/media'

STATICFILES_DIRS = [
    BASE_DIR/'static',
]

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'Strict'
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 15768000  # set low, but when site is ready for deployment, set to at least 15768000 (6 months)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
CSP_DEFAULT_SRC = ("'none'",)
CSP_STYLE_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'",)
CSP_FONT_SRC = ("'self'",)
CSP_IMG_SRC = ("'self'",)