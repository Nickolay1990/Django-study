from django.urls import path
from .views import full_base

urlpatterns = [
    path('full/', full_base)
]