#!/bin/bash

# Wait for MySQL to be ready
echo "Waiting for MySQL to be ready..."
while ! mysqladmin ping -h"mysql" -P"3306" -u"user" -p"password" --silent; do
    echo "MySQL is not ready yet... sleeping"
    sleep 1
done

echo "MySQL is ready! Proceeding with application startup..."

# Run migrations and start server
python manage.py migrate
exec "$@"