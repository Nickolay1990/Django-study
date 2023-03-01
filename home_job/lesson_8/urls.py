from django.urls import path
from lesson_8 import views

urlpatterns = [
    path('full_base/', views.full_database_task_1, name='full'),
    path('filter_1/', views.filter_task_1, name='filter_1'),
    path('filter_2/', views.filter_task_1_2, name='filter_2'),
    path('sort/', views.sort_task_1, name='sort'),
    path('task_2/', views.task_2, name='task_2'),
    path('task_3/', views.task_3, name='task_3'),
]