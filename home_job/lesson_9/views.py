from django.shortcuts import render
from lesson_9.models import ModelForLesson9
from django.http import HttpResponse
from rest_framework import viewsets
from lesson_9.serialazers import SerializerForTask1


def add(request):
    rec = ModelForLesson9()
    rec.name = 'PONG'
    rec.save()
    return HttpResponse('Done!')


class ViewForTask1(viewsets.ModelViewSet):
    queryset = ModelForLesson9.objects.all()
    serializer_class = SerializerForTask1
