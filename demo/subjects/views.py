from django.shortcuts import render

# Create your views here.

def subadd(request):
    return render(request,'subjects/subadd.html')

def subupdate(request):
    return render(request,'subjects/subupdate.html')