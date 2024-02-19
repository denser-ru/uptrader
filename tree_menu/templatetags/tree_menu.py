from django import template
from django.urls import reverse
from ..models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    # Получаем корневые элементы меню по имени
    root_items = MenuItem.objects.filter(name=menu_name, parent=None)
    # Генерируем HTML-код для меню
    html = '<ul>'
    for item in root_items:
        html += draw_item(item)
    html += '</ul>'
    return html

def draw_item(item):
    # Генерируем HTML-код для одного элемента меню и его потомков
    html = '<li>'
    # Проверяем, является ли URL именованным
    if item.url.startswith('name:'):
        # Получаем реальный URL по имени
        url = reverse(item.url[5:])
    else:
        # Используем URL как есть
        url = item.url
    # Добавляем ссылку на элемент
    html += f'<a href="{url}">{item.name}</a>'
    # Проверяем, есть ли потомки у элемента
    if item.children.exists():
        # Добавляем вложенный список для потомков
        html += '<ul>'
        for child in item.children.all():
            html += draw_item(child)
        html += '</ul>'
    html += '</li>'
    return html
