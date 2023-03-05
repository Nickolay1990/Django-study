from django.contrib.auth.models import User
from django.db import models


class GamesBase(models.Model):
    name = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    sale = models.FloatField()
    user = models.ForeignKey(User, verbose_name='Polzovatel',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Cityes(models.Model):
    city = models.CharField(max_length=20)
    time = models.CharField(max_length=20)

    def __str__(self):
        return self.city
