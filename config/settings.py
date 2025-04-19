"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG").lower() == "true"

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOST").split(",")


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_reportbroD.apps.ReportbrodConfig",
    "apps.base",
    "apps.users",
    "apps.biblioteca",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": os.environ.get("DATABASE_NAME"),
    #     "USER": os.environ.get("DATABASE_USER"),
    #     "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
    #     "HOST": os.environ.get("POSTGRES_HOST"),
    #     "PORT": int(os.environ.get("POSTGRES_PORT")),
    # }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "es-ar"  #'en-us'

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Mensajes personalizados de autenticación
LOGIN_ERROR_MESSAGE = "Credenciales incorrectas"

# STATIC_URL = '/static/'
# STATICFILES_DIRS = (BASE_DIR, 'static')
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

AUTH_USER_MODEL = "users.User"

AUTHENTICATION_BACKENDS = [
    'apps.biblioteca.auth.ArchivoAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]

JAZZMIN_SETTINGS = {
    "custom_index": "admin/index.html",
    "welcome_sign": "Bienvenido",
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Biblioteca",
    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Biblioteca",
    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Biblioteca",
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "img/logo.png",
    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": "img/logo.png",
    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": "img/logo.png",
    # CSS classes that are applied to the logo above
    "site_logo_classes": "",
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {
            "name": "Plantillas Reportes",
            "url": "/reportbroD",
            "permissions": [
                "reportbroD.view_reportrequest",
                "reportbroD.delete_reportrequest",
                "reportbroD.change_reportrequest",
                "reportbroD.add_reportrequest",
                "reportbroD.view_reportdefinition",
                "reportbroD.delete_reportdefinition",
                "reportbroD.change_reportdefinition",
                "reportbroD.add_reportdefinition",
            ],
        },
        {
            # "name": "Plantillas",
            # "url": "/usuarios_eventuales/",

        },
    ],
    # "order_with_respect_to": [
    #     "users",
    #     "auth",
    #     "nomina",
    #     "nomina.SalarioEscala",
    #     "nomina.Trabajador",
    #     "nomina.Asistencia",
    #     "nomina.DiaFeriado",
    #     "nomina.PlanificacionUtilidadesAnuales",
    #     "nomina.PagoPorUtilidadesAnuales",
    #     "nomina.LicenciaMaternidad",
    #     "nomina.CertificadoMedicoGeneral",
    #     "nomina.SalarioMensualTotalPagado",
    #     "reportbroD",
    # ],
    # # for the full list of 5.13.0 free icon classes
    # "icons": {
    #     "auth": "fas fa-users-cog",
    #     "users.User": "fas fa-user",
    #     "auth.Group": "fas fa-users",
    #     "auth.Permission": "fas fa-key",
    #     "nomina.SalarioEscala": "fas fa-dollar-sign",
    #     "nomina.Trabajador": "fas fas fa-user-tie",
    #     "nomina.Asistencia": "fas fas fa-walking",
    #     "nomina.PlanificacionUtilidadesAnuales": "fas fa-chalkboard-teacher",
    #     "nomina.PagoPorUtilidadesAnuales": "fas  fa-hand-holding-usd",
    #     "nomina.LicenciaMaternidad": "fas fa-baby-carriage",
    #     "nomina.CertificadoMedicoGeneral": "fas fa-user-md",
    #     "nomina.SalarioMensualTotalPagado": "fas fa-money-check-alt",
    #     "nomina.DiaFeriado": "fas fa-gifts",
    # },
    # Icons that are used when one is not manually specified
    # "default_icon_parents": "fas fa-chevron-circle-right",
}
JAZZMIN_UI_TWEAKS = {
    "theme": "default",
}

DJANGO_SUPERUSER_USERNAME = os.environ.get("DJANGO_SUPERUSER_USERNAME")
DJANGO_SUPERUSER_PASSWORD = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
DJANGO_SUPERUSER_EMAIL = os.environ.get("DJANGO_SUPERUSER_EMAIL")
DJANGO_SUPERUSER_FIRST_NAME = os.environ.get("DJANGO_SUPERUSER_FIRST_NAME")
DJANGO_SUPERUSER_LAST_NAME = os.environ.get("DJANGO_SUPERUSER_LAST_NAME")
