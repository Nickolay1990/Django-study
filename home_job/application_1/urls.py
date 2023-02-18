from application_1.views import answer
from django.urls import path

urlpatterns = [
    path('', answer, name='answer'),
]
