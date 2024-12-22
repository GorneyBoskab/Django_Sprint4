from .models import Post, User, Comment
from django import forms

# Форма для редактирования данных пользователя
class UserForm(forms.ModelForm):
    class Meta:
        model = User  # Модель пользователя
        fields = ('first_name', 'last_name', 'email')  # Поля для ввода: имя, фамилия, email

# Форма для создания и редактирования постов
class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # Модель публикации
        exclude = ('author', 'created_at')  # Исключаем поля: автор и дата создания, они будут заданы автоматически

# Форма для создания комментариев
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)  # Единственное поле для ввода текста комментария
