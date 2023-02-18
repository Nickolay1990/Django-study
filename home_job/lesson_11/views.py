from django.shortcuts import render


def index(request):
    return render(request, 'task1.html')

