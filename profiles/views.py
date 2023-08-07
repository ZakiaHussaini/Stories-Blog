from rest_framework import generics, filters
from story.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer
from django.db.models import Count


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        stories_count=Count('owner__story', distinct=True),
        followers_count = Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    
    serializer_class = ProfileSerializer
    filter_backends = [
       filters.OrderingFilter
    ]
    
    ordering_fields = [
        'stories_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]
    
class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        stories_count=Count('owner__story', distinct=True),
        followers_count = Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer


# class ProfileList(APIView):
#     def get(self, request):
#         profiles = Profile.objects.all()
#         serializer = ProfileSerializer(profiles, many=True, context={'request': request})
#         return Response(serializer.data)
    
    
# class ProfileDetail(APIView):
#     permission_classes = [IsOwnerOrReadOnly]
#     serializer_class = ProfileSerializer
    
#     def get_object(self, pk):
#         try:
#             profile = Profile.objects.get(pk=pk)
#             self.check_object_permissions(self.request, profile)
#             return profile
#         except Profile.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk):
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(profile, context={'request': request})
#         return Response(serializer.data)
    
    
#     def put(self, request, pk):
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(profile, data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    