from rest_framework import generics, permissions, filters
from story.permissions import IsOwnerOrReadOnly
from .models import Story, Category
from .serializers import StorySerializer, CategorySerializer
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend



class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    


class StoryByCategoryView(generics.ListAPIView):
    serializer_class = StorySerializer
    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Story.objects.filter(category_id=category_id)
    

class StoryList(generics.ListCreateAPIView):
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Story.objects.annotate(
        like_count=Count('like', distinct=True),
        comment_count = Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    
    filterset_fields = [
        'owner__followed__owner__profile',
        'like__owner__profile',
        'owner__profile',
    ]
    
    search_fields = [ 
    'owner__username',
    'title',
    'category__name',
    ]

    ordering_fields = [
        'like_count',
        'comment_count',
        'like__created_at',
    ]
    
    def perform_create(self, serializer):
        category_id = self.kwargs.get('category_id')
        category = Category.objects.get(id=category_id)
        serializer.save(owner=self.request.user, category=category)
        
        
        
class StoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StorySerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Story.objects.annotate(
        like_count=Count('like', distinct=True),
        comment_count=Count('comment', distinct=True)
    ).order_by('-created_at')





# from rest_framework import status, permissions
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Story
# from .serializers import StorySerializer
# from django.http import Http404
# from story.permissions import IsOwnerOrReadOnly


# class StoryList(APIView):
#     serializer_class = StorySerializer
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly
#     ]
#     def get(self, request):
#         stories = Story.objects.all()
#         serializer = StorySerializer(
#             stories, many=True, context = {'request': request}
#         )
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = StorySerializer(
#             data=request.data, context={'request', request}
#         )
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(
#                 serializer.data, status=status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.errors, status = status.HTTP_400_BAD_REQUEST
#         )
        
# class StoryDetail(APIView):
#     permission_classes = [IsOwnerOrReadOnly]
#     serializer_class = StorySerializer
    
#     def get_object(self, pk):
#         try:
#             story = Story.objects.get(pk=pk)
#             self.check_object_permissions(self.request, story)
#             return story
#         except Story.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk):
#         story = self.get_object(pk)
#         serializer = StorySerializer(
#             story, context={'request': request}
#         )
#         return Response(serializer.data)
    
    
#     def put(self, request, pk):
#         story = self.get_object(pk)
#         serializer = StorySerializer(
#             story, data=request.data, context = {'request':request}
#         )
        
#         if serializer.is_valid():
#             serializer.save() 
#             return Response(serializer.data)
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST 
#         )
            
#     def delete(self, request, pk):
#         story = self.get_object(pk)
#         story.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
#         )