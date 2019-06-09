from django.urls import path, include
from module_app import views

urlpatterns = [
    path('', views.module),
    path('add_module/', views.add_module),
    path('edit_module/<int:mid>/', views.edit_module),
    path('delete_module/<int:mid>/', views.delete_module),

]