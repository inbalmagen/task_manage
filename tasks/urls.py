from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_tasks, name='get_all_tasks'),
#     path('task/<int:task_id>/', views.task_detail, name='task_detail'),
#     path('create/', views.create_task, name='create_task'),
#     path('update/<int:task_id>/', views.update_task, name='update_task'),
#     path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]