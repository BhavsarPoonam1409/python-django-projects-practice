from django.shortcuts import render
from .models import Books

# Create your views here.
def home(request):
    data = Books.objects.all()
    context={"Booksdata":data}
    return render(request,'index.html',context)

def addbook(request):
    try:
        if(request.method == "GET"):
            bookname = request.GET.get("bname")
            bookimage = request.GET.get("bimage")
            authorname = request.GET.get("aname")
            price = request.GET.get("price")
            desc = request.GET.get("desc")

            Books.objects.create(
                book_name =bookname,
                book_image = bookimage,
                author_name = authorname,
                price = price,
                desc = desc
            )
    except:
        pass

    return render(request,'add.html')

def deletebook(request,id):
    deletebook = Books.objects.get(id=id)
    deletebook.delete()
    print("Books are deleted")
    return render(request,"delete.html")

def updatebook(request,id):
    data = Books.objects.get(id=id)
    print(data)
    
    try:
        if(request.method == "POST"):
            bookname = request.POST.get("bname")
            bookimage = request.POST.get("bimage")
            authorname = request.POST.get("aname")
            price = request.POST.get("price")
            desc = request.POST.get("desc")

            data.book_name = bookname
            data.book_image = bookimage
            data.author_name = authorname
            data.price = price
            data.desc = desc
            data.save()
                    

    except:
         pass

    context ={
                "booksdata" : data
            }
        

    
    return render(request,'update.html',context)