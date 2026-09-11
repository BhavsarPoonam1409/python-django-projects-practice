from django.shortcuts import render

# Create your views here.
def stuhome(request):
    return render(request, "students/stu.html")

def stuedit(request):
    return render(request, "students/edit.html")
