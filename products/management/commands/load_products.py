from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Load all products from data.csv (hardcoded)'

    def _create_product(self, colour, price, title, image, category):


        product = Product(title=title, price=float(price), category=category, colour=colour, image=image)
        product.save()


    def handle(self, *args, **options):

        with open('data.csv') as data_file:
            for line in data_file.readlines():
                split_data = [cell.strip() for cell in line.split(',')]
                # print(split_data)
                colour, price, title, image, category = split_data

                self._create_product(colour, price, title, image, category)