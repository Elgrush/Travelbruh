from django.db import models


# Create your models here.

class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    visits = models.JSONField(blank=True, null=True)


class Landmarks(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=8192)
    city_id = models.IntegerField()
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)
    image = models.CharField(max_length=128, default="")


class Cities(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=4096)


class LMSuggestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    city_id = models.IntegerField(default=None, blank=True, null=True)
    name = models.CharField(max_length=30)
    message = models.CharField(max_length=4096, default=None, blank=True, null=True)
