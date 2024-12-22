from django.urls import path

from . import views

# Название приложения для использования в шаблонах
app_name = 'blog'

urlpatterns = [
    # Главная страница: список публикаций
    path('', views.PostListView.as_view(), name='index'),
    
    # Страница публикации по её ID
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    
    # Страница с публикациями из определённой категории
    path('category/<slug:category_slug>/', views.CategoryPostsView.as_view(), name='category_posts'),
    
    # Страница для создания новой публикации
    path('posts/create/', views.PostCreateView.as_view(), name='create_post'),
    
    # Профиль пользователя по его имени
    path('profile/<slug:user_name>/', views.profile, name='profile'),
    
    # Страница для редактирования профиля пользователя
    path('edit_profile/', views.UserUpdateView.as_view(), name='edit_profile'),
    
    # Страница для редактирования публикации по её ID
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
    
    # Страница для удаления публикации по её ID
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete_post'),
    
    # Страница для добавления комментария к публикации
    path('posts/<int:pk>/comment/', views.CommentCreateView.as_view(), name='add_comment'),
    
    # Страница для редактирования комментария по его ID и публикации
    path('posts/<int:post_id>/edit_comment/<int:comment_id>/', views.CommentUpdateView.as_view(), name='edit_comment'),
    
    # Страница для удаления комментария по его ID и публикации
    path('posts/<int:post_id>/delete_comment/<int:comment_id>', views.CommentDeleteView.as_view(), name='delete_comment'),
]
