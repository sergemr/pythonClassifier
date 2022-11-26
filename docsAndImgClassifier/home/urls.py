from django.urls import path
from . import views
# Url Config
urlpatterns = [
    path('', views.home, name='home'),
]
