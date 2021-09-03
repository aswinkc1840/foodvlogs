from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from . models import *
from shop.models import *


def cartdetails(request,tot=0,count=0,ct_item=None):
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
        ct_item=item.objects.filter(cart=ct,active=True)
        for i in ct_item:
            tot +=(i.prod.price*i.quan)
            count+=i.quan
    except ObjectDoesNotExist:
           pass

    return render(request,'cart.html',{'ci':ct_item,'t':tot,'c':count})


def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id



def add_cart(request,product_id):
    prodt=product.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_item=item.objects.get(prod=prodt,cart=ct)
        if c_item.quan < c_item.prod.stock:
            c_item.quan+=1
        c_item.save()
    except item.DoesNotExist:
        c_item = item.objects.create(prod=prodt, quan=1, cart=ct)
        c_item.save()
    return  redirect('cartdetails')

def min_cart(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prodt=get_object_or_404(product,id=product_id)
    c_item=item.objects.get(prod=prodt,cart=ct)
    if c_item.quan>1:
        c_item.quan-=1
        c_item.save()
    else:
        c_item.delete()
    return  redirect('cartdetails')


def cart_delete(request, product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prodt = get_object_or_404(product, id=product_id)
    c_item = item.objects.get(prod=prodt, cart=ct)
    c_item.delete()
    return redirect('cartdetails')


