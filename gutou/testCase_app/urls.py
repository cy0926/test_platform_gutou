from django.urls import path, include
from testCase_app import views

urlpatterns = [
    path('', views.test_case_manage),



]