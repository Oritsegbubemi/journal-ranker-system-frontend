from .settings import *

print('Production Settings')

DEBUG = True

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