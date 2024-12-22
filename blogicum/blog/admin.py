from django.contrib import admin

from .models import Category, Location, Post, Comment

# Регистрируем модели в админ-панели для управления через интерфейс
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Post)
admin.site.register(Comment)
