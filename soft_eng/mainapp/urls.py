from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.car_list, name='car_list'),
    path('football_games/', views.football_game_list, name='football_game_list'),
    path('football_players/', views.football_player_list, name='football_player_list'),
    path('voices/', views.voice_list, name='voice_list'),
]
