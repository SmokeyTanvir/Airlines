from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    return render(request, 'Flights/index.html', {
        't1': models.Thumbnail.objects.first(),
        't2': models.Thumbnail.objects.last()
    })

def flights(request):
    flights = models.Flight.objects.all()

    return render(request, 'Flights/flights.html', {
        'flights': flights
    })

def flight(request, id):
    if not request.user.is_authenticated:
        pass

    flight = models.Flight.objects.get(pk=id)

    return render(request, 'Flights/flight_details.html', {
        'flight': flight
    })

def passenger(request, id):
    passenger = models.Passenger.objects.get(pk=id)

    return render(request, 'Flights/passenger_details.html', {
        'passenger': passenger
    })