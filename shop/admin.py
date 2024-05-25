from django.contrib import admin
from .models import (Product,Category,Vendor,CartOrder,CartOrderItem,Wishlist,ProductImages,ProductReview,Address )
# Register your models here.


class ProductImagesAdmin(admin.TabularInline):

    model = ProductImages


admin.site.register(ProductImages,ProductImagesAdmin)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    inlines = [ProductImagesAdmin]
    list_display =[

        'user','title','product_image','price','featured','product_status'
    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['title','category_image']


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):

    list_display =[

        'user','title','vendor_image','contact',
    ]

@admin.register(CartOrder)
class CartOrderAdmin(admin.ModelAdmin):

    list_display = [

        'user','price','paid_status','order_date','product_status'
    ]


@admin.register(CartOrderItem)
class CartOrderItemsAdmin(admin.ModelAdmin):

    list_display = [

        'order','invoice_no','item','image','qty','price','total'
    ]


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    
    list_display = [

        'user','product','review','rating'
    ]


class WishlistAdmin(admin.ModelAdmin):

    list_display = [

        'user','product','date'
    ]

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):

    list_display = [

        'user','address','status'
    ]