from django.db.models import Q
from django.shortcuts import render
import csv
from lesson_8.models import ModelForLesson8Task1, \
    ModelForProfessionsLesson8Task2, ModelForPersonsLesson8Task2
from django.http import HttpResponse
import io


def full_database_task_1(request):
    with io.open('vgsales.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            rec = ModelForLesson8Task1()
            rec.name = row[1]
            rec.platform = row[2]
            if row[3] != 'N/A':
                rec.year = row[3]
            rec.genre = row[4]
            rec.developer = row[5]
            rec.sales1 = row[6]
            rec.sales2 = row[7]
            rec.sales3 = row[8]
            rec.sales4 = row[9]
            rec.sales5 = row[10]
            rec.save()
    return HttpResponse('Fulled!')


def filter_task_1(request):
    query_set = ModelForLesson8Task1.objects.filter(name__startswith='L')
    print(query_set)
    return render(request, template_name='templates_for_lesson_8_task_1.html',
                  context={'queries': query_set})


def filter_task_1_2(request):
    query_set = ModelForLesson8Task1.objects.filter(
        Q(name__contains='1') | Q(name__contains='2') | Q(
            name__contains='3') | Q(name__contains='4') | Q(
            name__contains='5') | Q(name__contains='6') | Q(
            name__contains='7') | Q(name__contains='8') | Q(
            name__contains='9') | Q(name__contains='0'))
    print(len(query_set))
    return render(request, template_name='templates_for_lesson_8_task_1.html',
                  context={'queries': query_set})


def sort_task_1(request):
    query_set = ModelForLesson8Task1.objects.all().order_by('id')
    print(len(query_set))
    return render(request, template_name='templates_for_lesson_8_task_1.html',
                  context={'queries': query_set})


def task_2(request):
    query_set = ModelForProfessionsLesson8Task2.objects.filter(persons__id=3)
    print(query_set)
    return HttpResponse(query_set)


def task_3(request):
    query_set = ModelForProfessionsLesson8Task2.objects.filter(
        persons__name='Валерiя')
    return HttpResponse(query_set)
