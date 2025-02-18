from pathlib import Path
import os
from dotenv import load_dotenv
from google.oauth2 import service_account
import json

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'epis.apps.EpisConfig',
    'entrega_epi.apps.EntregaEpiConfig',
    'autenticacao.apps.AutenticacaoConfig',
    'colaboradores.apps.ColaboradoresConfig',
    'perfil.apps.PerfilConfig',
    "debug_toolbar",
    "django_cleanup.apps.CleanupConfig",
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'autenticacao.middleware.LoginRequiredMiddleware',  
    'autenticacao.middleware.AdminAutoLoginMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]

ROOT_URLCONF = 'setup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'setup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR / "static"]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media



MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'autenticacao.CustomUser'

# Login

LOGIN_URL = '/autenticacao/login/'  

LOGIN_REDIRECT_URL = '/'  

BASE_URL = os.getenv('BASE_URL', 'http://127.0.0.1:8000')

# Carregar as credenciais do Google Cloud Storage da variável de ambiente
GOOGLE_CREDENTIALS_JSON = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON")

GS_CREDENTIALS = None  # Definir um valor padrão

if GOOGLE_CREDENTIALS_JSON:
    try:
        credentials_info = json.loads(GOOGLE_CREDENTIALS_JSON)  # Converte JSON string para dicionário
        GS_CREDENTIALS = service_account.Credentials.from_service_account_info(credentials_info)
    except json.JSONDecodeError as e:
        print(f"Erro ao carregar credenciais JSON: {e}")

# Nome do bucket no Google Cloud Storage
GS_BUCKET_NAME = "bucket-epis"

# Configuração do backend de armazenamento do Django para GCS
DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
GS_DEFAULT_ACL = "publicRead"  # Permite acesso público aos arquivos

# URL base para acessar os arquivos no Google Cloud Storage
MEDIA_URL = f"https://storage.googleapis.com/{GS_BUCKET_NAME}/"

# Segurança

SESSION_COOKIE_AGE = 1800  # Expira em 30 minutos

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SECURE_BROWSER_XSS_FILTER = True  # Protege contra XSS

SECURE_CONTENT_TYPE_NOSNIFF = True  # Evita que o navegador tente adivinhar o tipo de conteúdo

SECURE_HSTS_SECONDS = 31536000  # Ativa HSTS por 1 ano

SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Inclui subdomínios no HSTS

SECURE_HSTS_PRELOAD = True  # Permite que o site seja listado em HSTS Preload List

SECURE_SSL_REDIRECT = True  # Redireciona todo tráfego para HTTPS

SESSION_COOKIE_SECURE = True  # Cookies apenas via HTTPS

CSRF_COOKIE_SECURE = True  # Protege o cookie CSRF via HTTPS

X_FRAME_OPTIONS = "DENY"  # Bloqueia Clickjacking

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'django_debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
