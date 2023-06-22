#!/bin/sh -x

ROOT=/home/ubuntu/asset/courseservice

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata assets/fixtures/status.json

mkdir /home/ubuntu/run
GUNICORN=/usr/local/bin/gunicorn
ROOT=/home/ubuntu/assets_management_service
PID=/home/ubuntu/run/gunicorn.pid
DJANGO_ENV="DJANGO_SETTINGS_MODULE=config.settings"
APP=config.wsgi:application

if [ -f $PID ]; then rm $PID; fi

cd $ROOT
WORKER_NUM=${WORKER_NUM:-8}
THREAD_NUM=${THREAD_NUM:-9}
MAX_REQUESTS=${MAX_REQUESTS:-1000}
MAX_REQUESTS_JITTER=${MAX_REQUESTS_JITTER:-100}
exec $GUNICORN --env $DJANGO_ENV --timeout 60 --bind 0.0.0.0:8000 --workers $WORKER_NUM --threads $THREAD_NUM --max-requests $MAX_REQUESTS --max-requests-jitter $MAX_REQUESTS_JITTER --pid=$PID $APP