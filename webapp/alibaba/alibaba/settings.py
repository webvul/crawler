# coding=utf-8
"""
Django settings for crawler project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

try:
    from local_settings import *
except ImportError:
    print "Don't have local settings"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8w81chmmaumpd=a6wkbzzt5y9_a-+!yf%v754+efejkb13&oo@'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": CACHES_LOCATION,
        'KEY_PREFIX': 'alibaba.',
        'TIMEOUT': 300,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
            "SOCKET_TIMEOUT": 5,  # in seconds
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
        }
    }
}

AUTH_USER_MODEL = 'auth.User'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# SECURITY WARNING: don't run with debug turned on in production!

TEMPLATE_DEBUG = DEBUG

MANAGERS = ADMINS

ALLOWED_HOSTS = ["www.yueguangba.com"]

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'silk.middleware.SilkyMiddleware',
    'userena.middleware.UserenaLocaleMiddleware',
    # 'django.middleware.security.SecurityMiddleware',
)

# Application definition

ROOT_URLCONF = 'alibaba.urls'

TEMPLATES_DIRS = (os.path.join(BASE_DIR, "templates").replace('\\', '/'),)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates").replace('\\', '/'),  # insert your TEMPLATE_DIRS here
        ],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.core.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                # insert your TEMPLATE_LOADERS here
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ]
        },
    },
]

WSGI_APPLICATION = 'alibaba.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
        'CHARSET': 'utf8'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh_CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = False

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

if not LOGGING:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'alibaba',
    }
}

FIRST_DAY_OF_WEEK = 1

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
SESSION_COOKIE_DOMAIN = "www.yueguangba.com"
SESSION_COOKIE_AGE = 86400

from django.contrib.messages import constants as message_constants

MESSAGE_LEVEL = message_constants.DEBUG

FILE_UPLOAD_TEMP_DIR = "/tmp"
EMAIL_TIMEOUT = 5

DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i'
TIME_FORMAT = 'H:i'

DJANGO_REDIS_IGNORE_EXCEPTIONS = True

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.contrib.douban.DoubanBackend2',
    'social_auth.backends.contrib.qq.QQBackend',
    'social_auth.backends.contrib.weibo.WeiboBackend',
    'social_auth.backends.contrib.renren.RenRenBackend',
    'social_auth.backends.contrib.baidu.BaiduBackend',
    'social_auth.backends.contrib.weixin.WeixinBackend',
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    # 必须加，否则django默认用户登录不上
    'django.contrib.auth.backends.ModelBackend',
)
INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'silk',
    'social_auth',
    'alibaba',
    'guardian',
    'userena',
    'userena.contrib.umessages',
    'accounts',
    'search',
    'scraper',
    "captcha",
    'djcelery'

)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    # login 在template中可以用 "{% url socialauth_begin 'douban-oauth2' %}"
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)

SUIT_CONFIG = {
    'ADMIN_NAME': u'搜索',
    'LIST_PER_PAGE': 50
}

import djcelery

djcelery.setup_loader()

BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_BACKEND = "alibaba"
BROKER_USER = "guest"
BROKER_PASSWORD = "guest"
BROKER_VHOST = "/"
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

LOCAL_HOST = "192.168.234.139"
MONGO_HOST = LOCAL_HOST
MONGO_PORT = 27017

import pymongo

MONGO_CLIENT = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)

ANONYMOUS_USER_ID = -1

SITE_ID = 1

LOGIN_URL = '/accounts/%(username)s/'
LOGIN_REDIRECT_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'
AUTH_PROFILE_MODULE = 'accounts.Profile'
USERENA_DISABLE_PROFILE_LIST = True
USERENA_MUGSHOT_SIZE = 100
USERENA_FORBIDDEN_USERNAMES = "('signup', 'signout', 'signin', 'activate', 'me', 'password')"
USERENA_DISABLE_SIGNUP = False
USERENA_HIDE_EMAIL= False
USERENA_HTML_EMAIL = True

# SILKY_PYTHON_PROFILER = True
# SILKY_AUTHENTICATION = True  # User must login
# SILKY_AUTHORISATION = True  # User must have permissions
# SILKY_MAX_REQUEST_BODY_SIZE = -1  # Silk takes anything <0 as no limit
# SILKY_MAX_RESPONSE_BODY_SIZE = 1024  # If response body>1024kb, ignore
SILKY_META = True
# SILKY_INTERCEPT_PERCENT = 50  # log only 50% of requests
# def my_custom_logic(request):
#     return 'record_requests' in request.session
#
# SILKY_INTERCEPT_FUNC = my_custom_logic # log only session has recording enabled.
# SILKY_DYNAMIC_PROFILING = [{
#     'module': 'path.to.module',
#     'function': 'foo',
#     # Line numbers are relative to the function as opposed to the file in which it resides
#     'start_line': 1,
#     'end_line': 2,
#     'name': 'Slow Foo'
# }]

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',

    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.misc.save_status_to_session',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
    'social_auth.backends.pipeline.misc.save_status_to_session',
)

SOCIAL_AUTH_DISCONNECT_PIPELINE = (
    'social.pipeline.disconnect.allowed_to_disconnect',
    'social.pipeline.disconnect.get_entries',
    'social.pipeline.disconnect.revoke_tokens',
    'social.pipeline.disconnect.disconnect'
)
SSOCIAL_AUTH_SANITIZE_REDIRECTS = False
# LOGIN_REDIRECT_URL = 'http://www.yueguangba.com/'
SOCIAL_AUTH_WEIBO_LOGIN_REDIRECT_URL = 'http://www.yueguangba.com/'
SOCIAL_AUTH_LOGIN_URL = '/login-url/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/login-error/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/logged-in/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-users-redirect-url/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/oauth/newassociation'
SOCIAL_AUTH_BACKEND_ERROR_URL = '/new-error-url'
SOCIAL_AUTH_AUTHENTICATION_SUCCESS_URL = '/oauth/authentication/success'

SOCIAL_AUTH_WEIBO_KEY = '123592348'
SOCIAL_AUTH_WEIBO_SECRET = 'aa8626a4396ab90366e51292baeaeb1e'

SOCIAL_AUTH_QQ_KEY = '101145292'
SOCIAL_AUTH_QQ_SECRET = '993fbbc3c7d9ed0b3a95b613c39f918d'
SOCIAL_AUTH_QQ_FIELDS_STORED_IN_SESSION = ['auth过程中的附加参数']

SOCIAL_AUTH_DOUBAN_OAUTH2_KEY = '0630fb0303a5947e1292f1090af0bd7a'
SOCIAL_AUTH_DOUBAN_OAUTH2_SECRET = 'e92927cfa3cefe4f'

SOCIAL_AUTH_WEIBO_AUTH_EXTRA_ARGUMENTS = {'forcelogin': 'true'}
SOCIAL_AUTH_WEIBO_FIELDS_STORED_IN_SESSION = ['auth过程中的附加参数']

SOCIAL_AUTH_RENREN_KEY = ''
SOCIAL_AUTH_RENREN_SECRET = ''

SOCIAL_AUTH_BAIDU_KEY = ''
SOCIAL_AUTH_BAIDU_SECRET = ''

SOCIAL_AUTH_WEIXIN_KEY = ''
SOCIAL_AUTH_WEIXIN_SECRET = ''
SOCIAL_AUTH_WEIXIN_SCOPE = ['snsapi_login',]

CAPTCHA_LENGTH = 6
CAPTCHA_DICTIONARY_MIN_LENGTH = CAPTCHA_DICTIONARY_MAX_LENGTH = 6
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.word_challenge'

from elasticsearch import Elasticsearch

ES = Elasticsearch(ES_HOST, timeout=50)
from django_redis import get_redis_connection
REDIS = get_redis_connection("default")
