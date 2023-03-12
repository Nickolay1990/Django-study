from django.db import models


class Games(models.Model):
    name = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
    developer = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    genre = models.ForeignKey(Games, null=True, blank=True,
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Sell(models.Model):
    disc = models.ForeignKey(Games, on_delete=models.CASCADE, null=True, blank=True)
    price = models.FloatField()
    sell = models.IntegerField()

    def __str__(self):
        return self.disc