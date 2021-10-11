from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # specify flight id as an int, then load flight view whose name will be flight
   path("<int:flight_id>", views.flight, name="flight"),
   path("<int:flight_id>/book", views.book, name="book")
]