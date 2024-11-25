from django.db import models

class Football(models.Model):
    season = models.CharField(max_length=20)
    match_day = models.IntegerField()
    date = models.DateField()
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    result = models.CharField(max_length=10)
