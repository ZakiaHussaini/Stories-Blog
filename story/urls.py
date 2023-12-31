
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from .views import logout_route
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path


urlpatterns = [
    # path(settings.BASE_URL + '/', views.root_route, name='root-route'),
     path('', TemplateView.as_view(template_name='index.html')),

    
    path('admin/', admin.site.urls),
    path('api/api-auth/', include('rest_framework.urls')),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),    
    path('api/dj-rest-auth/logout/', logout_route),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path(
        'api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
    ),
    path('api/', include('profiles.urls')),
    
    
    path('api/', include('posts.urls')),
    path('api/', include('comments.urls')),
    path('api/', include('likes.urls')),
    path('api/', include('followers.urls')),
    path('api/', include('savePost.urls')),
    path('api/', include('category.urls')),
    

    
]

handler404 = TemplateView.as_view(template_name='index.html')
