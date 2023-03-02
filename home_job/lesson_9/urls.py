from django.urls import path, include
from lesson_9 import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'ping', views.ViewForTask1)

urlpatterns = [
    path('add/', views.add),
    path('task/', include(router.urls))
]
