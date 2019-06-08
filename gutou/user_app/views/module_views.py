from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# 模块管理页面
@login_required
def module(request):
    return render(request, "module.html")
