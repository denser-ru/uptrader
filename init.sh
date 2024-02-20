#!/bin/bash
# Установка переменной окружения
export DJANGO_SETTINGS_MODULE='UpTrader.settings'

# Остановить скрипт при ошибках
#set -e

# Устанавливаем зависимости
#pip install -r requirements.txt

# Выполняем миграции
python manage.py makemigrations
python manage.py migrate

# Создание суперпользователя с заданными логином и паролем (lg: admin, pw: admin)
export DJANGO_SUPERUSER_USERNAME='admin'
export DJANGO_SUPERUSER_PASSWORD='admin'
export DJANGO_SUPERUSER_EMAIL='admin@example.com'
python manage.py createsuperuser --noinput

# Собираем статические файлы
python manage.py collectstatic --noinput

# Загружаем примеры меню в базу данных
python manage.py loaddata sample_menus.json

# Загружаем примеры страниц
python manage.py loaddata sample_flatpages.json

# Запускаем сервер разработки
python manage.py runserver --insecure


