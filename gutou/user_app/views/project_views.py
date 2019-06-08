from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from user_app.models.project import Project
from user_app.forms import ProjectForm


@login_required
def project(request):
    """
    项目管理页面
    :param request:
    :return:
    """
    project_all = Project.objects.all()
    return render(request, "project.html", {"projects": project_all,
                                            "type": "list"}
                  )


@login_required
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


@login_required
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
            # return HttpResponse("待编辑的项目不存在")
            return render(request, "project.html", {"error": "待编辑的项目不存在",
                                                    "type": "error"})
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            p = Project.objects.get(id=pid)
            """
              将form表单新的值，赋值给p.name, p.describe等
            """
            p.name = form.cleaned_data["name"]
            p.describe = form.cleaned_data["describe"]
            p.status = form.cleaned_data["status"]
            p.save()
            return HttpResponseRedirect('/project/')


@login_required
def delete_project(request, pid):
    try:
        if pid:
            Project.objects.get(id=pid).delete()
            return HttpResponseRedirect('/project/')
    except:
        # return HttpResponse("待删除的项目不存在")
        return render(request, "project.html", {"error": "待删除的项目不存在",
                                                "type": "error"})
