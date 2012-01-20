try:
    import json
    with open('/home/dotcloud/environment.json') as f:
        env = json.load(f)
    LOCAL_DEVELOPMENT = False
except IOError:  # Local development---not on DotCloud
    LOCAL_DEVELOPMENT = True

import os
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

#ADMINS = (
#    try:
#        # ('Your Name', 'your_email@example.com'),
#        (env['ADMIN_NAME'], env['ADMIN_EMAIL']),
#    except NameError, KeyError:
#        pass
#)
#
#MANAGERS = ADMINS

if not LOCAL_DEVELOPMENT:
    # Do not alter these values under normal circumstances:
    DOTCLOUD_DB = {
        'default': {
            'ENGINE':  'django.db.backends.postgresql_psycopg2',
            'NAME':    'template1',
            'USER':     env['DOTCLOUD_DB_SQL_LOGIN'],
            'PASSWORD': env['DOTCLOUD_DB_SQL_PASSWORD'],
            'HOST':     env['DOTCLOUD_DB_SQL_HOST'],
            'PORT':     int(env['DOTCLOUD_DB_SQL_PORT']),
        }
    }
    DATABASES = DOTCLOUD_DB

### Enter your local database information in local_settings.py
### An example_local_settings.py exists to give you an idea of
### how to set it up

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/home/dotcloud/data/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
# STATIC_ROOT shouldn't contain anything that isn't generated by collectstatic.
STATIC_ROOT = '/home/dotcloud/data/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    PROJECT_PATH + '/static/',
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
try:
    SECRET_KEY
except NameError:
    SECRET_FILE = os.path.join(PROJECT_PATH, 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            from random import choice
            SECRET_KEY = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            secret = file(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            Exception('Please create a %s file with random characters \
            to generate your secret key!' % SECRET_FILE)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
#    'djangosecure.middleware.SecurityMiddleware', # https
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'hellodjango.urls'

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates/',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'django.contrib.admin',
    'django.contrib.admindocs',
    'forum',
    'django.contrib.markup',
#    'django_bcrypt',
    'userena', 'guardian', 'easy_thumbnails', # userena
#    'djangosecure', # https
)

# Extension of the User model with forum-related fields in models.py
AUTH_PROFILE_MODULE = 'forum.UserProfile'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
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

### PONY-FORUM APP
## These already have default values, so you don't need to define them
# POSTS_PER_PAGE        =
# THREADS_PER_PAGE      =
# USER_CONTENT_PER_PAGE =

### E-MAIL SERVER
## http://sontek.net/using-gmail-to-send-e-mails-from-django
if not LOCAL_DEVELOPMENT:
    try:
        EMAIL_HOST           = env['EMAIL_HOST']
        EMAIL_HOST_USER      = env['EMAIL_HOST_USER']
        EMAIL_HOST_PASSWORD  = env['EMAIL_HOST_PASSWORD']
        EMAIL_PORT           = int(env['EMAIL_PORT'])
        EMAIL_USE_TLS        = bool(env['EMAIL_USE_TLS'])
    #    EMAIL_SUBJECT_PREFIX = ""  # Doesn't work, optional
    except KeyError:  # E-mail settings have not been entered
    #    raise KeyError("""You need to enter your e-mail server settings.
    #    A guide is available in the README at https://github.com/ndarville/dotcloud-django
    #    """)
        pass

### USERENA APP
ANONYMOUS_USER_ID = -1.

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = '/'
LOGIN_URL          = '/accounts/login/'
LOGOUT_URL         = '/accounts/logout/'

USERENA_ACTIVATION_REQUIRED  = True  # Set to False when debugging
USERENA_DEFAULT_PRIVACY      = 'open'
USERENA_DISABLE_PROFILE_LIST = True
USERENA_FORBIDDEN_USERNAMES  = ('activate', 'login', 'logout', 'me',\
                                'password', 'register', 'signin',\
                                'signout', 'signup')
USERENA_MUGSHOT_GRAVATAR     = False

### DJANGO-SECURE HTTPS
# if not LOCAL_DEVELOPMENT:
    # SECURE_SSL_REDIRECT = True
    # SECURE_FRAME_DENY = True
    # SECURE_BROWSER_XSS_FILTER
    # SESSION_COOKIE_SECURE, SESSION_COOKIE_HTTPONLY = True, True
    # SECURE_HSTS_SECONDS = 1

### BCRYPT APP, if used
BCRYPT_MIGRATE = True
BCRYPT_ROUNDS  = 16
###

try:
    LOCAL_SETTINGS
except NameError:
    try:
        from local_settings import *
    except ImportError:
        pass
