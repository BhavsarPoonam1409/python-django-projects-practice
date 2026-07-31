from django.shortcuts import render

def calc(request):
    context ={}
    try:
        if(request.method == "POST"):
            n1 = int(request.POST.get("num1"))
            n2 = int(request.POST.get("num2"))
            calc = request.POST.get("calc")

            if(calc == "+"):
                ans=n1+n2
            elif(calc == "-"):
                ans=n1-n2
            elif(calc == "*"):
                ans=n1*n2
            elif(calc == "/"):
                ans=n1/n2

            context = {
                "ans":ans
            }
    except:
        pass
    return render(request,'index.html',context)