import csv
from django.core.management.base import BaseCommand # type: ignore
from mainapp.models import Car, FootballGame, FootballPlayer # type: ignore

class Command(BaseCommand):
    help = 'Import CSV data into the database'

    def add_arguments(self, parser):
        parser.add_argument('model', type=str, help='The model to import data into (Car, FootballGame, FootballPlayer)')
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        model = options['model']
        csv_file = options['csv_file']

        if model not in ['Car', 'FootballGame', 'FootballPlayer']:
            self.stdout.write(self.style.ERROR('Invalid model name. Use Car, FootballGame, or FootballPlayer.'))
            return

        model_class = {'Car': Car, 'FootballGame': FootballGame, 'FootballPlayer': FootballPlayer}[model]

        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            entries = []

            for row in reader:
                try:
                    entries.append(model_class(**row))
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f"Skipping row due to error: {e}"))

            model_class.objects.bulk_create(entries)
            self.stdout.write(self.style.SUCCESS(f"Successfully imported {len(entries)} records into {model}."))
