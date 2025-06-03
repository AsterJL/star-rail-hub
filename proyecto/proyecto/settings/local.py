from .base import *
from decouple import config

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',  # Base de datos local
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',                 # Motor para mysql-connector-python
        'NAME': config('DB_NAME'),                          # Nombre de la base de datos
        'USER': config('DB_USER'),                          # Usuario de la base de datos
        'PASSWORD': config('DB_PASSWORD'),                  # Contraseña del usuario
        'HOST': config('DB_HOST', default='localhost'),     # Dirección del servidor
        'PORT': config('DB_PORT', default='3306'),          # Puerto de la base de datos
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}