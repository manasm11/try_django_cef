from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class TestView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({'message':'TU AUTHENTICATED HAI !!!! BTW Happy New Year...🎉🎉🎉'}, status=200)