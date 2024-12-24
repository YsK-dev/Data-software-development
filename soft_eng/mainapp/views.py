from django.shortcuts import render
from .models import Car, FootballGame, FootballPlayer

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

def football_game_list(request):
    games = FootballGame.objects.all()
    return render(request, 'football_game_list.html', {'games': games})

def football_player_list(request):
    players = FootballPlayer.objects.all()
    return render(request, 'football_player_list.html', {'players': players})
