# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y+xrhjgke3l2on-b7gp@topgix-@#^*9_f_$w11y5jno03*xvk'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Colette1!'
    }
}