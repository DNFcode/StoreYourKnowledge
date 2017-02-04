echo Starting Gunicorn.
exec gunicorn syk.wsgi:application \
    --name syk \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=info