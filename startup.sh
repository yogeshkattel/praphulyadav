#!/bin/sh
set -e
systemctl start cron
systemctl enable cron
python3 manage.py runserver 0.0.0.0:8000

exec "$@"

