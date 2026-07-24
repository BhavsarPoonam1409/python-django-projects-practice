from django.shortcuts import render
from student.models import Student

def home(request):
    return render(request,"index.html")

def dbdata(request):
    data = Student.objects.all()
    context={"studata":data}

    return render(request,"dbdata.html",context)