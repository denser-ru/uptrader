#!/bin/bash
# Скрипт для запуска Django-приложения

# Установка переменной окружения
export DJANGO_SETTINGS_MODULE='UpTrader.settings'

# Запуск сервера разработки
python manage.py runserver --insecure
