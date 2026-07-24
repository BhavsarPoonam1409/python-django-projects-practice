from django.db import models

# Create your models here.
class Student(models.Model):
    fullname = models.CharField(max_length=100)
    enrollment = models.IntegerField(max_length=20)
    mobileno = models.IntegerField(max_length=12)
    email = models.EmailField(max_length=50)

#for student ka name admin panel me dikhe iss liye
def __str__(self):
        return self.fullname + "" + self.enrollment 
      