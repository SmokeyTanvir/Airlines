from django.urls import path 
from . import views

app_name = 'flights'

urlpatterns = [
    path('', views.index, name='home'),
    path('flights/', views.flights, name='flights'),
    path('flights/<int:id>', views.flight, name='flight_details'),
    path('passengers/<int:id>', views.passenger, name='passenger_details'),
]

