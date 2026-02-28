from django.db import models

# Create your models here.

class CustomUser(models.Model):
    name = models.CharField(max_length=30 )
    l_name = models.CharField(max_length=40)
    age = models.IntegerField(default=23)
    nots = models.CharField(max_length=100)
