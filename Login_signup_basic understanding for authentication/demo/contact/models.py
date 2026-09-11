from django.db import models

# Create your models here.
class Contact(models.Model):
    firstName = models.CharField(max_length = 100)
    lastName  = models.CharField(max_length = 100)
    email     = models.EmailField(max_length = 100)
    orderid   = models.CharField(max_length = 100)
    topic     = models.CharField(max_length = 100)
    message   = models.CharField(max_length = 100)

    def __str__(self):
        return self.firstName