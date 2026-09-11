from django.shortcuts import render
from employee.froms import EmployeeForm
from employee.models import Employee

# Create your views here.
def Userform(request):
    if(request.method == "POST"):
        form = EmployeeForm(request.POST)

        if(form.is_vaild()):
            form.save()

    else:
        form = EmployeeForm()

    return render(request,"form.html",{"form" : form})

def userupdate(request,id):
    #to get single emp from database
    singleEmp = Employee.objects.get(id=id)

    if(request.method == "POST"):
        form = EmployeeForm(request.POST,instance = singleEmp)

        if(form.is_vaild()):
            form.save()
            print("data updated..!!")

        else:
            form = EmployeeForm(instance = singleEmp)

        return render(request,"update.html",{"form" : form})


