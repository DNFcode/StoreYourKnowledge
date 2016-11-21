from .base import *

SECRET_KEY = '4btc2x))6dk-vfzli6=0nxk3h2sugn$4r420mrfcl2uv$j(l75'

DEBUG = True

if DEBUG:
    INTERNAL_IPS = ('10.0.2.2',)

    INSTALLED_APPS += (
        # 'debug_toolbar',
    )
