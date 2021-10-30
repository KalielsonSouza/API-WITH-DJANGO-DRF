"""geobit URL Configuration

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
from django.urls import path, include, re_path
from rest_framework import routers
from playground.api import viewset
from playground import  views
from playground.api.viewset import MeerenWomanlist

route = routers.DefaultRouter()
route.register(r"person", viewset.PersonViewSet, basename="playground")

urlpatterns = [
    path('api/', include(route.urls)),
    path('', views.simple_upload),
    re_path('list', MeerenWomanlist.as_view())
]
