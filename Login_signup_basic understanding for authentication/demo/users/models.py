from django.db import models

# Create your models here.
class User(models.Model):
    image = models.CharField(max_length=255)
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    mobile = models.IntegerField()
    gender = models.CharField(max_length = 100)

    def __str__(self):
        return self.name