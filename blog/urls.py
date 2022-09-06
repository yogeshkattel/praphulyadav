from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    add_comment,
    FilterPostListView,
    News,
    CreateNewsView,
)


urlpatterns = [
    path('post/', PostListView.as_view(), name='news'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('news/create', CreateNewsView.as_view(), name='news_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),
    path('subscribe/<int:pk>', views.subscribe, name='subscribe_user'),
    path('filter/<str:category>', FilterPostListView.as_view(), name='filter_posts'),
    path('', News.as_view(), name='index'),
    
]
