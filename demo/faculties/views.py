from django.shortcuts import render

# Create your views here.

def fachome(request):
    return render(request,"faculties/fachome.html")

def facadd(request):
    return render(request,"faculties/facadd.html")