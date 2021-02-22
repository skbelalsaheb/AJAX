
from django.contrib import admin
from django.urls import path
from . views import *
urlpatterns = [
    path('',home,name="Home"),
    path('studData',studdata,name="Home"),
]
