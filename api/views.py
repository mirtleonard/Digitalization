from api.serializers import UserSerializer
from django.shortcuts import render
from rest_framework import viewsets
from user.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
