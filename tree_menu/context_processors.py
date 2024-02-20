# context_processors.py

from .models import MenuItem

def menu_processor(request):
    path = request.path
    menu_items = MenuItem.objects.prefetch_related('children').filter(parent=None)
    marked_menu_items = mark_active(menu_items, path)
    return {'menu_items': marked_menu_items}

def mark_active(menu_items, path):
    for item in menu_items:
        item.is_active = (path == item.url)
        if item.children.all():
            item.children_list = mark_active(list(item.children.all()), path)
        else:
            item.children_list = []
    return menu_items
