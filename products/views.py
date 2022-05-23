import imp
import json
from django.shortcuts import redirect,render
from .models import category,product,cart
import datetime 
# Create your views here.


def home(request):
    numofitems=0
    totalprice =0
    for v in cart.objects.all():
        numofitems=numofitems+int(v.num)
        for f in product.objects.all():
            if v.prid ==f.id:
                totalprice =totalprice +(int(f.price)*int(v.num))
    return render(request, 'index.html', {'allproducts':product.objects.all().order_by("-create_at"),'total':totalprice,'item':numofitems,'allcategory':category.objects.all()})

def productdetails(request,proid):
    numofitems=0
    totalprice =0
    for v in cart.objects.all():
        numofitems=numofitems+int(v.num)
        for f in product.objects.all():
            if v.prid ==f.id:
                totalprice =totalprice +(int(f.price)*int(v.num))      
    return render(request, 'product-details.html',{'pro':product.objects.filter(id = proid),'item':numofitems,'total':totalprice,'cat':category.objects.all()})

def presscatagory(request,categoryid):
    numofitems=0
    totalprice =0
    for v in cart.objects.all():
        numofitems=numofitems+int(v.num)
        for f in product.objects.all():
            if v.prid ==f.id:
                totalprice =totalprice +(int(f.price)*int(v.num))  
    return render(request, 'index.html',{'allproducts':product.objects.all().filter(cat =categoryid),'total':totalprice,'item':numofitems,'pro1':product.objects.all().filter(id =categoryid),'allcategory':category.objects.all()})

def cartitem(request):
    numofitems =0
    totalprice =0
    for v in cart.objects.all():
        numofitems=numofitems+int(v.num)
        for f in product.objects.all():
            if v.prid ==f.id:
                totalprice =totalprice +(int(f.price)*int(v.num)) 
                
    return render(request, 'cart.html',{'pro':product.objects.all(),'total':totalprice,'item':numofitems,'carts':cart.objects.all(),'cat':category.objects.all()})



def add(request,proid):
    numofitems=int(cart.objects.filter(prid=proid).count())
    if numofitems >= 1:
        sumofproduct=cart.objects.get(prid=proid)
        cart.objects.filter(prid=proid).update(num=int(sumofproduct.num)+1)
    else:
        carts=cart(prid=proid,num=1)
        carts.save()
    return redirect("/")

def delet(request,proid):
    numofitems=int(cart.objects.filter(prid=proid).count())
    if numofitems!=0:
        deleteoneitem=cart.objects.get(prid=proid)
        if deleteoneitem.num >1:
            cart.objects.filter(prid=proid).update(num=int(deleteoneitem.num)-1)
        
        else:
            deleteoneitem.delete()
    return redirect("/cartitem/")

    


