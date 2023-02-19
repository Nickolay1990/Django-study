from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def bio(request, username):
    print(username)
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def book(request, title):
    print(title)
    return render(request, 'book.html')
