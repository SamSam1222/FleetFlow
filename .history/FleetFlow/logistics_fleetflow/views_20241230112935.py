from django.shortcuts import render
from .models import Route

def home(request):
    routes = Route.objects.all()
    return render(request, 'logistics/home.html', {'routes': routes})
