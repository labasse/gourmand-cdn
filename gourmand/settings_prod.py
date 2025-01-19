import os
from .settings import *

# Settings overrides

SECRET_KEY = os.getenv('GMD_SEC')

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ['https://*.azurecontainerapps.io']

DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = True

ALLOWED_HOSTS = ['.azurecontainerapps.io']

# ...

ROOT_URLCONF = "gourmand.urls_prod"

# ...

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "gmd",
        "USER"    : "gmdapp",
        "PASSWORD": os.environ.get("GMD_DB_APP"),
        "HOST"    : os.environ.get("GMD_DB"),
        "PORT": "5432",  
    }
}

# ...

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.azure_storage.AzureStorage",
        "OPTIONS": {
            "account_name"   : os.environ.get("GMD_ST_ACC"),
            "account_key"    : os.environ.get("GMD_ST_KEY"),
            "azure_container": os.environ.get("GMD_ST_MEDIA"),
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.azure_storage.AzureStorage",
        "OPTIONS": {
            "account_name"   : os.environ.get("GMD_ST_ACC"),
            "account_key"    : os.environ.get("GMD_ST_KEY"),
            "azure_container": os.environ.get("GMD_ST_STATIC"),
        },
    },
}
