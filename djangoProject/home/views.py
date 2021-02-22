from django.shortcuts import render,HttpResponse
from .models import *
def home(req):
    ob=studData.objects.all()
    return render(req,"index.html",{"data":ob})

def studdata(req):
    name=req.GET.get("name")
    email=req.GET.get("email")
    course=req.GET.get("course")
    print(name,email,course)
    ob = studData(name=name,email=email,course=course)
    ob.save()
    return HttpResponse("true")