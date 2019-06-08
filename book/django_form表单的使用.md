### Django表单使用
参考：
https://docs.djangoproject.com/en/2.1/topics/forms/ 

参考：
https://docs.djangoproject.com/en/2.1/topics/forms/modelforms/

操作步骤：
1、需要创建一个forms.py的文件，并生成如下所示的样例类
```python
from django import forms
from user_app.models.project import Project


class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['name', 'describe', 'status']
        exclude = ['create_time']

```
* fieled 表示显示的字段
* exclude 表示屏蔽的字段

2、模版xxx.html需要用到form的样例
```html
   <!--这是添加项目-->
    {% if type == "add" %}
     <h4 class="sub-header">添加项目</h4>
        <form action="/project/add_project/" method="post">
            {{ form.as_p }}
          <button type="submit" class="btn btn-primary">
            保存
          </button>
          <button type="submit" class="btn btn-primary"
            onclick="window.location.href='/project/'">
            返回
          </button>
          {% csrf_token %}
        </form>
    {% endif %}


```
* {{ form.as_table }} 将它们作为表单封装在```<tr>```标签中。
* {{ form.as_p }} 将它们封装在```<p>```标签中。
* {{ form.as_ul }} 将它们封装在```<li>```标签中。

3、views中使用form对应的样例代码
```python
from django.http import HttpResponseRedirect
from django.shortcuts import render
from user_app.models.project import Project

from user_app.forms import ProjectForm

def add_project(request):
    """
    添加项目
    :param request:
    :return:
    """
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']
            Project.objects.create(name=name, describe=describe, status=status)
            return HttpResponseRedirect('/project/')
    else:
        form = ProjectForm()
        return render(request, "project.html", {"type": "add",
                                                "form": form}
                      )


def edit_project(request, pid):
    """
    编辑项目
    :param request:
    :return:
    """
    if request.method == "GET":
        try:
            if pid:
                p = Project.objects.get(id=pid)
                """
                子类ModelForm 可以接受现有的模型实例作为关键字参数instance,
                如果提供了这个，save()
                将更新该实例
                ps：instance其实就是此处ProjectForm的实例
                """
                form = ProjectForm(instance=p)
                return render(request, "project.html", {"type": "edit",
                                                        "form": form,
                                                        "id": pid})
        except:
            return HttpResponse("待编辑的项目不存在")
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            p = Project.objects.get(id=pid)
            p.name = form.cleaned_data["name"]
            p.describe = form.cleaned_data["describe"]
            p.status = form.cleaned_data["status"]
            p.save()
            return HttpResponseRedirect('/project/')

```

* instance其实就是此处ProjectForm的实例
* is_valid()方法，它所有字段的一个验证方法，调用它时，若所有的字段都包含了有效数据，
  则它就返回True，并将表单的数据放在其cleaned_data属性中。
* form.cleaned_data：访问“干净”数据，规避有些字段输入不合法等情况
* cleaned_data的官方解释：类中的每个字段Form不仅负责验证数据，还负责“清理”它 - 将其标准化为一致的格式。
  这是一个很好的功能，因为它允许以各种方式输入特定字段的数据，始终产生一致的输出