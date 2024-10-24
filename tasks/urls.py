from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_tasks, name='get_all_tasks'),
    path('tasks/user/<int:user_id>/', views.get_user_tasks, name='get_user_tasks'),
    path('add_task/', views.add_task, name='add_task'),

]