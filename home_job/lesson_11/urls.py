from lesson_11.views import index
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
]
