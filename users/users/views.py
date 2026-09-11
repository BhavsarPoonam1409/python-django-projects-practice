from django.shortcuts import render 
from .forms import Userform

def userform(request):

    if(request.method == "POST"):
        myform = Userform(request.POST) # after submit which will contain data

        if(myform.is_valid()):
            print(myform.cleaned_data)

    else:
        myform = Userform() #display form
    
    return render(request, "form.html", {"myform" : myform})