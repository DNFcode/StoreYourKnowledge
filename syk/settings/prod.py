from .base import *

DEBUG = False

SECRET_KEY = open(os.path.abspath('/root/.secret-key-syk')).read().strip()

STATIC_ROOT = '/opt/static/'