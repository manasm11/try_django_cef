from django.shortcuts import render
from .forms import NameForm

# Create your views here.
def index_view(request):
    return render(request, "test3/index.html")

def create_view(request):
    context = {
        'form':NameForm(request.POST or None)
    }
    context['form'].is_valid() and context['form'].save()
    return render(request, "test3/create.html", context)