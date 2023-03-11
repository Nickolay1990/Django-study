from django.contrib.auth.models import User
from django.db import models
from .managers import UserManager


class Profile(models.Model):
    level = models.CharField(max_length=64, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salary = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)

    user_manager = UserManager()
    objects = models.Manager()

    def __str__(self):
        return self.user.username
