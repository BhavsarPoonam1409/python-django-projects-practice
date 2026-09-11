from django.db import models

# Create your models here
class Employee(models.Model):
    name= models.CharField()
    age = models.ImageField()
    email = models.EmailField()

    def __str__(self):
        return self.name