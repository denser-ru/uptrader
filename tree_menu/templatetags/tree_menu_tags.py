from django import template
from tree_menu.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_block_name):
    request = context['request']
    path = request.path
    menu_items = MenuItem.objects.prefetch_related('children').filter(parent=None, menu_block__name=menu_block_name)
    
    def mark_active(items):
        for item in items:
            item.is_active = (path == item.url)
            if item.children.all():
                item.children_list = mark_active(list(item.children.all()))
            else:
                item.children_list = []
        return items

    activ_menu_items = mark_active(menu_items)

    # Получаем шаблон и рендерим его с контекстом
    t = template.loader.get_template('tree_menu/base_menu.html')

    return t.render({'menu_items': activ_menu_items})
