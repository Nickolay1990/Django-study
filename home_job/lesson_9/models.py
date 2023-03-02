from django.db import models


class ModelForLesson9(models.Model):
    name = models.CharField(max_length=64)
