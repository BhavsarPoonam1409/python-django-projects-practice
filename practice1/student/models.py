from django.db import models

# Create your models here.

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    enrollmentno = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

def __str__(self):
    return self.fullname 