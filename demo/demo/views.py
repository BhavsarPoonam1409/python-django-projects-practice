from django.shortcuts import render
from student.models import Student

def home(request):
    return render(request,"index.html")

def dbdata(request):
    data=Student.objects.all()
    context={"studata":data}
    print(data)
    return render(request,"dbdata.html",context)

def emp(request,id):
    data = Student.objects.get(id=id)
    context = {"studata" : data}
    return render(request,"emp.html",context)
