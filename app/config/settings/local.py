from django.conf import settings

from .base import *

import_secrets()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "localhost",
        "NAME": settings.DATABASE_NAME,
        "USER": settings.DATABASE_USER,
        "PASSWORD": settings.DATABASE_PASSWORD,
        "PORT": 5432,
    }
}
