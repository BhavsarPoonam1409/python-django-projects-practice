from django.db import models

# Create your models here.

class User(models.Model):
    image = models.CharField()
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    number = models.CharField(max_length=12)
    gender = models.CharField(max_length=50)

#Two String Method
def __str__(self):
    return self.name
