from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config("SECRET_KEY")


DEBUG = True

ALLOWED_HOSTS = ["realest.up.railway.app"]

CSRF_TRUSTED_ORIGINS = ["https://realest.up.railway.app"]

INSTALLED_APPS = [
    "accounts.apps.AccountsConfig",
    "realtors.apps.RealtorsConfig",
    "listings.apps.ListingsConfig",
    "pages.apps.PagesConfig",
    "contacts.apps.ContactsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "realest.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [Path.joinpath(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "realest.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("PGDATABASE"),
        "USER": config("PGUSER"),
        "PASSWORD": config("PGPASSWORD"),
        "HOST": config("PGHOST"),
        "PORT": config("PGPORT"),
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"


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


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_ROOT = Path.joinpath(BASE_DIR, "static")
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    Path.joinpath(BASE_DIR, "realest/static"),
]


MEDIA_ROOT = Path.joinpath(BASE_DIR, "media")
MEDIA_URL = "/media/"

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {messages.ERROR: "danger"}

# EMAIL_HOST = config("EMAIL_HOST")
# EMAIL_PORT = config("EMAIL_PORT")
# EMAIL_HOST_USER = config("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
# EMAIL_USE_TLS = True
