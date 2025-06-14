# settings/__init__.py
import os
from decouple import config

ENV = config('DJANGO_ENV', default='production')  # Cambiar esta variable en producción

if ENV == 'production':
    from .production import *
else:
    from .local import *