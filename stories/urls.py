from django.urls import path
from stories import views


urlpatterns = [
    path('stories/', views.StoryList.as_view()),
    path('stories/<int:pk>/', views.StoryDetail.as_view()),
    path('categories/<int:category_id>/stories/', views.StoryByCategoryView.as_view()),
    path('categories/', views.CategoryListView.as_view()),
    
    ]
