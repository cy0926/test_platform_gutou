from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from user_app.models.module import Module
from user_app.forms import ModuleForm


@login_required
def module(request):
    """
     模块管理列表
    :param request:
    :return:
    """
    if request.method == "GET":
        module_all = Module.objects.all()
        return render(request, "module.html", {"modules": module_all,
                                               "type": "list"})


@login_required
def add_module(request):
    """
    添加模块页面 + 添加模块功能
    :param request:
    :return:
    """
    if request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            project = form.cleaned_data['project']
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            Module.objects.create(project=project, name=name, describe=describe)
            return HttpResponseRedirect('/module/')
    else:
        form = ModuleForm()
        return render(request, "module.html", {"type": "add",
                                               "form": form})


@login_required
def edit_module(request, mid):
    """
    这是编辑模块页面
    :param request:
    :param mid:
    :return:
    """
    if request.method == "GET":
        print("pid____", mid)
        try:
            if mid:
                m = Module.objects.get(id=mid)
                form = ModuleForm(instance=m)
                return render(request, "module.html", {"type": "edit",
                                                       "form": form,
                                                       "id": mid})
        except:
            return render(request, "module.html", {"error": "待编辑的模块不存在~！",
                                                   "type": "error"})
    if request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            form.name = form.cleaned_data['name']
            form.describe = form.cleaned_data['describe']
            form.project = form.cleaned_data['project']
            form.save()
            return HttpResponseRedirect('/module/')


@login_required
def delete_module(request, mid):
    """
    这是删除模块功能
    :param request:
    :param pid:
    :return:
    """
    try:
        if mid:
            Module.objects.get(id=mid).delete()
            return HttpResponseRedirect('/module/')
    except:
        return render(request, "module.html", {"error": "待删除的模块不存在",
                                               "type": "error"})
