from django.urls import path
from . import views

urlpatterns = [
  
    path('', views.event_list, name='event_list'),
    path('', views.home, name='home'),
]