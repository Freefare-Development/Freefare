"""
Django settings for Sal_website project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from dotenv import load_dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# This loads the environment keys
load_dotenv(verbose=True, dotenv_path=os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['freefoodsal.com', 'www.freefoodsal.com', '167.71.106.235']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    'social_django',
    'materializecssform',
    'widget_tweaks',
    'address',
    'crispy_forms',
    'recurrence',
    'multiselectfield',
    'rest_framework',
    'escapejson',

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

ROOT_URLCONF = 'Sal_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
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

WSGI_APPLICATION = 'Sal_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATICFILES_DIRS = [
    # os.path.join(PROJECT_DIR, 'static'),
    os.path.join(BASE_DIR, 'node_modules'),
    ('google','node_modules/@google'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'main/media')
# User substitution
#  https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#auth-custom-user
# AUTH_USER_MODEL = 'auth.User'
AUTH_USER_MODEL = 'main.CustomUser'


# Social Signin backends
# https://python-social-auth.readthedocs.io/en/latest/configuration/django.html
AUTHENTICATION_BACKENDS = [
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    # 'social_core.backends.twitter.TwitterOAuth',
    # 'social_core.backends.yahoo.YahooOpenId',
    'social_core.backends.facebook.FacebookOAuth2',
    # 'social_core.backends.linkedin.LinkedinOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]


# Defining Soc_auth characteristics
# https://www.digitalocean.com/community/tutorials/django-authentication-with-facebook-instagram-and-linkedin
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login'

# [...]

SOCIAL_AUTH_URL_NAMESPACE = 'social'

# [...]

SOCIAL_AUTH_FACEBOOK_KEY = os.getenv('SOCIAL_AUTH_FACEBOOK_KEY')      # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv('SOCIAL_AUTH_FACEBOOK_SECRET') # App Secret
# SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_link'] 
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email'] 
# SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {       
#   'fields': 'id, name, email, picture.type(large), link'
# }
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {       
  'fields': 'id, name, email'
}

SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [                 
    ('name', 'name'),
    ('email', 'email'),
    # ('picture', 'picture'),
    # ('link', 'profile_url'),
]


# [...]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY') #client id
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET') #client password

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email']
# [...]
# TAKENOTE this library is for fromatting forms. might be useful editing the profiles 'materializecssform'
#https://pypi.org/project/django-materializecss-form/


# INSTALLED_APPS = (
#      'materializecssform',
#      ...
#      )

# [...]
# The following is for developing our email backend
# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html#sign-up-with-confirmation-mail
# also this:
# https://docs.djangoproject.com/en/dev/topics/email/

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'salhateswaste@gmail.com'
# EMAIL_HOST = 'smtp.sendgrid.net' # new
# EMAIL_HOST_USER = 'apikey' # new
# EMAIL_HOST_PASSWORD = '<sendgrid_password>' # new
# EMAIL_PORT = 587 # new
# EMAIL_USE_TLS = True # new

# [...]
# The following is another try at developing our email backend
# https://django-registration.readthedocs.io/en/3.1/quickstart.html#default-form-template

ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER= os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD= os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
PASSWORD_RESET_TIMEOUT_DAYS = 2



GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
