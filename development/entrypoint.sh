#!/usr/bin/env bash

echo "Waiting 15 seconds to be sure squadapp database is setup"

sleep 15

/usr/local/bin/python3 manage.py migrate

/usr/local/bin/python3 manage.py base_user

/usr/local/bin/gunicorn --reload --workers=1 --access-logfile=- --error-logfile=- -b 0.0.0.0:9090 squadapp.wsgi
