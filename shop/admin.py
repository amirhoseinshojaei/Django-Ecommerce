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


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['title','category_image']



class VendorAdmin(admin.ModelAdmin):

    list_display =[

        'user','title','vendor_image','contact',
    ]


class CartOrderAdmin(admin.ModelAdmin):

    list_display = [

        'user','price','paid_status','order_date','product_status'
    ]



class CartOrderItemsAdmin(admin.ModelAdmin):

    list_display = [

        'order','invoice_no','item','image','qty','price','total'
    ]



class ProductReviewAdmin(admin.ModelAdmin):
    pass