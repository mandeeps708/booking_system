"""
Django settings for bookingsystem project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Here BASE_DIR points to the src directory

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nr644jy+j(k6m9osgmx-*sgh+^qj5t)%kn3tu$vx9rvm4uau1%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Templates Location
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "templates"),
)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bookingsystem.urls'

WSGI_APPLICATION = 'bookingsystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

"""
Enter the database name, your mysql username and password
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bookingsystem',
        'USER': 'root',
        'PASSWORD':'1234',
        'HOST': 'localhost' ,
        'PORT': '',
    }
}


"""
This will automatically redirect to the login_url if the user is not logged in, it is called when using @login_required
"""
LOGIN_URL = '/login/'
# LOGIN_REDIRECT_URL = '/'

"""
This is used to specify the time format in H:M and H:M AM/PM.
"""
TIME_INPUT_FORMATS = ['%H:%M', '%I:%M%p', '%I:%M %p']

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (
        os.path.join(os.path.dirname(BASE_DIR), "static"),
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

#For email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True

EMAIL_HOST = 'smtp.gmail.com'

#replace your email within the quotes below.
EMAIL_HOST_USER = 'ramanvirdiz@gmail.com'

"""Must generate specific password for your app in [gmail settings] after activating 
2-step verfication."""
EMAIL_HOST_PASSWORD = 'hdobsbudnetdycqp'

EMAIL_PORT = 587

#This did the trick
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
