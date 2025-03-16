#!/bin/sh

# Check if the container should run as a Celery worker or Django app
if [ "$CELERY_WORKER" = "true" ]; then
    echo "Starting Celery worker..."
    # Run Celery worker in the background
    celery -A CopernicusFE worker --loglevel=info
else
    echo "Running Django tasks..."
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createcachetable

    # Check if the superuser already exists before creating it
    echo "Checking for existing superuser..."
    python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
exists = User.objects.filter(is_superuser=True).exists();
exit(0 if exists else 1)
    "

    if [ $? -eq 0 ]; then
        echo "Superuser already exists"
    else
        echo "Superuser does not exist. Creating superuser..."
        if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
            python manage.py createsuperuser \
                --noinput \
                --username "$DJANGO_SUPERUSER_USERNAME" \
                --email "$DJANGO_SUPERUSER_EMAIL"
        else
            echo "Superuser environment variables are not set. Skipping superuser creation."
        fi
    fi

    echo "Starting Django server..."
    exec "$@"
fi
