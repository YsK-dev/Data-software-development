from django.urls import path # type: ignore 
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('cars/', views.car_list, name='car_list'),
    path('football_games/', views.football_game_list, name='football_game_list'),
    path('football_players/', views.football_player_list, name='football_player_list'),
]
