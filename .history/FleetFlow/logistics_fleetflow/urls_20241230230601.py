from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
        
    path('about/', views.about, name='about'),
    path('air_services/', views.air_services, name='air_services'),
    path('road_services/', views.road_services, name='road_services'),
    path('ocean_services/', views.ocean_services, name='ocean_services'),
    path('all_services/', views.all_services, name='all_services'),
    path('price_table/', views.price_table, name='price_table'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),

]
