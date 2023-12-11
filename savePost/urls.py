from django.urls import path
from .views import SavedPostCheckView, SavedPostSaveView, SavedPostUnsaveView, SavedPostsListView

urlpatterns = [
    path('saved-posts/', SavedPostsListView.as_view()),
    path('saved-posts/check/<int:user_id>/<int:post_id>/', SavedPostCheckView.as_view(), name='saved-post-check'),
    path('saved-posts/save/<int:user_id>/<int:post_id>/', SavedPostSaveView.as_view(), name='saved-post-save'),
    path('saved-posts/unsave/<int:user_id>/<int:post_id>/', SavedPostUnsaveView.as_view(), name='saved-post-unsave'),
]






