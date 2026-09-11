from django.db import models

# Create your models here.
class Student(models.Model):
    fullname = models.CharField(max_length = 100)
    mobile = models.CharField(max_length = 12)
    email = models.EmailField()
    
    def __str__(self):
        return self.fullname

