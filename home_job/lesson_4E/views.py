from django.shortcuts import render
from lesson_4E.models import Games
import csv


def show_bootstrap(request):
    queryset = Games.objects.all()
    odd_dict = []
    for i in queryset:
        if i.id % 2 == 0:
            odd_dict.append(i)
    return render(request, 'for_task_2.html', context={'games': odd_dict})


def full_base(request):
    with open('vgsales.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            game = Games()
            game.name = row[1]
            game.developer = row[5]
            game.platform = row[2]
            print(game)
            game.save()
    queryset = Games.objects.all()
    return render(request, 'main/main_page.html', context={'games': queryset})