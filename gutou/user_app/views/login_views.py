from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth


# Create your views here.

# 登录的首页

def index(request):
    if request.method == "GET":
        return render(request, "index.html")

    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        if username == "" or password == "":
            return render(request, "index.html", {"error": "用户名或密码不能为空"})

        user = auth.authenticate(username=username, password=password)
        if user is None:
            return render(request, "index.html", {"error": "用户名或密码错误"})

        else:
            auth.login(request, user)  # django封装的记录用户的登录状态
            return HttpResponseRedirect("/project/")


# 退出登录
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/index/")
