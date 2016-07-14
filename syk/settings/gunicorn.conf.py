bind = '127.0.0.1:8000'
workers = 3
user = "nobody"
raw_env = {
    'DJANGO_SETTINGS_MODULE': 'syk.settings.prod'
}
