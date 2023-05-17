"""
Django settings for Sal_website project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from distutils.debug import DEBUG
import os
from urllib.parse import urlparse
from dotenv import load_dotenv


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# This loads the environment keys
load_dotenv(verbose=True, dotenv_path=os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False") == "True"
# DEBUG = True

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = [os.getenv("DJANGO_ALLOWED_HOSTS"),"127.0.0.1","localhost","167.71.106.235","68.183.143.170","32.213.8.188","24.60.248.41","108.30.157.162", "192.168.1.69",
                 "74.71.89.122","24.97.185.90", "98.113.160.98", "74.71.90.175", "74.71.79.251", "testserver", "findfreefare.com", "127.0.0.1:8000"]
                         
# ['freefoodsal.com', 'www.freefoodsal.com', '167.71.106.235', 'http://127.0.0.1:8000']
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.',
    'main.apps.MainConfig',
    'materializecssform',
    'widget_tweaks',
    'address',
    'crispy_forms',
    'recurrence',
    'multiselectfield',
    'rest_framework',
    'escapejson',
    'django_extensions',
    'oauth2_provider',
    'social_django',
    # 'social_django_mongoengine',
    'drf_social_oauth2',
    'corsheaders',
    # "registration",

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


APPEND_SLASH =  True
TRAILING_SLASH = False
ROOT_URLCONF = 'Sal_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'main/Templates')],
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

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'defaultdb',
        'USER' : 'doadmin',
        'PASSWORD': 'AVNS_0rub7t86vsLNkona9PY',
        'HOST' : 'db-postgresql-nyc3-88337-do-user-11366552-0.b.db.ondigitalocean.com',
        # 'HOST': 'localhost:3000',
        'PORT' : '25060',
                'TEST': {
            'NAME': 'test_postdb',
        },
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




PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'


PROJECT_DIR_ABOVE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
# print(PROJECT_DIR_ABOVE)


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'Sal_django_site/main/static'),
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
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'drf_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

REST_FRAMEWORK = {
   'DEFAULT_AUTHENTICATION_CLASSES': (
       'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  
       'drf_social_oauth2.authentication.SocialAuthentication',
   )
}
CORS_ALLOWED_ORIGINS = [
   "http://localhost:3000",
   "http://127.0.0.1:3000"
]

# Defining Soc_auth characteristics
# https://www.digitalocean.com/community/tutorials/django-authentication-with-facebook-instagram-and-linkedin
LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/logout'
LOGOUT_REDIRECT_URL = '/login'

# [...]

SOCIAL_AUTH_URL_NAMESPACE = 'social'
# SOCIAL_AUTH_STORAGE = 'social_django_mongoengine.models.DjangoStorage'
# [...]

SOCIAL_AUTH_FACEBOOK_KEY = os.getenv('SOCIAL_AUTH_FACEBOOK_KEY')      # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv('SOCIAL_AUTH_FACEBOOK_SECRET') # App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email'] 

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {       
  'fields': 'id, name, email'
}
SOCIAL_AUTH_USER_FIELDS=['email','password','your_name',]
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [                 
    ('name', 'name'),
    ('email', 'email'),
]

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'main.utils.cleanup_social_account',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'main.utils.create_profile'  #Custom pipeline
)

# [...]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY') #client id
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET') #client password

# SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email']
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
   'https://www.googleapis.com/auth/userinfo.email',
   'https://www.googleapis.com/auth/userinfo.profile',
]
# [...]
# TAKENOTE this library is for fromatting forms. might be useful editing the profiles 'materializecssform'
#https://pypi.org/project/django-materializecss-form/



ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'


# [...]
# The following is for developing our email backend
# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html#sign-up-with-confirmation-mail
# also this:
# https://docs.djangoproject.com/en/dev/topics/email/



# [...]
# The following is another try at developing our email backend
# https://django-registration.readthedocs.io/en/3.1/quickstart.html#default-form-template

ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'salhateswaste@gmail.com'
EMAIL_HOST_USER= os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD= os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587


# Password reset settings
PASSWORD_RESET_TIMEOUT_DAYS = 2



GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
