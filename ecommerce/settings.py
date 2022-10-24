"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)x^n81w5+jwpoo2d40k=0-ru$eh2h-@#e%b)45t^&**18lx5wq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','52.198.55.170']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentications',
    'products',
    'frontside',
    'accountmanage',
    'widget_tweaks'
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

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['template'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'frontside.context_processors.menulinks',
                'frontside.context_processors.cartcount',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'
AUTH_USER_MODEL='authentications.Account'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
   'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'project',

        'USER': 'jithin',

        'PASSWORD': 'jithinrs',

        'HOST': 'localhost',

        'PORT': '',

    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

ACCOUNT_SID='AC88d1b4e0e16cd6bb345b62a6148060bb'
AUTH_TOKEN = '18b5a09dc609142c162ffebf4a81670f'
SERVICES_ID='VA4840bc38f8b8963adc0d7ae1519b3443'

# ACCOUNT_SID='ACee8fb23615caf7ea6d7ba1c33294891a'
# AUTH_TOKEN='dbe1b62ac3d24ca5f72f7b060be235dd'
# SERVICES_ID='MG367abf4e1e8a7a8479a32441f1ae75f4'



MEDIA_URL="/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,"media")
