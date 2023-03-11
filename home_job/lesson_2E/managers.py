from django.contrib.auth.models import User
from django.db.models import Manager


class UserManager(Manager):
    def delete_user(self, pk):
        user = User.objects.get(pk=pk)
        user.delete()

    def get_filter(self, name):
        users = User.objects.filter(username=name)
        return users

    def get_all(self):
        users = User.objects.all()
        return users