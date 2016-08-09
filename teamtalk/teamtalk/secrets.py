# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2s-q8ozhl!1zqp-=6j%tepb)80l*rk&&zug(&9=m$@bz4e1-13'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'teamtalk',
        'USER': 'Oakes',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
