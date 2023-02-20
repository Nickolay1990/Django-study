from django.urls import path
from lesson_3 import views

urlpatterns = [
    path('html/', views.html),
    path('json/', views.json),
    path('text/', views.text),
    path('redirect/', views.redirect),
    path('class/', views.MyView.as_view()),
    path('task_1/', views.task_1),
    path('main_task_2/', views.main_task_2),
    path('main_task_2/luk/', views.luk_task_2),
    path('main_task_2/leya/', views.leya_task_2),
    path('main_task_2/hun/', views.hun_task_2),
    path('task_3/', views.task_3),
]
