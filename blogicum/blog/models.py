from django.db import models
from django.contrib.auth import get_user_model

# Получаем модель пользователя
User = get_user_model()

# Базовая модель с общими полями для других моделей
class BaseModel(models.Model):
    # Поле для указания опубликованности записи
    is_published = models.BooleanField(
        'Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.',
    )
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    # Метод для строки объекта (обычно используется в админ-панели)
    def __str__(self):
        return self.title

    class Meta:
        abstract = True  # Указывает, что данная модель является абстрактной

# Модель публикации
class Post(BaseModel):
    title = models.CharField('Заголовок', max_length=256)
    text = models.TextField('Текст')
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        help_text='Если установить дату и время в будущем — можно делать отложенные публикации.'
    )
    image = models.ImageField('Фото', upload_to='post_images', blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
        related_name='posts',
    )  # Автор публикации (связь с моделью пользователя)
    location = models.ForeignKey(
        'Location',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Местоположение',
        related_name='posts',
    )  # Местоположение (необязательно)
    category = models.ForeignKey(
        'Category',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        related_name='posts',
    )  # Категория публикации

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('created_at',)

# Модель категории
class Category(BaseModel):
    title = models.CharField('Заголовок', max_length=256)  # Заголовок категории
    description = models.TextField('Описание')  # Описание категории
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.'
    )  # Уникальный идентификатор для URL

    class Meta:
        verbose_name = 'категория'  # Человеко-читаемое имя модели
        verbose_name_plural = 'Категории'  # Во множественном числе

# Модель местоположения
class Location(BaseModel):
    name = models.CharField('Название места', max_length=256)  # Название места

    def __str__(self):
        return self.name  # Отображаем название места

    class Meta:
        verbose_name = 'местоположение'  # Человеко-читаемое имя модели
        verbose_name_plural = 'Местоположения'  # Во множественном числе

# Модель комментария
class Comment(models.Model):
    text = models.TextField('Текст комментария')  # Текст комментария
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )  # Связь с публикацией
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
