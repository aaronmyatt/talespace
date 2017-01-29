from .common_settings import *

AUTHENTICATION_METHOD = 'username'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'talespace',
        'USER': 'root',
        'HOST': 'localhost',
    }
}