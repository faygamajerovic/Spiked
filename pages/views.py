from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render
from components.models import Spirit

# Create your views here.

def home(request):
    return render(request, 'home.html')


def spirits(request):
    query = Spirit.objects.all()
    context = {
        "spirits": query
    }
    return render(request, 'spirits.html', context=context)



def glasses(request):
    return render(request)
