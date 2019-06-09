from django.urls import path, include
from project_app import views

urlpatterns = [
    path('', views.project),
    path('add_project/', views.add_project),
    path('edit_project/<int:pid>/', views.edit_project),
    path('delete_project/<int:pid>/', views.delete_project),



]