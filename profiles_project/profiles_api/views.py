from django.shortcuts import render, HttpResponse
from rest_framework import viewsets, authentication, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.settings import api_settings
from django.conf import settings

# from .models import User
# from .serializers import UserSerializer
from . import (
    permissions,
    models,
    serializers,
    )

# Create your views here.
def home_view(request):
    return HttpResponse("<h1>HELLO</h1>")

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.UserUpdateTheirProfile]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['email', 'name']
    ordering_fields = ['email', 'name']
    filterset_fields = ['id', 'name', 'email']

# To access urls after login, add
# Authorization : Token <TOKEN> along with request.
class UserLoginView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class FeedViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FeedSerializer
    queryset = models.Feed.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.UserUpdateTheirFeed, IsAuthenticatedOrReadOnly]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['text']
    ordering_fields = ['user', 'text', 'created_on']
    filterset_fields = ['user', 'text', 'created_on']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
