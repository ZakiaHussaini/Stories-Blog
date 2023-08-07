from rest_framework import generics, permissions
from story.permissions import IsOwnerOrReadOnly
from .models import Story
from .serializers import StorySerializer



class StoryList(generics.ListCreateAPIView):
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Story.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
        
        
class StoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StorySerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Story.objects.all()





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