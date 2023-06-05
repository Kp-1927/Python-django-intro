from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
 

 #string-message
def test_api(request):
    return HttpResponse("My First API...")

#JSON-message
def test_json_api(request):
    data={
        "name":"Khushi's API",
        "framework":"Python-Django",
        "university":"SIT"
    }
    return JsonResponse(data)
#html-Template

def test_html_page(request):
    data={
        "name":"Khushi's API",
        "framework":"Python-Django",
        "university":"SIT",
        "year":2025
    }
    return render(request,"playground/index.html",data)

#Hello,{{name}}

def test_hello_name(request,name):
    return HttpResponse(f"Hello,{name}")
def test_html_for_page(request):
    context = {
        "data" : [{
                "name" : "SIT",
                "framework" : "Python-Django",
                "year" : 2023
            }, {
                "name" : "SIT",
                "framework" : "Java-Spring-Boot",
                "year" : 2024 
            }]
        }
    return render(request, "playground/for_loop.html", context)