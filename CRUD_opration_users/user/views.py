from django.shortcuts import render,redirect
from .models import User

# Create your views here.

# def home(request):
#     return render(request,'user/home.html')

def home(request):
    data = User.objects.all()

    context = {
        "alluser" : data
    }
    return render(request,'user/alluser.html',context)

def singleuser(request,id):
    data = User.objects.get(id=id)
    context = {
        "singleuser" :data
    }
    return render(request,'user/singleuser.html',context)

def adduser(request):
    try:
        if(request.method == "GET"):
            image = request.GET.get("image")
            name = request.GET.get("name")
            age = request.GET.get("age")
            number = request.GET.get("number")
            gender = request.GET.get("gender")

            User.objects.create(
               image = image,
               name = name,
               age = age,
               number = number,
               gender = gender
           )

    except:
        pass
    return render(request,'user/adduser.html')

def deleteuser(request,id):
    targetstu = User.objects.get(id=id)
    targetstu.delete()
    return render(request,'user/deleteuser.html')

def updateuser(request,id):
    data = User.objects.get(id=id)

    context = {
        "updateuser" : data
    }

    try:
        if(request.method == "POST"):
            image = request.POST.get("image")
            name = request.POST.get("name")
            age = request.POST.get("age")
            number = request.POST.get("number")
            gender = request.POST.get("gender")

            data.image = image
            data.name = name
            data.age = age
            data.number = number
            data.gender = gender
            data.save()
            return redirect("user_list")

    except:
        pass
            

    return render(request,'user/updateuser.html',context)