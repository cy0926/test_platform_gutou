from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
import requests


# Create your views here.

def test_case_manage(request):
    return render(request, "testCase.html", {"type": "debug"})


def debug(request):
    """
    测试用例调试
    :param request:
    :return:
    """
    if request.method == "POST":
        url = request.POST.get("url", "")
        method = request.POST.get("method", "")
        header = request.POST.get("header", "")
        param_type = request.POST.get("param_type")
        parameter = request.POST.get("parameter", "")

        if url == "":
            return JsonResponse({"result": "url不能为空"})

        if header == "":
            header = {}
        try:
            header = json.loads(header.replace("\'", "\""))
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "header类型错误"})

        if parameter == "":
            parameter = {}
        try:
            payload = json.loads(parameter.replace("\'", "\""))
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "参数类型错误"})

        if method == "get":
            result = requests.get(url, params=payload, headers=header)
            result_text = result.text

        if method == "post":
            if param_type == "form":
                result = requests.post(url, data=payload, headers=header)
                result_text = result.text

            if param_type == "json":
                result = requests.post(url, json=payload, headers=header)
                result_text = result.text

        if method == "put":
            result = requests.put(url, data=payload)
            result_text = result.text

        if method == "delete":
            result = requests.delete(url)
            result_text = result.text

        return JsonResponse({"result": result_text})
    else:
        return JsonResponse({"result": "请求方法错误"})


def test_assert(request):
    """
    测试用例的断言
    :param request:
    :return:
    """
    if request.method == "POST":
        result_text = request.POST.get("result", "")
        assert_text = request.POST.get("assert", "")
        assert_type = request.POST.get("assert_type", "")

        if result_text == "" or assert_text == "":
            return JsonResponse({"result": "断言的文本不能为空"})

        if assert_type == "contains":
            if assert_text not in result_text:
                return JsonResponse({"result": "断言失败"})
            else:
                return JsonResponse({"result": "断言成功"})
        if assert_type == "mathches":
            if assert_text != result_text:
                return JsonResponse({"result": "断言失败"})
            else:
                return JsonResponse({"result": "断言成功"})

    else:
        return JsonResponse({"result": "请求方法错误"})
