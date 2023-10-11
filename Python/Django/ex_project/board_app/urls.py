from django.urls import path
from . import views

urlpatterns = [
    path('board_list/', views.show_board_list, name='show_board_list'),    
    path('board_form/', views.board_form, name='board_form'),     
]