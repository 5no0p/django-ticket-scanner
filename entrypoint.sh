#!/bin/sh

python manage.py collectstatic --noinput
python manage.py migrate 
python manage.py createsuperuser --no-input
#add this to ur variable envieronment('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')" | python manage.py shell

exec "$@"