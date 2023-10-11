from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.show_info, name='show_info'), 
           
]