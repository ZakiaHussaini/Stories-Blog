from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('categories/<int:category_id>/posts/', views.StoryByCategoryView.as_view()),
    path('categories/', views.CategoryListView.as_view()),
    path('posts/<int:pk>/save/', views.PostDetail.as_view(), name='post-save'),
]