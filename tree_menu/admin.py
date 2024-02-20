from django.contrib import admin
from .models import MenuItem

@admin.register(MenuItem)

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_url', 'get_parent')

    def get_url(self, obj):
        # Вернуть URL, если он определён
        return obj.url if hasattr(obj, 'url') else 'URL не определён'

    def get_parent(self, obj):
        # Вернуть родительский элемент, если он определён
        return obj.parent if hasattr(obj, 'parent') else 'Родитель не определён'

    def get_name(self, obj):
        # Вернуть значение поля 'name', если оно существует
        return obj.name if hasattr(obj, 'name') else 'Имя не определено'

    get_name.short_description = 'Name'  # Описание для отображения в административной панели
    get_url.short_description = 'URL'
    get_parent.short_description = 'Родитель'
