from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'generator/home.html', {'password':'asddsfvergdgf'})

def boxing(request):
    return HttpResponse('<h1>I love boxing!</h1>')