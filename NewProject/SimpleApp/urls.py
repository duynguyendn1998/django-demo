from django.urls import path
from SimpleApp import views

urlpatterns = [
   path('', views.home),
]