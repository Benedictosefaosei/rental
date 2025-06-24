web: gunicorn rental_manager.wsgi
worker: celery -A rental_manager worker --loglevel=info --uid=nobody --gid=nogroup
beat: celery -A rental_manager beat --loglevel=info
