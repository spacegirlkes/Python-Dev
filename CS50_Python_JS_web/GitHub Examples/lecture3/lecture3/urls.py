"""lecture3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# urls.py file for the entire project for all of the apps that might be contained in this project
urlpatterns = [
    path('admin/', admin.site.urls),

    # add hello path and include all of the urls from urls.py of my hello application
    # This will link the url configuration files together
    # hello is the module and include urls file
    path('hello/', include("hello.urls")),
    path('newyear/', include("newyear.urls")),
    path('tasks/', include("tasks.urls"))
    ]
