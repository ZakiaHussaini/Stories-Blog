
from django.contrib import admin
from django.urls import path, include
from .views import root_route
from django.conf import settings
from . import views


urlpatterns = [
    path(settings.BASE_URL + '/', views.root_route, name='root-route'),
    path('', root_route),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj_rest_auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', include('profiles.urls')),
    path('', include('stories.urls')),
    path('', include('comments.urls')),
    path('', include('likes.urls'))
    
]
