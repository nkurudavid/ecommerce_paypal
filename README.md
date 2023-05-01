# Ecommerce with paypal

screen shot

part 1 : store
![image](https://user-images.githubusercontent.com/122406122/235504648-9141dd2d-1062-4287-9c44-09cd4fe0e968.png)

part 2: checkout
![image](https://user-images.githubusercontent.com/122406122/235504828-677df1ac-6425-4483-adda-aea355f2934c.png)

part 3: pay via paypal
![image](https://user-images.githubusercontent.com/122406122/235505169-4b9b8384-9357-40b1-bbc6-539b7ec9c290.png)

![image](https://user-images.githubusercontent.com/122406122/235505326-8f7aa903-7cde-4f14-9e3f-82149063d341.png)

![image](https://user-images.githubusercontent.com/122406122/235505385-3efff54e-ac47-43d4-94e9-10fb6b1a5f1d.png)

![image](https://user-images.githubusercontent.com/122406122/235505481-82a7b5ad-f8bb-4e7b-8676-77c7e4a18aec.png)

# Import configuration

CORS_ORIGIN_WHITELIST = [

    'https://ba96-102-22-173-74.ngrok-free.app',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    
]


CSRF_TRUSTED_ORIGINS = [

    'https://ba96-102-22-173-74.ngrok-free.app',
]


INSTALLED_APPS = [

    #...third party
    'paypal.standard.ipn',
    'corsheaders',

    #...local app
    'shop.apps.ShopConfig',
]


## install:

- pipenv shell
- pip install django django-cors-headers django-paypal



## static configuration

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT  = os.path.join(BASE_DIR, 'static/staticfiles')


## Base url to serve media files

MEDIA_URL = '/media/'
### Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

## paypal configuration

PAYPAL_RECEIVER_EMAIL = 'sb-ygjma25843660@business.example.com'

PAYPAL_TEST = True
