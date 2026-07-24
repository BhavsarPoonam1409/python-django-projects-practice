from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def loop(request):
    context = {
        "loop" : [1,2,3,4,5,6,7,8,9,10],
    }
    return render(request,"loop.html",context)

def conditions(request):
    context = {
        "conditions" : [1,2,3,4,5,6,7,8,9,10],
    }
    return render(request,"conditions.html",context)

#even odd no print
def even_odd(request):
    context = {
        "even_odd" : [1,2,3,4,5,6,7,8,9,10],
    }
    return render(request,"even_odd_no.html",context)

def nested_condition(request):
    context = {
        "nested_condition" : [1,2,3,4,5,6,7,8,9,10],
    }
    return render(request,"nested_condition.html",context)