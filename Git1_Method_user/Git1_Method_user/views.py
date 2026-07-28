from django.shortcuts import render

def userform(request):
    name = request.GET.get("name")
    email = request.GET.get("email")

    context = {
        "name" : name,
        "email" : email,
    }
    return render(request,"index.html",context)