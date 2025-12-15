import os
from pathlib import Path
from decouple import config, Csv
import dj_database_url

# --- CAMINHOS ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SEGURANÇA (VPS & Produção) ---
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
# Permite acesso do seu domínio e localhost
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# --- APLICAÇÕES ---
INSTALLED_APPS = [
    'unfold',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Libs de Terceiros
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',

    # Apps do PipLy (Vamos criar a seguir)
    'apps.dashboard',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Essencial para estáticos no VPS
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # CORS para aceitar o Next.js
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# --- BANCO DE DADOS (PostgreSQL) ---
# Lê a URL do banco do arquivo .env (igual ao seu projeto anterior)
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

# --- VALIDAÇÃO DE SENHA ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- INTERNACIONALIZAÇÃO ---
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# --- ARQUIVOS ESTÁTICOS ---
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- API REST & JWT ---
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

# --- CORS (Conexão Frontend) ---
# Permite que o Next.js (localhost:3000) converse com o Django
CORS_ALLOWED_ORIGINS = config(
    'CORS_ALLOWED_ORIGINS', default="http://localhost:3000", cast=Csv())

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
