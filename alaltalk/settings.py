"""
Django settings for alaltalk project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import json
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-*qdqs)r29%v^7$+euwdg_p2-g2fs-9w2tl)egk=4i#872*m*%9"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "channels",
    "chat",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "accounts",
    "search",
    "storages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
]

ROOT_URLCONF = "alaltalk.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

ASGI_APPLICATION = "alaltalk.asgi.application"
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}
SESSION_COOKIE_AGE = 600
SESSION_SAVE_EVERY_REQUEST = True

WSGI_APPLICATION = "alaltalk.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


#  기존 연결된 DATABASE - SQlite
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_DIR = os.path.join(BASE_DIR, "static")
print(STATIC_DIR)
STATICFILES_DIRS = [
    STATIC_DIR,
]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.CustomUser"
AUTHENTICATION_BACKENDS = ["accounts.backends.EmailBackend"]


# local_setting을 위한 설정
try:
    from alaltalk.local_settings import *
except ImportError:
    pass


# Email 전송을 위한 설정

try:
    with open(os.path.join(BASE_DIR, "alaltalk/config/email.json")) as f:
        email = json.loads(f.read())

    EMAIL_BACKEND = email["BACKEND"]
    EMAIL_HOST = email["HOST"]
    EMAIL_PORT = int(email["PORT"])
    EMAIL_HOST_USER = email["HOST_USER"]
    EMAIL_HOST_PASSWORD = email["HOST_PASSWORD"]
    EMAIL_USE_TLS = True
    EMAIL_USE_SSL = False

except FileNotFoundError:
    pass


# # # AWS S3 connet
# DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
# STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
#
#
# with open(os.path.join(BASE_DIR, "alaltalk/config/aws.json")) as f:
#     secret = json.loads(f.read())
#
# AWS_ACCESS_KEY_ID = secret["AWS"]["ACCESS_KEY_ID"]
# AWS_SECRET_ACCESS_KEY = secret["AWS"]["SECRET_ACCESS_KEY"]
# AWS_STORAGE_BUCKET_NAME = secret["AWS"]["STORAGE_BUCKET_NAME"]
# AWS_REGION = "ap-northeast-2"
# AWS_DEFAULT_ACL = "public-read"
# AWS_S3_CUSTOM_DOMAIN = "%s.s3.%s.amazonaws.com" % (AWS_STORAGE_BUCKET_NAME, AWS_REGION)


# MySQL Configuration
try:
    with open(os.path.join(BASE_DIR, "alaltalk/config/sql.json")) as f:
        sql = json.loads(f.read())

    DATABASES = {
        "default": {
            "ENGINE": sql["RDS"]["ENGINE"],
            "NAME": sql["RDS"]["NAME"],
            "USER": sql["RDS"]["USER"],
            "PASSWORD": sql["RDS"]["PASSWORD"],
            "HOST": sql["RDS"]["HOST"],
            "PORT": sql["RDS"]["PORT"],
            "OPTIONS": {
            # "init_command" : "SET sql_mode='STRICT_TRANS_TABLES'",
            }
        }
    }

except FileNotFoundError:
    pass
