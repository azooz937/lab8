from django.urls import path
from . import views

urlpatterns = [
    path('lab8/task7', views.task7_view, name='task7'),
]
