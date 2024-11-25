# FILE: your_app/management/commands/import_data.py
import csv
from django.core.management.base import BaseCommand # type: ignore
from mainapp.models import Car, Football, Audio

class Command(BaseCommand):
    help = 'Import data from CSV files into the database'

    def handle(self, *args, **kwargs):
        self.import_cars()
        self.import_football()
        self.import_audio()

    def import_cars(self):
        with open('path/to/cars.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Car.objects.create(
                    ad_Id=row['ad_Id'],
                    ad_date=row['ad_date'],
                    ad_neighborhood=row['ad_neighborhood'],
                    ad_district=row['ad_district'],
                    ad_province=row['ad_province'],
                    brand=row['brand'],
                    series=row['series'],
                    model=row['model'],
                    year=row['year'],
                    mileage=row['mileage'],
                    fuel_type=row['fuel_type'],
                    transmission=row['transmission'],
                    body_type=row['body_type'],
                    engine_power=row['engine_power'],
                    engine_capacity=row['engine_capacity'],
                    color=row['color'],
                    ad_price=row['ad_price'],
                    ad_url=row['ad_url']
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported Car data'))

    def import_football(self):
        with open('path/to/football.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Football.objects.create(
                    season=row['season'],
                    match_day=row['match_day'],
                    date=row['date'],
                    home_team=row['home_team'],
                    away_team=row['away_team'],
                    result=row['result'],
                    league=row['league']
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported Football data'))

    def import_audio(self):
        with open('path/to/audio.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Audio.objects.create(
                    audio_file=row['audio_file']
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported Audio data'))