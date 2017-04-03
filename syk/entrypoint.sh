export DJANGO_SETTINGS_MODULE=syk.settings.dev

python ./manage.py collectstatic --noinput

python ./manage.py migrate

echo Starting Gunicorn.
exec gunicorn syk.wsgi:application \
    --name syk \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=info