# Project uyuchun
# Django v3.1.4

# Imports
from pathlib import Path
import os
# End Imports


# Config
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = '@my8&l^^re=2bz(mc9y@lv*a725g-j#655eikbr7^+3w#o24gd'
DEBUG = True
ALLOWED_HOSTS = ['*', ]
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainapp.apps.MainappConfig',
    'admin.apps.AdminConfig',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'uyuchun.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'uyuchun.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'uyuchun',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'OPTIONS': {
               'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
               'charset': 'utf8mb4',
        }
    }
}
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
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Asia/Samarkand'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# StaticAndMedia
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'mainapp/static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mainapp/media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)
# End StaticAndMedia

# End Config
