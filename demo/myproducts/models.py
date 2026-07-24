from django.db import models

# Create your models here.
class Products(models.Model):
    image = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    quny = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)