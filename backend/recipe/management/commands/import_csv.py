import csv
from django.core.management import BaseCommand

from recipe.models import Ingredients


class Command(BaseCommand):
    help = "Loads ingredients from CSV file."

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def handle(self, *args, **options):
        file_path = options['filename']
        with open(file_path, 'r') as csv_file:
            data = csv.reader(csv_file)
            for row in data:
                name, measurement_unit = row
                Ingredients.objects.create(
                    name=name,
                    measurement_unit=measurement_unit,
                )
        self.stdout.write(
            self.style.SUCCESS('Loading CSV success')
        )
