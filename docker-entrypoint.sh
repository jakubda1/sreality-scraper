#!/bin/sh
python3 manage.py makemigrations scraper_core
python3 manage.py migrate
python3 manage.py scrape

echo "Collecting static"
python3 manage.py collectstatic --no-input &&
echo "Starting server"
python3 manage.py runserver 0.0.0.0:8080 --settings djangoProject1.settings &&
echo "Creating unicorns"
gunicorn djangoProject1.wsgi:application --bind 0.0.0.0:8080 --workers 3 &&