from django.shortcuts import render
from .models import Products

# Create your views here.

def allproduct(request):
    data = Products.objects.all()
    context = {"product" : data}
    return render(request,'products/allproducts.html',context)

 