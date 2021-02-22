from django.db import models


# Create your models here.
class studData(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
