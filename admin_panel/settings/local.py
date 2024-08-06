from .base import *


DEBUG = True


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


SECRET_KEY = "django-insecure-_fd8=wtxq*om2-o9g48o!vqzjaj4^nej@gs*)n*_74wci-84q7"
