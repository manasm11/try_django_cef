from django.shortcuts import render, HttpResponse
from rest_framework import viewsets, authentication, filters
# from .models import UserProfile
# from .serializers import UserProfileSerializer
from . import (
    permissions,
    models,
    serializers,
    )

# Create your views here.
def home_view(request):
    return HttpResponse("<h1>HELLO</h1>")

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.UserUpdateTheirProfile]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['email', 'name']
    ordering_fields = ['email', 'name']