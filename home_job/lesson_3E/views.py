from django.shortcuts import render
import csv
from .models import Games
from django.http import HttpResponse


def full_base(request):
    with open('vgsales.csv', 'r') as f:
        reader = csv.reader(f)
        for raw in reader:
            game = Games()
            game.name = raw[1]
            game.platform = raw[2]
            game.developer = raw[5]
            game.save()
    return HttpResponse('done!')