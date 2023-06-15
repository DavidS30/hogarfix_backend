from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Profile
from .serializers import ProfileSerializer, UserSerializer
from rest_framework import viewsets
# Create your views here.

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer