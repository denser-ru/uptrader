from django.db import models
from django.urls import reverse


class MenuBlock(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text='Уникальное техническое имя блока меню')
    title = models.CharField(max_length=100, help_text='Отображаемое название блока меню')

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    menu_block = models.ForeignKey(MenuBlock, on_delete=models.CASCADE, related_name='menu_items')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.url.startswith('name:'):
            return reverse(self.url[5:])
        return self.url

