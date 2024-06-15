from django.urls import path
from . import views

app_name = 'shop'


urlpatterns=[

    path("",views.index,name='home'),
    path("products/",views.product_list_view,name='product_list'),
    path("category/",views.category_list_view,name='category'),
    path("category/<cid>/",views.category_product_list_view,name='category_product_list'),

    # Vendor
    path('vendors/',views.vendor_list_view,name='vendor_list'),
    path('vendor/<vid>/',views.vendor_detail_view,name='vendor_detail'),
]