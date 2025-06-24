
web: gunicorn rental_manager.wsgi
worker: useradd -r -M -d /app -s /bin/false celeryuser && chown -R celeryuser:celeryuser /app && celery -A rental_manager worker --uid=celeryuser --gid=nobody
beat: celery -A rental_manager beat --loglevel=info
