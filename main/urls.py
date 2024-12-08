from django.urls import path
from . import views

urlpatterns = [
    path('', views.problem_set_list, name='problem_set_list'),
    path('create/', views.problem_set_create, name='problem_set_create'),
    path('edit/<int:problem_set_id>/', views.problem_set_edit, name='problem_set_edit'),
    path('delete/<int:problem_id>/', views.problem_delete, name='problem_delete'),
    path('delete_set/<int:problem_set_id>/', views.problem_set_delete, name='problem_set_delete'),
]
