from django.shortcuts import render

# Create your views here.

def marksadd(request):
    return render(request,'marks/add.html')