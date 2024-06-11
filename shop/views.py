from django.shortcuts import render
from .models import (Product,Category,Vendor,CartOrder,CartOrderItem,Wishlist,ProductImages,ProductReview,Address )
from django.db.models import Count
# Create your views here.


def index(request):

    # products = Product.objects.all().order_by('-id')
    products = Product.objects.filter(product_status="published").order_by('-id')
    context = {

        "products":products
    }

    return render(request,"shop/index.html",context)


def product_list_view(request):

    products = Product.objects.filter(product_status = 'published').order_by('-id')
    context = {

        'products':products
    }

    return render(request,'shop/product_list.html',context)


def category_list_view(request):

    # categories = Category.objects.all()
    categories = Category.objects.all().annotate(product_count=Count("product"))
    context = {

        'categories': categories
    }

    return render(request,'shop/category_list.html',context)