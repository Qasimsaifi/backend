import os
from pathlib import Path
from datetime import timedelta

import cloudinary

# Add your Cloudinary credentials
cloudinary.config(
    cloud_name="dehpkgdw5",
    api_key="338538795738672",
    api_secret="6gRybYadzcKdC2FnyijAuhIhwLc",
)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-^*k^z%#w=-wa87c_s#l#v0c)3)3$neqoawp$4yalw1au8cq+)!"
DEBUG = True
ALLOWED_HOSTS = ["*"]

CORS_ORIGIN_WHITELIST = [
    "https://devdox.up.railway.app",
    "http://localhost:5173",
    "https://devdox.vercel.app",
    "http://127.0.0.1:5500",
    "http://localhost:3000",
    "https://kasimsaifi.tech",
    "https://devdox.kasimsaifi.tech",
    "https://backend.kasimsaifi.tech",



    # Add other trusted origins as needed
]
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Use the SMTP backend

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587

EMAIL_USE_TLS = True  # Use TLS for secure connection
EMAIL_HOST_USER = 'kasimthecoder@gmail.com'  # Your email address
EMAIL_HOST_PASSWORD = 'qmpvcudrfzahvnih'  # Your email password


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "django_filters",
    "cloudinary",
    "corsheaders",
    "whitenoise.runserver_nostatic",
    "tinymce",
    "snippets",
    "accounts",
    'portfolio',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "blogapi.urls"
AUTH_USER_MODEL = "accounts.User"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "blogapi.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "railway",
        "USER": "postgres",
        "PASSWORD": "dASzvj9KonJmQZ2qAMKC",
        "HOST": "containers-us-west-148.railway.app",
        "PORT": "7403",
    }
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        # Other authentication classes...
    ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

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
USE_TZ = True

CSRF_TRUSTED_ORIGINS = [
    "https://devdox.up.railway.app",
    "https://devdox.vercel.app",
    ".now.sh",
    ".vercel.app",
    "http://127.0.0.1:800",
    "http://127.0.0.1:5500",
    "http://localhost:3000",
    "https://kasimsaifi.tech",
    "https://devdox.kasimsaifi.tech",
    "https://backend.kasimsaifi.tech",


    
    
    # Add other trusted origins as needed
]

TINYMCE_DEFAULT_CONFIG = {
    "height": 600,
    "width": 900,
    "plugins": "image  media  code  emoticons  link  preview lists  wordcount  codesample  fullscreen ",
    "toolbar": "undo redo | formatselect | bold italic codesample wordcount| alignleft aligncenter alignright emoticons link table view | image media numlist bullist| code preview",
}
CORS_ALLOW_HEADERS = (
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
)
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)
STATIC_URL = "/static/"
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles_build" , 'static')
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=62),
    "ROTATE_REFRESH_TOKEN": True,
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
