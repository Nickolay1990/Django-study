from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Profile


def get_user(request, pk):
    user = Profile.user_manager.get(pk=pk)
    return HttpResponse(user)


def delete_user(request, pk):
    user = Profile.user_manager.delete_user(pk)
    print(user)
    return HttpResponse('deleted')


def filter_users(request, name):
    user = Profile.user_manager.get_filter(name=name)
    return HttpResponse(user)


def all_users(request):
    users = Profile.user_manager.get_all()
    return HttpResponse(users)
