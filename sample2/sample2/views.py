from django.shortcuts import render
from employee.models import Employee


def home(request):
    context = {"name":"atomic habits","author":"jemas goslin","price":200,"contory":"usa"}
    return render(request,'index.html',context)

def dbdata(request):
    data=Employee.objects.all()
    context={"empdata":data}
    print(data)
    return render(request,"dbdata.html",context)
