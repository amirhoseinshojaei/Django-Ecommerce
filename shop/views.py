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


def category_product_list_view(request,cid):

    category = Category.objects.get(cid=cid) #or use get object or 404
    products = Product.objects.filter(product_status = 'published',category=category)

    context = {

        'category':category,
        'products':products
        
    }

    return render(request,'shop/category_product_list.html',context)


def vendor_list_view(request):

    vendors = Vendor.objects.all()
    context = {
        'vendors':vendors
    }

    return render(request,'vendor/list.html',context)


def vendor_detail_view(request,vid):

    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(vendor=vendor,product_status = 'published')
    context = {
        'vendor': vendor,
        'products':products,
    }

    return render(request,'vendor/detail.html',context)


def product_detail_view(request,pid):

    product = Product.objects.get(pid=pid)
    context = {

        'product':product,
    }

    return render(request,'shop/product_detail.html',context)