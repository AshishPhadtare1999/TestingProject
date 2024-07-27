from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    active=models.BooleanField()
    location=models.CharField(max_length=100)
    