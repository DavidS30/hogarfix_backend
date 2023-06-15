from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from .models import Profile

# Serializers define the API representation.
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'