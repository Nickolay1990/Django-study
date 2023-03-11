from django.urls import path
from .views import *

urlpatterns = [
    path('get_user/<int:pk>', get_user),
    path('delete_user/<int:pk>', delete_user),
    path('filter/<str:name>', filter_users),
    path('all/', all_users),
]