from .base import *

DEBUG = False

SECRET_KEY = open(os.path.expanduser('~/.secret-key-syk')).read().strip()

STATIC_ROOT = '/opt/static/'