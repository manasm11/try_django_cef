from django.shortcuts import render, HttpResponse

# Create your views here.
def home_view(request):
    return HttpResponse("<h1>HELLO</h1>")