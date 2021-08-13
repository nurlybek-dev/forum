from django.contrib import admin
from django.db import models


"""
Сообщение:
    Пользователь
    Тело сообщений
    Дата

Тема:
    Название темы
    Создатель
    Дата

Раздел:
    Родительский раздел
    Название
"""


class Section(models.Model):
    name = models.CharField(max_length=120)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self) -> str:
        return self.name

    @admin.display(boolean=True, ordering='parent')
    def is_top_section(self) -> bool:
        return not self.parent
