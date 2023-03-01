from django.db import models


class ModelForLesson8Task1(models.Model):
    name = models.CharField(max_length=640)
    platform = models.CharField(max_length=64)
    year = models.IntegerField(null=True)
    genre = models.CharField(max_length=64)
    developer = models.CharField(max_length=64)
    sales1 = models.FloatField()
    sales2 = models.FloatField()
    sales3 = models.FloatField()
    sales4 = models.FloatField()
    sales5 = models.FloatField()

    def __str__(self):
        return self.name


class ModelForPersonsLesson8Task2(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class ModelForProfessionsLesson8Task2(models.Model):
    profession = models.CharField(max_length=64)
    salary = models.IntegerField()
    persons = models.ManyToManyField(ModelForPersonsLesson8Task2)

    def __str__(self):
        return self.profession
