#!/bin/bash

python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser --no-input
gunicorn -w 3 -b :8000 bookmarks.wsgi:application
