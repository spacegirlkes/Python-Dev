from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        # give index.html access to a variable called flights and gives me all the flights - since we used Flight.objects.all()
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    # get me the flight whose id is equal to flight_id
    flight = Flight.objects.get(pk=flight_id)
    # render a template like flight/flight.html and pass the input to that the flight to flight.html
    return render(request, "flights/flight.html", {
        "flight": flight,
        # adding the passengers view to the page. we can do this b/c the 2nd passengers is a related name and getting all
        # the passengers that are on that flight
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))