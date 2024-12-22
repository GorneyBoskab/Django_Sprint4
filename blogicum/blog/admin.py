from django.contrib import admin

# Импорт моделей для регистрации в админ-панели
from .models import Category, Location, Post, Comment

# Регистрируем модели в админ-панели для управления через интерфейс
admin.site.register(Category)  # Категории публикаций
admin.site.register(Location)  # Местоположения
admin.site.register(Post)      # Публикации
admin.site.register(Comment)   # Комментарии
