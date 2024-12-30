import csv
from django.core.management.base import BaseCommand  # type: ignore
from mainapp.models import FootballGame

class Command(BaseCommand):
    help = 'Import FootballGame data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        file_path = options['file_path']

        field_mapping = {
            'Wk': 'Wk',
            'Day': 'Day',
            'Date': 'Date',
            'Time': 'Time',
            'Home': 'Home',
            'Away': 'Away',
            'Score': 'Score',
            'xG': 'xG',
            'xG.1': 'xG_1',
            'season': 'season',
            'game_id': 'game_id',
        }

        entries = []

        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                model_data = {model_field: row[csv_field] for csv_field, model_field in field_mapping.items() if csv_field in row}

                for field, value in model_data.items():
                    if value == '':
                        model_data[field] = None
                    elif field in ['Wk', 'xG', 'xG_1', 'game_id'] and value is not None:
                        model_data[field] = float(value)

                try:
                    entries.append(FootballGame(**model_data))
                except Exception as e:
                    self.stdout.write(f"Error creating entry: {e}. Row: {row}")

        FootballGame.objects.bulk_create(entries, ignore_conflicts=True)

        self.stdout.write(f"Successfully imported {len(entries)} records.")
