#!/bin/bash

python manage.py migrate
python manage.py runserver_plus --cert-file cert.crt --reloader-interval 60 0.0.0.0:8000
