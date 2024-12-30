import csv
from django.core.management.base import BaseCommand  # type: ignore
from mainapp.models import Car

class Command(BaseCommand):
    help = 'Import Car data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        file_path = options['file_path']

        field_mapping = {
            'ad_Id': 'ad_Id',
            'ad_date': 'ad_date',
            'ad_loc1': 'ad_loc1',
            'ad_loc2': 'ad_loc2',
            'brand': 'brand',
            'series': 'series',
            'model': 'model',
            'year': 'year',
            'mileage': 'mileage',
            'transmission': 'transmission',
            'fuel_type': 'fuel_type',
            'body_type': 'body_type',
            'color': 'color',
            'engine_capacity': 'engine_capacity',
            'engine_power': 'engine_power',
            'drive_type': 'drive_type',
            'vehicle_condition': 'vehicle_condition',
            'fuel_consumption': 'fuel_consumption',
            'fuel_tank': 'fuel_tank',
            'paint/replacement': 'paint_replacement',
            'trade_in': 'trade_in',
            'seller_type': 'seller_type',
            'seller_name': 'seller_name',
            'ad_price': 'ad_price',
            'ad_url': 'ad_url',
        }

        entries = []

        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                model_data = {}

                for csv_field, model_field in field_mapping.items():
                    value = row.get(csv_field, '').strip()

                    if model_field == 'mileage':
                        value = value.replace(' km', '').replace('.', '') if value else None
                    elif model_field == 'ad_price':
                        value = value.replace(' TL', '').replace('.', '') if value else None

                    model_data[model_field] = value

                try:
                    entries.append(Car(**model_data))
                except Exception as e:
                    self.stdout.write(f"Error creating entry: {e}. Row: {row}")

        Car.objects.bulk_create(entries, ignore_conflicts=True)

        self.stdout.write(f"Successfully imported {len(entries)} records.")
