from django.urls import path
from . import views
from django.shortcuts import render

from fileUpload import views
from home import views as home_views

# Url Config
urlpatterns = [
    path('', views.upload, name='upload'),
    path('/fileupload/*', views.upload, ),
]
