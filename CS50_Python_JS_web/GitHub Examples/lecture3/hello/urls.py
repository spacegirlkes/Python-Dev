from django.urls import path

from . import views # . means import from current directory

urlpatterns = [ # list of allowable urls that can be accessed for this particular app
    # "" means no aditional arguments. Nothing at the end of the route
    # views.index (views.py) (index is the function inside views.py we want to call)
    # means what view should be rendered when this empty ("") url is visited
    # Then you can optionally provide the path with a string name. Makes it easy to 
    # reference from other parts of the application
    path("", views.index, name ="index"), #loads default when using ""
    path("Elise", views.Elise, name="Elise"), # have to type in /hello/Elise to render
    path("Kelly", views.Kelly, name="Kelly"), # have to type in /hello/Kelly to render
    path("<str:name>", views.greet, name="greet") # allows me to create a custom route that lets me use any string
]