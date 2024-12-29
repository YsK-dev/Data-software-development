from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Car, FootballGame, FootballPlayer

def home(request):
    return render(request, 'home.html')

def car_list(request):
    cars = Car.objects.all()
    paginator = Paginator(cars, 100)  # Show 100 cars per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'car_list.html', {'cars': page_obj})

def football_game_list(request):
    games = FootballGame.objects.all()
    paginator = Paginator(games, 100)  # Show 100 games per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'football_game_list.html', {'games': page_obj})

def football_player_list(request):
    players = FootballPlayer.objects.all()
    paginator = Paginator(players, 100)  # Show 100 players per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'football_player_list.html', {'players': page_obj})
