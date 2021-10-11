from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    # one model for each of the main tables we care about storing information about
    # origin = models.CharField(max_length=64)
    # cascade deletes and airpot from airport table and the flights associated
    # related_name is a way to access a relationship in reverse order
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures") 
    # destination = models.CharField(max_length=64)
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

# adding a passenger list
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    # passengers will have flights associated with them which are a models.manytomanyfield with flight
    # so every passenger could be associated with many flights
    # blank=true allows passengers to have no flights
    # related_name means if I have a passenger I can use the flights (variable at begining) attribute to access all of their flights
    # If I have a flight I can use this passengers related_name to access all of the passengers who are on that flight
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    #string representation of a passenger
    def __str__(self):
        return f"{self.first} {self.last}"