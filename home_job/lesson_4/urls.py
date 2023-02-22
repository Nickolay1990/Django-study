from django.urls import path
from lesson_4.views import show_template, task_1, task_2_1, task_2_2, task_3

urlpatterns = [
    path('main/', show_template),
    path('task_1/', task_1),
    path('task_2/main/', task_2_1),
    path('task_2/<int:ids>/', task_2_2),
    path('task_3/', task_3),
]