from django.urls import path
from . import views

app_name = 'Tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_task, name='add_task'),
    path('mark_done/<int:task_id>/', views.mark_done, name='mark_done'),
    path('detele_task/<int:task_id>/', views.delete_task, name='delete_task')
]
