from django.shortcuts import render

# Create your views here.
def create_test_view(request, *args, **kwargs):
    return render(request, 'test1/create.html')