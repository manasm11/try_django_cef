from django.shortcuts import render, HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import UserProfile
from .serializers import UserProfileSerializer

# Create your views here.
def home_view(request):
    return HttpResponse("<h1>HELLO</h1>")

class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer