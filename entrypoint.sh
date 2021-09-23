#!/bin/sh

python backend/manage.py collectstatic --noinput
python backend/manage.py migrate 
python backend/manage.py createsuperuser --no-input
#add this to ur variable envieronment('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')" | python backend/manage.py shell

exec "$@"