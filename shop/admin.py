from django.contrib import admin
from .models import (Product,Category,Vendor,CartOrder,CartOrderItem,Wishlist,ProductImages,ProductReview,Address )
# Register your models here.


class ProductImagesAdmin(admin.TabularInline):

    model = ProductImages



class ProductAdmin(admin.ModelAdmin):

    inlines = [ProductImagesAdmin]
    list_display =[

        'user','title','product_image','price','featured','product_status'
    ]


