from django.shortcuts import render,redirect
from student.models import Student
from myprod.models import Product
from contact.models import Contact
from login.models import Myuser

def home(request):  
    data = Product.objects.all()
    context = {
        "allprod" : data
    }
    return render(request, "index.html", context)


def login(request): 
    context = {}
    try:
        if(request.method == "POST"):
            email = request.POST.get("email") 
            password = request.POST.get("password") 
            
            userdata = Myuser.objects.get(email=email)

            if(userdata.password == password):
                print("login success")
                
                return redirect("home")
            else:
                print("invalid password")
                context = {
                    "msg" : "invalid password"
                }
    except:
        pass
   
    return render(request, "login.html",context)


def signup(request):
    context = {}
    try:
        if(request.method == "POST"):
            email = request.POST.get("email") 
            password = request.POST.get("password") 
            Cpassword = request.POST.get("confirmpassword") 

            if(password == Cpassword):
                # password is correct 
                # create new user in database
                Myuser.objects.create(email=email, password = password)
                return redirect("login")
                
            else:
                context = {"msg" : "password and confirm password should be same"}

          
    except:
        pass

    return render(request, "signup.html",context)






def contact(request):  
    # to add new contact in db

    try:
        if(request.method == "POST"):
            fname = request.POST.get("firstname")
            lname = request.POST.get("lastname")
            email = request.POST.get("email")
            orderid = request.POST.get("order_id")
            topic = request.POST.get("topic")
            msg = request.POST.get("message")

            Contact.objects.create(firstName = fname,lastName= lname, email=email, orderid=orderid, topic=topic,message = msg)
            print("data stored in DB")
    except:
        pass
    return render(request, "contact.html")

def about(request):  
    return render(request, "about.html")

def services(request):  
    return render(request, "services.html")
def emp(request, id):
   
    data = Student.objects.get(id=id)
    context = {
        "studata" : data
    }
    return render(request, "emp.html", context)