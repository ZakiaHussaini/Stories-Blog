from django.urls import path
from category import views

urlpatterns = [
    path('categories/<int:category_id>/posts/', views.StoryByCategoryView.as_view()),
    path('categories/', views.CategoryListView.as_view()),
]