from django.urls import path
from lesson_7 import views

urlpatterns = [
    path('task_1/', views.task_1, name='go_form'),
    path('task_2/', views.task_2, name='task_2'),
    path('task_3/', views.ModelFormView.as_view(), name='modelform')
]