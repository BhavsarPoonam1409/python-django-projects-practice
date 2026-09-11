from django.shortcuts import render
from .models import Faculties

# Create your views here.
def fachome(request):
    data = Faculties.objects.all()
    context = {
        "facusers" : data
    }
    return render(request,"faculties/index.html", context)


def facdata(request):
    try:
        if(request.method == "POST"):
            fullname = request.POST.get("fullname")
            mobile = request.POST.get("mobile")
            email = request.POST.get("email")
            age = request.POST.get("age")

            print(fullname)

            # now we want to store this data into database
            Faculties.objects.create(
                fullname = fullname,
                mobile =  mobile,
                email = email,
                age =age,
            )
            print("data stored into database")
    except:
        pass

    return render(request, "faculties/fac.html")

def updatefac(request, id):
    facupdate = Faculties.objects.get(id=id) 
    context = {
        "facusers" :facupdate
    }
    try:
        if(request.method == "POST"):
            # updated data 
            fullname = request.POST.get("fullname")
            mobile = request.POST.get("mobile")
            email = request.POST.get("email")
            age = request.POST.get("age")

            #now we want to update this data into database
            facupdate.fullname = fullname
            facupdate.mobile = mobile
            facupdate.email = email
            facupdate.age = age
            facupdate.save()
            print("data updated into database")
            return redirect("fac_list")
    except:
        pass
    
    return render(request, "faculties/update.html", context)

def deletefac(request, id):

    targetStu = Faculties.objects.get(id=id) 
    targetStu.delete()
    print("student deleted")
    return render(request,"faculties/after.html")

