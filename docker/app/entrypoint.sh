#!/bin/sh

set -e

whoami

python manage.py collectstatic --noinput

uwsgi --socket :8000 --master --enable-threads --module qblock.wsgi


ENTRYPOINT ["bash","entrypoint.prod.sh"]
