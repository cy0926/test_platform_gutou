"""gutou URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user_app.views import login_views, project_views , module_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_views.index),
    path('index/', login_views.index),
    path('accounts/login/', login_views.index),
    path('logout/', login_views.logout),


    # 项目相关
    path('project/', project_views.project),
    path('project/add_project/', project_views.add_project),
    path('project/edit_project/<int:pid>/', project_views.edit_project),
    path('project/delete_project/<int:pid>/', project_views.delete_project),


    # 模块相关
    path('module/', module_views.module),







]
