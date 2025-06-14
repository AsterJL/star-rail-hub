from .base import *
from decouple import config

DEBUG = True

ALLOWED_HOSTS = []
# '127.0.0.1', config('SERVER_DOMAIN', default='localhost')

# RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
# if RENDER_EXTERNAL_HOSTNAME:
#     ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

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
# cast=int

# This production code might break development mode, so we check whether we're in DEBUG mode
if not DEBUG:
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'