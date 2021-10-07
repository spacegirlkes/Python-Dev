from django import forms
from django.http import HttpResponseRedirect
from django.forms.fields import CharField
from django.http.response import HttpResponse, HttpResponseRedirect # django can generate forms instead of us making one in HTML
from django.shortcuts import render
from django.urls import reverse

# tasks = [] # empty list to populate for testing pre-sessions adding. This is a global variable
class NewTaskForm(forms.Form): # django creates a form
    task = CharField(label="New Task") # enter in characters
    #priority = forms.IntegerField(label="Priority", min_value=1, max_value=10) # can add a prioroty/integer field with constraints like min/max. Also provides client side validation. No server interaction

# Create your views here.
def index(request):
    # storing tasks inside of the user's session
    if "tasks" not in request.session:
        request.session["tasks"] = [] # create empty list if there are no "tasks"

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"] # django gives us access to tasks on the right
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST) # rewquest.post contains all of the data the user submitted
        if form.is_valid(): # manually check server side validation
            task = form.cleaned_data["task"] # gives us access to all data user submitted
            #tasks.append(task) # add task to list of tasks
            request.session["tasks"] += [task] # append to that list of tasks thats already stored inside of the session before redirecting the user back
            # telling django to reverse engineer the url and bring the user back to that page
            return HttpResponseRedirect(reverse("tasks:index"))

        else:
            return render(request, "tasks/add.html", {
                "form":form # display information back to user
            })

    return render(request, "tasks/add.html" , {
        "form": NewTaskForm()
    })