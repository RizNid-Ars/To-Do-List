from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.base_view),
    path('tasks/', views.task_list_view),
    path('tasks/<int:id>/', views.task_detail_view),
    path('create_task/', views.task_create_view),
]