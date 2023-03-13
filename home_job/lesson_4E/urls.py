from django.urls import path
from .views import show_bootstrap, full_base

urlpatterns = [
    path('boot/', show_bootstrap),
    # path('fuul/', full_base),
]