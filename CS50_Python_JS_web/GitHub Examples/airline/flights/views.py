from django.shortcuts import render

from .models import Flight

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        # give index.html access to a variable called flights and gives me all the flights - since we used Flight.objects.all()
        "flights": Flight.objects.all()
    })