from django.db import models


class Games(models.Model):
    name = models.CharField(max_length=250)
    developer = models.CharField(max_length=244)
    platform = models.CharField(max_length=123)
    color = models.BooleanField(default=False)

    def __str__(self):
        return self.name