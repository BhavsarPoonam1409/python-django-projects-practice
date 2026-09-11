from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def allusers(request):
    data = User.objects.all()
    context = {
        "allusers" : data
    }
    return render(request,"users/index.html", context)

def adduser(request):

    try:
        if(request.method == "GET"):
            inputimage = request.GET.get("image")
            name = request.GET.get("name")
            age = request.GET.get("age")
            mobile = request.GET.get("mobile")
            gender = request.GET.get("gender")

            # now we want to store this data into database
            User.objects.create(
                image = inputimage,
                name = name,
                age = age,
                mobile = mobile,
                gender = gender
            )
            print("data stored into database")
            
    except:
        pass

    return render(request,"users/form.html")

def updateUser(request, id):
    userupdate = User.objects.get(id=id) 
    context = {
        "studata" :userupdate
    }
    try:
        if(request.method == "POST"):
            # updated data 
            inputimage = request.POST.get("image")
            name = request.POST.get("name")
            age = request.POST.get("age")
            mobile = request.POST.get("mobile")
            gender = request.POST.get("gender")

            #now we want to update this data into database
            userupdate.image = inputimage
            userupdate.name = name
            userupdate.age = age
            userupdate.mobile = mobile
            userupdate.gender = gender
            userupdate.save()
            print("data updated into database")
            return redirect("users_list")
    except:
        pass
    
    
    return render(request, "users/update.html", context)

def deleteUser(request, id):

    targetStu = User.objects.get(id=id) 
    targetStu.delete()
    print("student deleted")
    return render(request,"users/afterdelete.html")

def singleUser(request, id):

    data = User.objects.get(id=id)
    context = {
        "singleuser" : data
    }
    return render(request,"users/singleuser.html", context)