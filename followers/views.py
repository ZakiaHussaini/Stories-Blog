from rest_framework import generics, permissions
from story.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import followerSerializer



class FollowerList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = followerSerializer
    
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class FollowerDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = followerSerializer
    