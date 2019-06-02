from django.shortcuts import render
from django.http import HttpResponse


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
        if username == "admin" and password == "admin123":
            return HttpResponse("登录成功")
        else:
            return render(request, "index.html", {"error": "用户名或密码错误"})
