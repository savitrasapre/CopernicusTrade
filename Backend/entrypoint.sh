python manage.py makemigrations
python manage.py migrate
python manage.py createcachetable

# Check if the superuser already exists before creating it
echo "Checking for existing superuser..."
python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
exists = User.objects.filter(is_superuser=True).exists();
exit(exists)
"

if [ $? -eq 1 ]; then
    echo "Superuser already exists"
else
    echo "Superuser does not exist"
    if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
        echo "Creating superuser..."
        python manage.py createsuperuser \
            --noinput \
            --username $DJANGO_SUPERUSER_USERNAME \
            --email $DJANGO_SUPERUSER_EMAIL
    fi
fi

$@