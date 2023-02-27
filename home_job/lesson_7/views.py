from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from lesson_7.forms import ReviewForTask1, AuthorizationForTask2, \
    FormFromModelTask3


def task_1(request):
    form = ReviewForTask1(request.GET)
    if form.is_valid():
        print(form.cleaned_data.items())
        print(form.errors)
    return render(request, 'form_for_lesson_7_task_1.html',
                  context={'items': form})


def task_2(request):
    form = AuthorizationForTask2(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    else:
        print(form.errors)
    return render(request, 'form_for_lesson_7_task_2.html',
                  context={'auto': form})


class ModelFormView(FormView):
    form_class = FormFromModelTask3
    template_name = 'lesson_7_task_3.html'
    success_url = reverse_lazy('modelform')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
