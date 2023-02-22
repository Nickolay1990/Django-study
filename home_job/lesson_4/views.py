from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def show_template(request):
    latest_question_list = [
        {'id': 1, 'question_text': 'В чем смысл жизни?'},
        {'id': 2, 'question_text': 'Что первично, дух или материя?'},
        {'id': 3, 'question_text': 'Существует ли свобода воли?'}]
    template = loader.render_to_string(
        template_name='template_example.html',
        context={'latest_question_list': latest_question_list})
    return HttpResponse(template)


def show_page(request, id):
    return HttpResponse('Id of this page is ' + str(id))


def task_1(request):
    lets_do_it = [{'priority': 100, 'task': 'Составить список дел'},
                  {'priority': 150, 'task': 'Изучать Django'},
                  {'priority': 1, 'task': 'Подумать о смысле жизни'}]
    template = loader.render_to_string(
        template_name='template_for_lesson_4_task_1.html',
        context={'array': lets_do_it})
    return HttpResponse(template)


def task_2_1(request):
    return render(request, 'template_for_lesson_4_task_2_1.html')


def task_2_2(request, ids):
    message = ''
    if ids == 1:
        message = 'страница Люка: Люк Скайуокер — один из главных персонажей вселенной «Звёздных войн», джедай, сын сенатора с Набу Падме Амидалы Наберри и рыцаря-джедая Энакина Скайуокера'
    elif ids == 2:
        message = 'страница Леи: Лея Органа — дочь рыцаря-джедая Энакина Скайуокера и сенатора Падме Амидалы Наберри.'
    elif ids == 3:
        message = 'страница Хана: Хан Соло — пилот космического корабля «Тысячелетний сокол», его бортмехаником и вторым пилотом является вуки по имени Чубакка.'
    template = loader.render_to_string(
        template_name='template_for_lesson_4_task_2_2.html',
        context={'text': message})
    return HttpResponse(template)


def task_3(request):
    data = [{'name': 'Шаддам IV', 'surname': 'Коррино'},
            {'name': 'Пол', 'surname': 'Атрейдес'},
            {'name': 'Франклин', 'surname': 'Герберт'}]
    template = loader.render_to_string(
        template_name='template_for_lesson_4_task_3.html',
        context={'list_of_dict': data})
    return HttpResponse(template)
