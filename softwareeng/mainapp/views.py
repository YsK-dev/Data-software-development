from django.shortcuts import render
from .models import Car, Football, Audio

def home(request):
    return render(request, 'home.html')

def car_view(request):
    cars = Car.objects.all()
    return render(request, 'car.html', {'cars': cars})

def football_view(request):
    leagues = ['Premier League', 'La Liga', 'Bundesliga', 'Serie A']
    selected_league = request.GET.get('league')
    football_matches = Football.objects.all()
    if selected_league:
        football_matches = football_matches.filter(league=selected_league)
    return render(request, 'football.html', {'matches': football_matches, 'leagues': leagues})

def audio_view(request):
    audios = Audio.objects.all()
    return render(request, 'audio.html', {'audios': audios})
