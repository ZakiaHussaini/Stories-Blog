# views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import SavedPost
from .serializers import SavedPostSerializer

class SavedPostCheckView(generics.RetrieveAPIView):
    serializer_class = SavedPostSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        post_id = self.kwargs['post_id']
        try:
            return SavedPost.objects.get(user=user, post_id=post_id)
        except SavedPost.DoesNotExist:
            return None

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response({'saved': False})

class SavedPostSaveView(generics.CreateAPIView):
    serializer_class = SavedPostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SavedPostUnsaveView(generics.DestroyAPIView):
    serializer_class = SavedPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        post_id = self.kwargs['post_id']
        return SavedPost.objects.filter(user=user, post_id=post_id)

