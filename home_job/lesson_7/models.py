from django.db import models


class ModelPersonTask3(models.Model):
    name = models.CharField(max_length=30)
    biography = models.CharField(max_length=30)
    age = models.IntegerField()
    stars = models.FloatField()