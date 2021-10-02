from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request): #index returns http response "hello world"
    return HttpResponse("Hello!")

def index(request): #index returns http response "hello world"
    return render(request, "hello/index.html")

def Elise(request):
    return HttpResponse("Hello, Elise!")

def Kelly(request):
    return HttpResponse("Hello, Kelly!")

def greet(request, name): # added the name parameter
    return HttpResponse(f"Hello, {name.capitalize()}!")