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
from django.urls import path, include
from user_app.views import login_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_views.index),
    path('index/', login_views.index),
    path('accounts/login/', login_views.index),
    path('logout/', login_views.logout),


    # 项目相关
    path('project/', include('project_app.urls')),

    # 模块相关`
    path('module/', include('module_app.urls')),





]
