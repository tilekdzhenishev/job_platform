from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated

class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'user_id'
