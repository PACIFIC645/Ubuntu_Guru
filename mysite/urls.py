"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  
"""

# mysite/urls.py

from django.contrib import admin
from django.urls import path, include
from polls.views import view_polls_live  # Import the view function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Ubuntu_Guru.urls', namespace='Ubuntu_Guru')),
    path('polls/', include(('polls.urls', 'polls'), namespace='polls')),
    path('view-polls/live/', view_polls_live, name='live_polls_redirect'),
]

