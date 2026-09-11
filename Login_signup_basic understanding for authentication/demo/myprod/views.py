from django.shortcuts import render
from .models import Product

# Create your views here.

def allproducts(request):

    data = Product.objects.all()
    context = {
        "allprod" : data
    }
    return render(request,"products/index.html", context)
