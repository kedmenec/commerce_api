from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Clear all entries from the Product table'

    def _delete_all_products(self):
        Product.objects.all().delete()



    def handle(self, *args, **options):

        self._delete_all_products()