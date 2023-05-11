from django.urls import path
from task_api import views

urlpatterns = [
    path('task_api/', views.task_list),
    path('task_api/<str:pk>/', views.task_detail),
]
