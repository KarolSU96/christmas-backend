from django.shortcuts import render
from .models import Profile
from .ProfileSerializer import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
# Create your views here.
