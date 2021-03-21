from django.contrib import admin
from django.urls import path, include
from shoulder_bone import views

urlpatterns = [
    path('', views.home, name='Home'),
]