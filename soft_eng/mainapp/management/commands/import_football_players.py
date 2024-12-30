import csv
from django.core.management.base import BaseCommand #type: ignore
from mainapp.models import FootballPlayer

class Command(BaseCommand):
    help = 'Import FootballPlayer data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        file_path = options['file_path']

        field_mapping = {
            'index': 'index',
            'Player': 'Player',
            '#': 'number',
            'Nation': 'Nation',
            'Pos': 'Pos',
            'Age': 'Age',
            'Min': 'Min',
            'Gls': 'Gls',
            'Ast': 'Ast',
            'PK': 'PK',
            'PKatt': 'PKatt',
            'Sh': 'Sh',
            'SoT': 'SoT',
            'CrdY': 'CrdY',
            'CrdR': 'CrdR',
            'Touches': 'Touches',
            'Tkl': 'Tkl',
            'Int': 'Int',
            'Blocks': 'Blocks',
            'xG': 'xG',
            'npxG': 'npxG',
            'xAG': 'xAG',
            'SCA': 'SCA',
            'GCA': 'GCA',
            'Cmp_x': 'Cmp_x',
            'Att_x': 'Att_x',
            'Cmp%_x': 'Cmp_pct_x',
            'PrgP': 'PrgP',
            'Carries': 'Carries',
            'PrgC': 'PrgC',
            'Att_x.1': 'Att_x_alt',
            'Succ': 'Succ',
            'SoTA': 'SoTA',
            'GA': 'GA',
            'Saves': 'Saves',
            'Save%': 'Save_pct',
            'PSxG': 'PSxG',
            'Cmp_y': 'Cmp_y',
            'Att_y': 'Att_y',
            'Cmp%_y': 'Cmp_pct_y',
            'Att (GK)': 'Att_GK',
            'Thr': 'Thr',
            'Launch%': 'Launch_pct',
            'AvgLen': 'AvgLen',
            'Opp': 'Opp',
            'Stp': 'Stp',
            'Stp%': 'Stp_pct',
            'AvgDist': 'AvgDist',
            'home': 'home',
            'game_id': 'game_id',
            'Cmp': 'Cmp',
            'Att': 'Att',
            'Cmp%': 'Cmp_pct',
            'Att.1': 'Att_alt',
        }

        entries = []

        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                model_data = {model_field: row[csv_field] for csv_field, model_field in field_mapping.items() if csv_field in row}

                for field, value in model_data.items():
                    if value == '':
                        model_data[field] = None

                try:
                    entries.append(FootballPlayer(**model_data))
                except Exception as e:
                    self.stdout.write(f"Error creating entry: {e}. Row: {row}")

        FootballPlayer.objects.bulk_create(entries, ignore_conflicts=True)

        self.stdout.write(f"Successfully imported {len(entries)} records.")