from django.shortcuts import render
from .models import Route

def home(request):
    routes = Route.objects.all()
    return render(request, 'logistics/home.html', {'routes': routes})

def about(request):
    return render(request, 'logistics/about.html')

def air_services(request):
    return render(request, 'logistics/air_services.html')

def road_services(request):
    return render(request, 'logistics/road_services.html')

def ocean_services(request):
    return render(request, 'logistics/ocean_services.html')

def all_services(request):
    return render(request, 'logistics/all_services.html')


def price_table(request):
    return render(request, 'logistics/price_table.html')

def team(request):
    return render(request, 'logistics/team.html')

def contact(request):
    return render(request, 'logistics/contact.html')