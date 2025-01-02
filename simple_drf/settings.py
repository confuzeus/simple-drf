from pathlib import Path

import environ
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()

if env.bool("READ_DOT_ENV", True):
    env_file = BASE_DIR / "appconfig.env"
    if not env_file.is_file():
        raise ImproperlyConfigured(f"appconfig.env not found in {BASE_DIR}")

    environ.Env.read_env(str(env_file))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG", False)

TEST = env.bool("DJANGO_TEST", False)

PROJECT_NAME = "Simple DRF"

DOMAIN_NAME = env.str("DJANGO_DOMAIN_NAME", "example.com")

PORT_NUMBER = env.int("DJANGO_SITE_PORT_NUMBER")

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

# https://docs.djangoproject.com/en/3.2/ref/settings/#language-code
LANGUAGE_CODE = "en-us"

LANGUAGES = (("en", _("English")),)

TIME_ZONE = "UTC"

# https://docs.djangoproject.com/en/3.2/ref/settings/#use-i18n
USE_I18N = True

# https://docs.djangoproject.com/en/3.2/ref/settings/#use-l10n
USE_L10N = True

# https://docs.djangoproject.com/en/3.2/ref/settings/#use-tz
USE_TZ = True

# https://docs.djangoproject.com/en/3.2/ref/settings/#site-id
SITE_ID = 1

# https://docs.djangoproject.com/en/3.2/ref/settings/#locale-paths
LOCALE_PATHS = [
    BASE_DIR / "locale",
]

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": env.str("DB_PATH"),
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/ref/settings/#root-urlconf
ROOT_URLCONF = "simple_drf.urls"

# https://docs.djangoproject.com/en/3.2/ref/settings/#wsgi-application
WSGI_APPLICATION = "simple_drf.wsgi.application"

# APPS
# ------------------------------------------------------------------------------
django_apps = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.admin",
    "django.contrib.sitemaps",
    "django.forms",
]
third_party_apps = [
    "django_extensions",
    "allauth",
    "allauth.account",
    "allauth.headless",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "rest_framework",
]

local_apps = [
    "simple_drf.core",
    "simple_drf.accounts",
]
# https://docs.djangoproject.com/en/3.2/ref/settings/#installed-apps
INSTALLED_APPS = django_apps + third_party_apps + local_apps

if DEBUG or TEST:
    INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-user-model
AUTH_USER_MODEL = "accounts.User"
# https://docs.djangoproject.com/en/3.2/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "/"
# https://docs.djangoproject.com/en/3.2/ref/settings/#login-url
LOGIN_URL = reverse_lazy("account_login")

# Allauth

ACCOUNT_AUTHENTICATION_METHOD = "email"

ACCOUNT_CONFIRM_EMAIL_ON_GET = True

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = "optional"

ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_CHANGE_EMAIL = True

ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

ACCOUNT_LOGIN_ON_PASSWORD_RESET = True

SOCIALACCOUNT_EMAIL_AUTHENTICATION = True

SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT = True

SOCIALACCOUNT_LOGIN_ON_GET = True

HEADLESS_FRONTEND_URLS = {
    "account_confirm_email": env.str("ALLAUTH_ACCOUNT_CONFIRM_EMAIL_URL"),
    "account_reset_password": env.str("ALLAUTH_ACCOUNT_RESET_PASSWORD_URL"),
    "account_reset_password_from_key": env.str(
        "ALLAUTH_ACCOUNT_RESET_PASSWORD_FROM_KEY_URL"
    ),
    "account_signup": env.str("ALLAUTH_ACCOUNT_SIGNUP_URL"),
    "socialaccount_login_error": env.str("ALLAUTH_SOCIALACCOUNT_LOGIN_ERROR_URL"),
}

HEADLESS_ONLY = True

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/ref/settings/#password-hashers
if DEBUG or TEST:
    PASSWORD_HASHERS = [
        "django.contrib.auth.hashers.MD5PasswordHasher",
    ]
else:
    PASSWORD_HASHERS = [
        # https://docs.djangoproject.com/en/3.2/topics/auth/passwords/#using-argon2-with-django
        "django.contrib.auth.hashers.Argon2PasswordHasher",
        "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
        "django.contrib.auth.hashers.PBKDF2PasswordHasher",
        "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    ]

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        # noqa: E501
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

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

# STATIC
# ------------------------------------------------------------------------------
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# https://docs.djangoproject.com/en/3.2/ref/settings/#static-root
STATIC_ROOT = env.str("DJANGO_STATIC_ROOT", str(BASE_DIR / "static_collected"))

# https://docs.djangoproject.com/en/3.2/ref/settings/#static-url
STATIC_URL = "/static/"

# https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/ref/settings/#media-root
MEDIA_ROOT = Path(env.str("DJANGO_MEDIA_ROOT", str(BASE_DIR / "media")))

# https://docs.djangoproject.com/en/3.2/ref/settings/#media-url

if DEBUG or TEST:
    MEDIA_URL = "/media/"
else:
    MEDIA_URL = env.str("DJANGO_MEDIA_URL")

template_loaders = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

if DEBUG is False:
    template_loaders = [("django.template.loaders.cached.Loader", template_loaders)]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
            ],
            "debug": DEBUG or TEST,
            "loaders": template_loaders,
        },
    },
]

