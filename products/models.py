from django.db import models

# Create your models here.
class Product(models.Model):
    # created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    price = models.FloatField()
    description = models.TextField()
    tags = models.TextField()
    inventory_quantity = models.IntegerField()
    # Just store the image URL.
    image_url = models.TextField()
