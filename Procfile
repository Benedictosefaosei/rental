web: gunicorn rental_manager.wsgi
worker: celery -A rental_manager worker --loglevel=info --uid=1 --gid=1
beat: celery -A rental_manager beat --loglevel=info
