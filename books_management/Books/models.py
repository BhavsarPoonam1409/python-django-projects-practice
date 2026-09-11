from django.db import models

# Create your models here.

class Books(models.Model):
    book_name = models.CharField(max_length=100)
    book_image = models.CharField()
    author_name = models.CharField(max_length=100)
    price = models.IntegerField(max_length=50)
    desc = models.CharField(max_length=100)

def __str__(self):
        return self.book_name 