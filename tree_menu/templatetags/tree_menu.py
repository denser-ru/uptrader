from django import template
from tree_menu.models import MenuItem

register = template.Library()

@register.inclusion_tag('tree_menu/tree_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    path = request.path
    all_menu_items = MenuItem.objects.prefetch_related('children').filter(parent=None)
    
    # Определение активного пункта меню
    def mark_active(menu_items):
        for item in menu_items:
            item.is_active = (path == item.url)
            if item.children.all():
                item.children = mark_active(item.children.all())
        return menu_items

    menu_items = mark_active(all_menu_items)
    
    return {'menu_items': menu_items}
