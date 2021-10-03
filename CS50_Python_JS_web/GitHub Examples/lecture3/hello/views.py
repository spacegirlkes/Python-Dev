from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request): #index returns http response "hello world"
    return HttpResponse("Hello!")

def index(request): #how to create an entire page
    return render(request, "hello/index.html") #adding in a template index.html from hello folder inside templates

def Elise(request):
    return HttpResponse("Hello, Elise!")

def Kelly(request):
    return HttpResponse("Hello, Kelly!")

def greetOne(request, name): # added the name parameter
    return HttpResponse(f"Hello, {name.capitalize()}!")
    
def greet(request, name): # render template greet.html and proving template with additional context/information. In this case a dictionary
    return render(request, "hello/greet.html", {
        # creating a dictionary w/key of name (effectively giving this template 
        # access to avariable called name) and its value is whatever name.capitalize is equal to
        # .capitalize is part of the argument for name -> greet(request, name)
        "name": name.capitalize() 
    })