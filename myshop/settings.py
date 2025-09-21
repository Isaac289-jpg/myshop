"""
Django settings for myshop project.
"""

from pathlib import Path
import os  

BASE_DIR = Path(__file__).resolve().parent.parent

# Use environment variable for secret key
SECRET_KEY = os.environ.get("SECRET_KEY", "fallback-key-for-local")

# Debug is ON locally, OFF in production
DEBUG = os.environ.get("DEBUG", "False") == "True"

# ✅ Allow Render subdomains + local development
ALLOWED_HOSTS = [
    ".onrender.com",   # matches any Render subdomain
    "localhost",
    "127.0.0.1",
]

# ✅ Allow requests from frontend + backend for CSRF
CSRF_TRUSTED_ORIGINS = [
    "https://myshop-1-y53w.onrender.com",
    "https://id-preview--bd86b5db-53bd-4025-9968-7d1608ae5fc1.lovable.app",
]

# Application definition
INSTALLED_APPS = [
    # Default Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party apps
    "corsheaders",        # for CORS
    "django_extensions",  # for show_urls command

    # Your apps
    "shop",  # replace 'shop' with your actual app name if different
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # must be near the top
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "myshop.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "myshop.wsgi.application"


# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static files
STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ✅ CORS configuration (important for frontend-backend connection)
CORS_ALLOWED_ORIGINS = [
    "https://id-preview--bd86b5db-53bd-4025-9968-7d1608ae5fc1.lovable.app",  # Lovable frontend
]

# ✅ Allow credentials (needed for CSRF cookies + auth)
CORS_ALLOW_CREDENTIALS = True
