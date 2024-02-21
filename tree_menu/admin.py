from django.contrib import admin
from .models import MenuItem, MenuBlock

@admin.register(MenuItem)

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'parent', 'menu_block')

    def get_url(self, obj):
        # Вернуть URL, если он определён
        return obj.url if hasattr(obj, 'url') else 'URL не определён'

    def get_parent(self, obj):
        # Вернуть родительский элемент, если он определён
        return obj.parent if hasattr(obj, 'parent') else 'Родитель не определён'

    def get_name(self, obj):
        # Вернуть значение поля 'name', если оно существует
        return obj.name if hasattr(obj, 'name') else 'Техническое имя не определено'

    def get_menu_block(self, obj):
        # Вернуть родительский элемент, если он определён
        return obj.menu_block if hasattr(obj, 'menu_block') else 'Блок меню не определён'

    get_name.short_description = 'Техническое имя'  # Описание для отображения в административной панели
    get_url.short_description = 'URL'
    get_parent.short_description = 'Родитель'
    get_menu_block.short_description = 'Блок меню'

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1  # Количество форм для новых элементов

@admin.register(MenuBlock)
class MenuBlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    inlines = [MenuItemInline]

