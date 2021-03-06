from gc import get_objects
from unicodedata import category

from django.shortcuts import render, get_object_or_404
from .models import product, categ
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage


# Create your views here.


def home(request):
    return render(request,'index.html')




def details(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prodt=product.objects.filter(category=c_page,available=True)
    else:
        prodt = product.objects.all().filter(available=True)
    cat=categ.objects.all()
    paginator=Paginator(prodt,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)
    return render(request,'products.html',{'p':prodt,'ct':cat,'pg':pro})


def single(request,c_slug,product_slug):
    try:
       pr= product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'single-product.html',{'i':pr})

def about(request):

    return render(request,'about.html')

def contact(request):

    return render(request,'contact.html')

def searhing(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=product.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))

    return render(request,'search.html',{'qr':query,'pr':prod})
