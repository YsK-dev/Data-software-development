from django.shortcuts import render # type: ignore
from django.core.paginator import Paginator # type: ignore
from .models import Car, FootballGame, FootballPlayer

def home(request):
    return render(request, 'home.html')
def car_list(request):
    brand_filter = request.GET.get('brand', '') 
    cars = Car.objects.all()

    if brand_filter:  
        cars = cars.filter(brand=brand_filter)
    
    paginator = Paginator(cars, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    brands = Car.objects.values_list('brand', flat=True).distinct()

    return render(request, 'car_list.html', {'cars': page_obj, 'brands': brands, 'request': request})


def football_game_list(request):
    games = FootballGame.objects.all()
    paginator = Paginator(games, 100) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'football_game_list.html', {'games': page_obj})

def football_player_list(request):
    players = FootballPlayer.objects.all()
    paginator = Paginator(players, 100) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'football_player_list.html', {'players': page_obj})
