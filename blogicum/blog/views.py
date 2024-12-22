from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.urls import reverse
from django.utils import timezone
from django.http import Http404
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView, DetailView)

from .models import Post, Category, User, Comment
from .forms import PostForm, CommentForm, UserForm

# Количество постов на одной странице
NUMBER_POSTS = 10

# Вспомогательная функция для получения постов с возможностью фильтрации и аннотирования
def get_posts(posts=Post.objects, filters=True, annotations=True):
    queryset = posts.select_related('author', 'location', 'category')
    if filters:
        queryset = queryset.filter(
            pub_date__lt=timezone.now(),
            is_published=True,
            category__is_published=True,
        )
    if annotations:
        queryset = queryset.annotate(comment_count=Count('comments')).order_by('-pub_date')
    return queryset

# Миксин для обработки прав на комментарии (проверка на автора)
class CommentMixin(LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    template_name = 'blog/comment.html'

    def get_object(self):
        comment_id = self.kwargs.get('comment_id')
        return get_object_or_404(Comment, id=comment_id)

    # Переадресация после успешной операции
    def get_success_url(self):
        post_id = self.kwargs.get('post_id')
        return reverse('blog:post_detail', kwargs={'pk': post_id})

    # Проверка, что комментарий принадлежит текущему пользователю
    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

# Представление для отображения профиля пользователя и его постов
def profile(request, user_name):
    user = get_object_or_404(User, username=user_name)
    posts = get_posts(filters=False).filter(author=user)
    paginator = Paginator(posts, NUMBER_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'profile': user, 'page_obj': page_obj}
    return render(request, 'blog/profile.html', context)

# Представление для списка всех опубликованных постов
class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = NUMBER_POSTS

    def get_queryset(self):
        return get_posts()

# Представление для редактирования поста (только для его автора)
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create.html'

    # Проверка, что пост может редактировать только его автор
    def dispatch(self, request, *args, **kwargs):
        self.post_id = kwargs['pk']
        if self.get_object().author != request.user:
            return redirect('blog:post_detail', pk=self.post_id)
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('blog:profile', args=[self.request.user.username])

# Представление для отображения подробностей поста
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'

    # Проверка, что отображаются только опубликованные посты или посты текущего пользователя
    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        if not post.is_published and post.author != self.request.user:
            raise Http404
        return super().get_queryset()

    # Включение формы для комментария и списка комментариев в контекст
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = self.object.comments.select_related('author')
        return context

# Представление для создания нового поста
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create.html'

    # Присваивание авторства текущему пользователю при сохранении поста
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Переадресация на профиль пользователя после успешного создания поста
    def get_success_url(self):
        return reverse('blog:profile', args=[self.request.user.username])

# Представление для удаления поста (только для его автора)
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/create.html'

    # Переадресация на профиль пользователя после удаления поста
    def get_success_url(self):
        return reverse('blog:profile', args=[self.request.user.username])

    # Проверка, что удаление может выполнить только автор поста
    def dispatch(self, request, *args, **kwargs):
        self.post_id = kwargs['pk']
        if self.get_object().author != request.user:
            return redirect('blog:post_detail', pk=self.post_id)
        return super().dispatch(request, *args, **kwargs)

# Представление для отображения постов по категории
class CategoryPostsView(ListView):
    model = Post
    template_name = 'blog/category.html'
    paginate_by = NUMBER_POSTS

    # Получение постов для конкретной категории
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category_slug'], is_published=True)
        return get_posts(filters=False).filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category=self.category,
        )

    # Включение категории в контекст
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

# Представление для редактирования профиля пользователя
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'blog/user.html'

    # Получение текущего пользователя для редактирования
    def get_object(self):
        return self.request.user

    # Переадресация на профиль пользователя после успешного редактирования
    def get_success_url(self):
        return reverse('blog:profile', args=[self.request.user.username])

# Представление для создания комментария к посту
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment.html'

    # Присваивание авторства текущему пользователю и связывание с постом
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(
            Post,
            pk=self.kwargs['pk'],
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True,
        )
        return super().form_valid(form)

    # Переадресация на страницу поста после успешного создания комментария
    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.kwargs['pk']})

class CommentDeleteView(CommentMixin, DeleteView):
    pass

class CommentUpdateView(CommentMixin, UpdateView):
    form_class = CommentForm
