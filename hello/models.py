from django.db import models

# Create your models here.

class Boat(models.Model):
    name = models.CharField(max_length = 120)
    status = models.BooleanField()
