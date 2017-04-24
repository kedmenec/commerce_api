from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    price = models.FloatField()
    category = models.TextField()
    colour = models.TextField()
    image = models.TextField()


class Review(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    rating = models.IntegerField()
    product = models.ForeignKey(Product, related_name="reviews")

