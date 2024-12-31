from django.shortcuts import render
from .models import Route

def home(request):
    routes = Route.objects.all()
    return render(request, 'logistics/home.html', {'routes': routes})

def about(request):
    return render(request, 'logistics/about.html')

def services(request):
    return render(request, 'logistics/services.html')
