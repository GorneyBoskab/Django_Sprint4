import os
from django.core.wsgi import get_wsgi_application

# Установка переменной окружения для конфигурации настроек проекта Django.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogicum.settings')

# Эта переменная `application` будет использоваться веб-сервером для передачи запросов Django.
application = get_wsgi_application()
