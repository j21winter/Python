from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dojo/new', views.create_dojo),
    path('dojo/delete', views.destroy_dojo),
    path('ninja/new', views.create_ninja), 
    path('ninja/delete', views.destroy_ninja)
]