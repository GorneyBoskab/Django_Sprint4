from django.apps import AppConfig

# Конфигурация приложения 'blog'
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    verbose_name = 'Блог'
