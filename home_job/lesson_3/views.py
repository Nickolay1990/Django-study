from django.views.generic import View
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render


def html(request):
    return render(request, 'html.html')


def json(request):
    return JsonResponse({"ret": 43, "KOlia": 32})


def text(request):
    return HttpResponse('Text Response')


def redirect(request):
    return HttpResponseRedirect('http://www.google.com')


lets_do_it = [{'priority': 100, 'task': 'Составить список дел'},
              {'priority': 150, 'task': 'Изучать Django'},
              {'priority': 1, 'task': 'Подумать о смысле жизни'}]


def task_1(request):
    return HttpResponse(lets_do_it)


class MyView(View):
    def get(self, request):
        print('this is get')
        return HttpResponse('Text Response from class')


def main_task_2(request):
    return render(request, 'main_star_wars.html')


def luk_task_2(request):
    return render(request, 'luk_star_wars.html')


def leya_task_2(request):
    return render(request, 'leya_star_wars.html')


def hun_task_2(request):
    return render(request, 'hun_star_wars.html')


def task_3(request):
    return HttpResponse('«Вот ваш файл>>', status=227)
