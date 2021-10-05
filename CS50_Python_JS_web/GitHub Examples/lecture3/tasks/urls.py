from django.urls import path

from . import views

app_name = "tasks" # unique identifier to make sure you are calling the right app to render. See index.html line 10
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add") # calling the "add" def from views.py

]