from .models import Post, User, Comment
from django import forms

# Форма для редактирования данных пользователя
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

# Форма для создания и редактирования постов
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author', 'created_at')

# Форма для создания комментариев
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
