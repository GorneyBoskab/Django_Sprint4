from pathlib import Path

# Получение базового пути для проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ для обеспечения безопасности вашего проекта
SECRET_KEY = (
    'django-insecure-b@gq&%0mi#a00)8r*vmu=r^bwz40diwj3^z37-xl#a$qq1wqi!'
)

# Включение режима отладки (не рекомендуется включать в продакшн-режиме)
DEBUG = True

# Список разрешённых хостов для вашего приложения (используется для безопасности)
ALLOWED_HOSTS = []

# Установка установленных приложений (включает стандартные и ваши приложения)
INSTALLED_APPS = [
    'django.contrib.admin',  # Панель администратора Django
    'django.contrib.auth',  # Модели и механизмы аутентификации
    'django.contrib.contenttypes',  # Системы для работы с моделями и связями
    'django.contrib.sessions',  # Сессии пользователей
    'django.contrib.messages',  # Сообщения
    'django.contrib.staticfiles',  # Статические файлы
    'blog',  # Ваше приложение блога
    'pages',  # Ваше приложение страниц
    'django_bootstrap5',  # Подключение Bootstrap 5 для упрощения верстки
]

# Мидлваре — промежуточные слои, через которые проходят все запросы
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Защита приложения
    'django.contrib.sessions.middleware.SessionMiddleware',  # Обработка сессий
    'django.middleware.common.CommonMiddleware',  # Общие операции для всех запросов
    'django.middleware.csrf.CsrfViewMiddleware',  # Защита от CSRF-атак
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Аутентификация
    'django.contrib.messages.middleware.MessageMiddleware',  # Сообщения
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Защита от кликджекинга
]

# Настройка корневого URL-конфигуратора
ROOT_URLCONF = 'blogicum.urls'

# Путь к директории шаблонов
TEMPLATES_DIR = BASE_DIR / 'templates'

# Конфигурация шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Использование стандартного движка шаблонов
        'DIRS': [TEMPLATES_DIR],  # Папка с шаблонами
        'APP_DIRS': True,  # Разрешение использования шаблонов внутри приложений
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Для отладки
                'django.template.context_processors.request',  # Обработчик запросов
                'django.contrib.auth.context_processors.auth',  # Аутентификация
                'django.contrib.messages.context_processors.messages',  # Сообщения
            ],
        },
    },
]

# ASGI-приложение для асинхронной работы с сервером
WSGI_APPLICATION = 'blogicum.wsgi.application'

# Конфигурация базы данных (используется SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Драйвер для SQLite
        'NAME': BASE_DIR / 'db.sqlite3',  # Путь к базе данных
    }
}

# Валидация паролей (защита слабых паролей)
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Проверка на схожесть атрибутов
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Минимальная длина пароля
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Проверка на общеизвестные пароли
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Проверка на числовые пароли
    },
]

# Язык интерфейса
LANGUAGE_CODE = 'ru-RU'

# Часовой пояс
TIME_ZONE = 'UTC'

# Использование международной локализации
USE_I18N = True

# Локализация чисел, дат и времени
USE_L10N = True

# Включение временной зоны
USE_TZ = True

# Папки для статических файлов
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Путь к статическим файлам
]

# URL для доступа к статическим файлам
STATIC_URL = '/static/'

# Установка автоинкрементных полей в модели как BigAutoField
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Включение обработки ошибок CSRF
CSRF_FAILURE_VIEW = 'pages.views.csrf_failure'

# Путь после успешного входа
LOGIN_REDIRECT_URL = 'blog:index'

# URL для входа
LOGIN_URL = 'login'

# Путь для медиафайлов
MEDIA_ROOT = BASE_DIR / 'media'

# Конфигурация почтовой системы (сохранение писем в файл)
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'

# Папка для хранения отправленных писем
EMAIL_FILE_PATH = BASE_DIR / 'sent_emails'
