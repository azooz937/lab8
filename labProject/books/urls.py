from django.urls import path
from . import views

urlpatterns = [
    path('lab8/task1', views.task1_view, name='task1'),
    path('lab8/task2', views.task2_view, name='task2'),
    path('lab8/task3', views.task3_view, name='task3'),
    path('lab8/task4', views.task4_view, name='task4'),
    path('lab8/task5', views.task5_view, name='task5'),
]
