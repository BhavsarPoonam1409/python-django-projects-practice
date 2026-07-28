from django.shortcuts import render

def userform(request):
    n1 = 0
    n2 = 0

    context = {}
    try:
        if(request.method == "GET"):
            n1 = int(request.GET.get("n1"))
            n2 = int(request.GET.get("n2"))

            context = {
                "n1" : n1,
                "n2" : n2,
                "output" : n1 + n2
            }

    except:
        pass
    return render(request,'index.html',context)