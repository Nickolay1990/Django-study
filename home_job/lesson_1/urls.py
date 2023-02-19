from lesson_1 import views
from django.urls import path

urlpatterns = [
    path('index/', views.index, name='index-view'),
    path('bio/<username>/', views.bio, name='bio'),
    path('home/', views.home, name='home-view'),
    path('book/<title>/', views.book, name='book'),
]
