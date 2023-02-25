from django.db import models


class Book(models.Model):
    count = models.IntegerField(default='')
    on_shop = models.BooleanField(default='')
    name = models.CharField(max_length=30, default='')
    description = models.TextField(default='')
    email = models.EmailField(default='')
    file = models.FileField(default='')
    weight = models.FloatField(default='')
    image = models.ImageField(default='')
    site = models.URLField(default='')
    ip = models.GenericIPAddressField(default='')


class Wrape(models.Model):
    color = models.ManyToManyField(Book,
                                   verbose_name='this wrape has the same color of this books',
                                   default='')
    price = models.FloatField(default='')
    name = models.CharField(max_length=30, default='')
