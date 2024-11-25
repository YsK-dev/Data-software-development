from django.db import models

class Football(models.Model):
    LIG_CHOICES = [
        ('EPL', 'English Premier League'),
        ('LaLiga', 'La Liga'),
        ('SerieA', 'Serie A'),
        ('Bundesliga', 'Bundesliga'),
        ('Ligue1', 'Ligue 1'),
    ]

    season = models.CharField(max_length=20)
    match_day = models.IntegerField()
    date = models.DateField()
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    result = models.CharField(max_length=10)
    lig = models.CharField(max_length=20, choices=LIG_CHOICES)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} - {self.lig}"