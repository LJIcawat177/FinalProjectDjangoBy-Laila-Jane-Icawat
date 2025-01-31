from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    CategoryListView, CategoryCreateView,
    RecipeListView, RecipeDetailView, RecipeCreateView,
    CommentCreateView, PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView
)

urlpatterns = [
    path('', RecipeListView.as_view(), name='home'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/new/', CategoryCreateView.as_view(), name='new_category'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='view_recipe'),
    path('recipe/new/', RecipeCreateView.as_view(), name='new_recipe'),
    path('comment/new/', CommentCreateView.as_view(), name='new_comment'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', PostCreateView.as_view(), name='create_post'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='update_post'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
