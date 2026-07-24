from django.db import models

# Create your models here.
class Faculties(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.IntegerField(max_length=12)