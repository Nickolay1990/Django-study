from django.http import HttpResponse


def answer(response):
    return HttpResponse('Hello world')

