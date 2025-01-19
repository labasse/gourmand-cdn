import os
from .settings_prod import *

# Root settings overrides

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "gmd",
        "USER"    : "gmdroot",
        "PASSWORD": os.environ.get("GMD_DB_ROOT"),
        "HOST"    : os.environ.get("GMD_DB"),
        "PORT": "5432",  
    }
}
