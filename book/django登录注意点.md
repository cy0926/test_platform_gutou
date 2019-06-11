### django实现登录注意点
在__index.html页面中：
```html
<form action="/login_action/" method="post">
 <input name="username">
 <input name="password">
</form>
```
* 请求路径 login_action/
* 请求方法 post
* input标签的name属性，是前端传参的名称

在__views.py文件中：
```python
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        
        user = auth.authenticate(
            username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 验证登录
            return render(request, "project_manage.html")
        else:
            return render(request, "index.html",
                                    {"error": "用户名或者密码错误"})



@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/index/")

```
* request.POST.get("username",""")获取POST请求的参数
* auth.authenticate(username=xxx,password=xxx) -- 判断用户是否存在（django自己封装的方法）
* auth.login(request,user)  django封装的记录用户的登录状态