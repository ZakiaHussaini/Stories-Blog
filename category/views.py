from rest_framework import generics, permissions, filters
from story.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from .models import Category
from posts.models import Post
from .serializers import  CategorySerializer
from posts.serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status



class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    


class StoryByCategoryView(generics.ListAPIView):
    serializer_class = PostSerializer
    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Post.objects.filter(category_id=category_id)