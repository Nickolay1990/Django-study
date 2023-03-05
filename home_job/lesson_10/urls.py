from django.urls import path, include, re_path
from lesson_10 import views
from rest_framework import routers

urlpatterns = [
    path('api/', views.GamesApiList.as_view()),
    path('api/<int:pk>', views.GamesApiUpdate.as_view()),
    path('api_delete/<int:pk>', views.GamesApiDestroy.as_view()),
    path('drf_auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('add_cityes/', views.CityesFormView.as_view(), name='cityes'),
    path('time/<str:city>', views.GetTime.as_view()),
    path('api_ret_id/<int:pk>', views.GamesApiRetrieveId.as_view()),
    path('api_ret_name/<str:name>', views.GamesApiRetrieveName.as_view()),
]
