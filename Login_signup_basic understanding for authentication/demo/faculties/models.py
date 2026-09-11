from django.db import models

# Create your models here.
class Faculties(models.Model):
    fullname = models.CharField(max_length = 100)
    mobile = models.CharField(max_length = 12)
    email = models.EmailField()
    age = models.CharField(max_length = 3)

    