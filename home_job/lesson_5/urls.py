from django.urls import path
from lesson_5.views import create_book, create_wrape

urlpatterns = [
    path('create-book/', create_book),
    path('create-wrape/', create_wrape),
]