from django.urls import path, include
from testCase_app import views

urlpatterns = [
    path('', views.test_case_manage),
    path('debug/', views.debug),
    path('test_assert/', views.test_assert),





]