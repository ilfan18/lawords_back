import os
import datetime
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pw+*a^45y7s_f(im29%4ot2222m1h7zed4w+$03_trf4)0)!l!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SITE_NAME = "Lawords"

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'ckeditor',
    'ckeditor_uploader',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'drf_spectacular',
    'corsheaders',

    'oauth2_provider',
    'social_django',
    'rest_framework_social_oauth2',

    'courses',
    'users',
    'users_auth',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dev_db',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

AUTH_USER_MODEL = 'users.User'
# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Add needed from https://python-social-auth.readthedocs.io/en/latest/backends/index.html#supported-backends
AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'rest_framework_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]


# Internationalization
LANGUAGE_CODE = 'ru'
LANGUAGES = (
    ('ru', _('Russian')),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = ['static/logo/', ]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# DRF
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# SimpleJWT
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(seconds=6000),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,
}

# smtp
# ! Временно, пока не разобрался с отправкой писем
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# MAILER_EMAIL_BACKEND = EMAIL_BACKEND
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'iqonzzedjmlygqkv'
EMAIL_HOST_USER = 'ilfanmuratov@gmail.com'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'ilfanmuratov@gmail.com'

# My user settings
CUSTOM_USER_SYSTEM = {

}

#  Django REST Framework Social OAuth2
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '75953706797-gd7cqpdj4kor1f87hpmmln985mhmll4p.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

# Corsheaders
CORS_ORIGIN_ALLOW_ALL = True

# drf-spectacular
SPECTACULAR_SETTINGS = {
    'TITLE': 'Lawords',
    'DESCRIPTION': 'Сервис изучения английского языка',
    'VERSION': '1.0.0',
}

# Admin settings
JAZZMIN_SETTINGS = {
    'site_title': 'Lawords admin',
    'site_header': 'Lawords',
    'site_brand': 'Lawords',
    'site_logo': 'logo.png',
    'site_logo_classes': '',
    #! Про это уточнить
    'show_ui_builder': True,
    'topmenu_links': [
        {'name': 'Свагер',  'url': 'swagger-ui',
            'permissions': ['auth.view_user']},
        {'name': 'Дока',  'url': 'redoc',
            'permissions': ['auth.view_user']},
    ],
    'icons': {
        'courses.course': 'fas fa-box',
        'courses.lesson': 'fas fa-book-open',
        'courses.exercise': 'fas fa-grip-horizontal',
        'users.user': 'fas fa-user',
        'auth': 'fas fa-users-cog',
        'auth.Group': 'fas fa-users-cog',
    },
    "order_with_respect_to": ['courses', 'users', 'auth'],
}

# CKEDITOR
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"
