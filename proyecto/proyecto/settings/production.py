from .base import *
from decouple import config

DEBUG = False

ALLOWED_HOSTS = ['jcfp.ieshm.org', 'www.jcfp.ieshm.org']

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