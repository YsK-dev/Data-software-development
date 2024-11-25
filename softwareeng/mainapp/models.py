from django.db import models # type: ignore

class Car(models.Model):
    ad_Id = models.AutoField(primary_key=True)
    ad_date = models.DateField()
    ad_neighborhood = models.CharField(max_length=100)
    ad_district = models.CharField(max_length=100)
    ad_province = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    series = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    mileage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    body_type = models.CharField(max_length=50)
    engine_power = models.IntegerField()
    engine_capacity = models.DecimalField(max_digits=6, decimal_places=2)
    color = models.CharField(max_length=50)
    ad_price = models.DecimalField(max_digits=10, decimal_places=2)
    ad_url = models.URLField()

    def __str__(self):
        return f"{self.brand} {self.model} - {self.ad_price}"

class Football(models.Model):
    LEAGUE_CHOICES = [
        ('Premier League', 'Premier League'),
        ('La Liga', 'La Liga'),
        ('Bundesliga', 'Bundesliga'),
        ('Serie A', 'Serie A'),
    ]

    season = models.CharField(max_length=20)
    match_day = models.IntegerField()
    date = models.DateField()
    home_team = models.CharField(max_length=50)
    away_team = models.CharField(max_length=50)
    result = models.CharField(max_length=10)
    league = models.CharField(max_length=20, choices=LEAGUE_CHOICES)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} - {self.result}"

class Audio(models.Model):
    audio_file = models.FileField(upload_to='audio/')

    def __str__(self):
        return f"Audio {self.id}"