# https://docs.djangoproject.com/en/3.2/ref/settings/#form-renderer
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# SECURITY
# ------------------------------------------------------------------------------
SECRET_KEY = env.str("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")

CSRF_TRUSTED_ORIGINS = env.list("DJANGO_CSRF_TRUSTED_ORIGINS", [])

SESSION_COOKIE_DOMAIN = env.str("DJANGO_SESSION_COOKIE_DOMAIN")

CSRF_COOKIE_DOMAIN = env.str("DJANGO_CSRF_COOKIE_DOMAIN")

if not DEBUG:
    # https://docs.djangoproject.com/en/3.2/ref/settings/#session-cookie-httponly
    SESSION_COOKIE_HTTPONLY = True

    # https://docs.djangoproject.com/en/3.2/ref/settings/#session-engine
    SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

    # https://docs.djangoproject.com/en/3.2/ref/settings/#csrf-cookie-httponly
    CSRF_COOKIE_HTTPONLY = False

    # https://docs.djangoproject.com/en/3.2/ref/settings/#secure-browser-xss-filter
    SECURE_BROWSER_XSS_FILTER = True

    # https://docs.djangoproject.com/en/3.2/ref/settings/#x-frame-options
    X_FRAME_OPTIONS = "DENY"

    # https://docs.djangoproject.com/en/3.2/ref/settings/#secure-proxy-ssl-header
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    # https://docs.djangoproject.com/en/3.2/ref/settings/#session-cookie-secure
    SESSION_COOKIE_SECURE = True

    # https://docs.djangoproject.com/en/3.2/ref/settings/#csrf-cookie-secure
    CSRF_COOKIE_SECURE = True

    # https://docs.djangoproject.com/en/3.2/topics/security/#ssl-https
    # https://docs.djangoproject.com/en/3.2/ref/settings/#secure-hsts-seconds
    SECURE_HSTS_SECONDS = 518400

    # https://docs.djangoproject.com/en/3.2/ref/settings/#secure-hsts-include-subdomains
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    # https://docs.djangoproject.com/en/3.2/ref/settings/#secure-hsts-preload
    SECURE_HSTS_PRELOAD = True

    # https://docs.djangoproject.com/en/3.2/ref/middleware/#x-content-type-options-nosniff
    SECURE_CONTENT_TYPE_NOSNIFF = True

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/ref/settings/#email-backend
DEFAULT_FROM_EMAIL = env.str(
    "DJANGO_DEFAULT_FROM_EMAIL", "Simple DRF <hello@example.com>"
)

SERVER_EMAIL = env.str("DJANGO_SERVER_EMAIL", DEFAULT_FROM_EMAIL)

EMAIL_SUBJECT_PREFIX = env.str("DJANGO_EMAIL_SUBJECT_PREFIX", "[Simple DRF]")

if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = env.str("DJANGO_SMTP_HOST", "localhost")
    EMAIL_PORT = env.int("DJANGO_SMTP_PORT", 1025)
else:
    EMAIL_BACKEND = "anymail.backends.amazon_ses.EmailBackend"
    ANYMAIL = {
        "AMAZON_SES_CLIENT_PARAMS": {
            "aws_access_key_id": env.str("DJANGO_AWS_ACCESS_KEY_ID"),
            "aws_secret_access_key": env.str("DJANGO_AWS_SECRET_ACCESS_KEY"),
            "region_name": env.str("DJANGO_AWS_REGION_NAME"),
            "config": {
                "connect_timeout": 30,
                "read_timeout": 30,
            },
        },
    }

# https://docs.djangoproject.com/en/3.2/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = env.str("DJANGO_ADMIN_URL")

# https://docs.djangoproject.com/en/3.2/ref/settings/#admins
ADMINS = [("""Josh Karamuth""", "hello@example.com")]
# https://docs.djangoproject.com/en/3.2/ref/settings/#managers
MANAGERS = ADMINS

# Logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "million_timer": {
            "level": "DEBUG",
            "handlers": ["console"],
        },
    },
}

if not DEBUG:
    LOGGING["loggers"]["simple_drf"]["level"] = "INFO"

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/ref/settings/#caches

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
    }
}

# Django Extensions

SHELL_PLUS_IMPORTS = [
    "from simple_drf.accounts.tests import factories as accounts_factories",
]

SHELL_PLUS_PRINT_SQL = True