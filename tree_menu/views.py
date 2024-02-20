from django.shortcuts import render
from .models import MenuItem

def custom_404(request, exception):
    return render(request, '404.html', {}, status=404)

def get_menu_items(menu_name):
    # Получаем все пункты меню и их детей с одним запросом к БД
    menu_items = MenuItem.objects.prefetch_related('children').filter(parent=None)
    return menu_items

def mark_active(menu_items, path):
    # Рекурсивная функция для отметки активных пунктов меню
    for item in menu_items:
        # Проверяем, совпадает ли URL пункта меню с текущим путем
        item.is_active = (path == item.url)
        # Если у пункта меню есть дети, рекурсивно отмечаем их
        if item.children.all():
            item.children_list = mark_active(list(item.children.all()), path)
        else:
            item.children_list = []
    return menu_items

def home(request):
    # Получаем текущий путь запроса
    path = request.path
    # Получаем все пункты меню
    menu_items = get_menu_items('main_menu')
    # Отмечаем активные пункты меню
    marked_menu_items = mark_active(menu_items, path)
    # Передаем пункты меню в контекст шаблона
    context = {'menu_items': marked_menu_items}
    return render(request, 'home.html', context)

