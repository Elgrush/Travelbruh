from django.db import models

# Create your models here.

class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Landmarks(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=3000)
    city_id = models.IntegerField()

class Cities(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=3000)