from django.shortcuts import render
from django.http import HttpResponse
from lesson_5.models import Book, Wrape


def create_book(request):
    dune = Book()
    dune.count = 2
    dune.on_shop = True
    dune.name = 'Gerbert'
    dune.description = 'Book about dune'
    dune.email = 'dune@dune.com'
    dune.weight = 3.22
    dune.site = 'http://dune.com'
    dune.ip = '127.0.0.1'
    dune.save()
    return HttpResponse('created')


def create_wrape(request):
    wrape = Wrape()
    wrape.price = 3.12
    wrape.name = 'salofan'
    wrape.save()
    return HttpResponse('created!')
