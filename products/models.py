from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    price = models.FloatField()
    category = models.TextField()
    colour = models.TextField()
    image = models.TextField()
