from django.shortcuts import render
from .models import (Product,Category,Vendor,CartOrder,CartOrderItem,Wishlist,ProductImages,ProductReview,Address )
# Create your views here.


def index(request):

    # products = Product.objects.all().order_by('-id')
    products = Product.objects.filter(product_status="published",featured=True)
    context = {

        "products":products
    }

    return render(request,"shop/index.html",context)
