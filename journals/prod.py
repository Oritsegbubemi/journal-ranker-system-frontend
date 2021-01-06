from .settings import *

import dj_database_url

print('Production Settings')

DEBUG = False

ALLOWED_HOSTS = ['journal-ranker.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'de7t719dbptl8i',
        'HOST': 'ec2-3-208-50-226.compute-1.amazonaws.com',
        'USER': 'mnsfaqmushcxvt',
        'PASSWORD': '93870378dadf14ed34cc332a88b6090af341409e4da6bd8d748ca32ba9d5d932',
        'PORT': '5432',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
