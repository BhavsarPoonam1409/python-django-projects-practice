from django.db import models

# Create your models here.
class Marks (models.Model):
    java = models.IntegerField(max_length=100)
    python = models.IntegerField(max_length=100)
    Linux = models.IntegerField(max_length=100)
    
    