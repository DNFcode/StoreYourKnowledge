from .base import *
import os

DEBUG = False

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

STATIC_ROOT = '/opt/static/'