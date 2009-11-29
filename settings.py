
import os

PROJECT_ROOT = os.path.dirname(__file__)

LOCAL_DEVELOPMENT = False

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ("Brian Rosner", "brosner@gmail.com"),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be avilable on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "America/Denver"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = "/static/"

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = "/media/"

AUTH_PROFILE_MODULE = 'authors.userprofile'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.load_template_source",
    "django.template.loaders.app_directories.load_template_source",
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",

    "blog.context_processors.blog",
    "blog.context_processors.stats",
)

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.doc.XViewMiddleware",

    'debug_toolbar.middleware.DebugToolbarMiddleware',

    "blog.middleware.BlogMiddleware",
)

ROOT_URLCONF = "mightylemon.urls"
INTERNAL_IPS = ('127.0.0.1',)
THEME = "oebfare"

THEME_DIR = os.path.join(PROJECT_ROOT, "themes", THEME)

TEMPLATE_DIRS = (
    #os.path.join(PROJECT_ROOT, "templates"),
    os.path.join(PROJECT_ROOT, "themes", THEME, "templates"),
)

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.realpath(os.path.join(THEME_DIR, "static"))

STATS_CODE = ""  # contains stats tracking code

INSTALLED_APPS = (
    # Blog functionality
    "blog",
    "authors",
    "links",
    "tagging",
    "comment_utils",
    "gravatar",
    "portfolio",
    "typogrify",
    "speaking",
    "codingrepo",

    # misc. extras
    "wsgi",
    "mailer",
    "django_extensions",
    "debug_toolbar",
   
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.comments",
    "django.contrib.sessions",
    "django.contrib.sites",
)

try:
    from local_settings import *
except ImportError:
    pass
