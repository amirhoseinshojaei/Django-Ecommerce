from django.contrib import admin
from .models import (Product,Category,Vendor,CartOrder,CartOrderItem,Wishlist,ProductImages,ProductReview,Address )
# Register your models here.


class ProductImagesAdmin(admin.TabularInline):

    model = ProductImages
