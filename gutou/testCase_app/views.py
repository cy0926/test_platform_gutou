from django.shortcuts import render


# Create your views here.

def test_case_manage(request):
    return render(request, "testCase.html", {"type": "debug"})
