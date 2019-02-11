from django.conf.urls import url
from django.urls import path
from django.conf.urls import include 
from django.contrib import admin
from .views import home, students, courses

urlpatterns = [
    path(r'', home),
    path(r'students/', students),
    path(r'courses/', courses)
]