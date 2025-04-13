from django.shortcuts import render

# Create your views here.
# your_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]


