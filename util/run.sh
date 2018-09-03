#!/bin/bash


PYTHONUNBUFFERED=1

RUN_MIGRATE=1

set -e

if [ "$RUN_MIGRATE" != 0 ]; then
  printf "#--- Run migrations ---# \n"
  python manage.py migrate
fi

printf "#--- Run development server ---# \n"
python manage.py runserver 0.0.0.0:8000

exit 0
