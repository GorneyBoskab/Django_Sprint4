from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.conf import settings
from django.conf.urls.static import static

# Указание обработчиков ошибок 404 и 500
handler404 = 'pages.views.page_not_found'  # Обработчик для ошибок 404
handler500 = 'pages.views.server_error'  # Обработчик для ошибок 500

urlpatterns = [
    # Маршрут для административной панели
    path('admin/', admin.site.urls),
    
    # Включение маршрутов приложения blog
    path('', include('blog.urls')),  
    
    # Включение маршрутов приложения pages
    path('pages/', include('pages.urls')),  
    
    # Включение встроенных маршрутов для аутентификации Django
    path('auth/', include('django.contrib.auth.urls')),  
    
    # Пользовательская регистрация с использованием встроенной формы UserCreationForm
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('blog:index'),
        ),
        name='registration',  # Имя маршрута
    ),
] 

# Добавление URL-обработки для медиафайлов в режиме разработки
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
