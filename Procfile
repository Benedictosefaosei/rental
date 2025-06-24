web: gunicorn rental_manager.wsgi
worker: celery -A rental_manager worker --loglevel=info --uid=0 --euid=0 --gid=0 --egid=0
beat: celery -A rental_manager beat --loglevel=info
