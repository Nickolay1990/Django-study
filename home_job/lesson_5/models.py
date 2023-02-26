from django.db import models


class Book(models.Model):
    count = models.IntegerField(null=True)
    on_shop = models.BooleanField(null=True)
    name = models.TextField(null=True)
    email = models.EmailField(null=True)
    weight = models.FloatField(null=True)
    site = models.URLField(null=True)
    ip = models.GenericIPAddressField(null=True)
    test = models.CharField(max_length=43)


class Wrape(models.Model):
    color = models.ManyToManyField(Book,
                                   verbose_name='this wrape has the same color of this books')
    price = models.FloatField(null=True)
    name = models.CharField(max_length=30, null=True)
