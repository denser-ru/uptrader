#!/bin/bash
# Откат миграций для приложения tree_menu
python manage.py migrate tree_menu zero

# Удаление всех файлов миграций в приложении tree_menu
find . -path "*/tree_menu/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/tree_menu/migrations/*.pyc"  -delete

# Удаление папок __pycache__
find . -type d -name "__pycache__" -exec rm -r {} +

# Очистка таблиц базы данных (опционально)
# ВНИМАНИЕ: Это удалит все данные из таблиц!
#python manage.py flush

# Удаление суперпользователя (опционально)
#python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(is_superuser=True).delete()"

# Очистка базы данных
# ВНИМАНИЕ: Это удалит все данные из базы данных!
echo "Вы уверены, что хотите удалить все данные из базы данных? (yes/no)"
read confirmation
if [ "$confirmation" == "yes" ]; then
    # Замените 'db.sqlite3' на путь к вашей базе данных, если он отличается
    rm db.sqlite3
    echo "База данных удалена."
else
    echo "Действие отменено."
fi

# Удаление всех собранных статических файлов
# ВНИМАНИЕ: Это удалит все собранные статические файлы!
echo "Вы уверены, что хотите удалить все собранные статические файлы? (yes/no)"
read confirmation
if [ "$confirmation" == "yes" ]; then
    # Замените 'static' на путь к вашей папке со статическими файлами, если он отличается
    rm -rf static/
    echo "Статические файлы удалены."
else
    echo "Действие отменено."
fi

# Удаление всех файлов журналов
# ВНИМАНИЕ: Это удалит все файлы журналов!
echo "Вы уверены, что хотите удалить все файлы журналов? (yes/no)"
read confirmation
if [ "$confirmation" == "yes" ]; then
    # Замените 'logs' на путь к вашей папке с файлами журналов, если он отличается
    rm -rf logs/
    echo "Файлы журналов удалены."
else
    echo "Действие отменено."
fi

echo "Деинсталляция завершена."
