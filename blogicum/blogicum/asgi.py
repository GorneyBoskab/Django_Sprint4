import os

# Импорт функции get_asgi_application из django, которая предоставляет ASGI-совместимую точку входа
from django.core.asgi import get_asgi_application

# Установка переменной окружения для указания настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogicum.settings')

# Получение и создание ASGI-приложения
application = get_asgi_application()
