from .base import *
import dj_database_url

os.environ['SECRET_KEY'] = '4u49ke%41f1o=!eb$&xveawsxysx3n=qhh9168va-#3(^yh#bz' #TODO: Turn off on realease
SECRET_KEY = os.environ['SECRET_KEY'] 
DEBUG = True #TODO: Turn off on realease

ALLOWED_HOSTS += ["masiin.org", "*.masiin.org", "MSSN20.herokuapp.com", "www.masiin.org"]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'MSSNdb',
       'USER': 'MSSN',
       'PASSWORD': 'Pass@1234',
       'HOST': 'localhost',
       'PORT': '',
   }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
#     }
# }
DATABASES_URL = os.environ['DATABASE_URL'] 
DATABASES['default'] = dj_database_url.parse(DATABASES_URL, conn_max_age=600)


STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/MSSNstatic/'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
MEDIA_URL = '/MSSNmedia/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

HOST = "https://MSSN.org"

# Google cloud for images
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_PROJECT_ID ='dabolinux'
GS_BUCKET_NAME = 'dabolinux_tech_clients'
GS_FILE_OVERWRITE = True
GS_LOCATION = 'clients/masiin'
from google.oauth2 import service_account
# a.Credentials.from_service_account_info TODO: Fix here
GS_AUTH_FILE = os.path.join(PROJECT_ROOT, "dabolinux-clients-demo-32103b022bf6.json")
# GS_CREDENTIALS = {
#   "type": "service_account",
#   "project_id": "dabolinux",
#   "private_key_id": os.environ['private_key_id'],
#   "private_key": os.environ['private_key'],
#   "client_email": os.environ['client_email'],
#   "client_id": os.environ['client_id'],
#   "auth_uri": os.environ['auth_uri'],
#   "token_uri": os.environ['token_uri'],
#   "client_x509_cert_url": os.environ['client_x509_cert_url']
#     }
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    GS_AUTH_FILE)
# GS_CREDENTIALS = service_account.Credentials.from_service_account_info(
#     GS_CREDENTIALS)