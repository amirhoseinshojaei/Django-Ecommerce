from django.urls import path
from . import views

app_name = 'shop'


urlpatterns=[

    path("",views.index,name='home'),
    path("products/",views.product_list_view,name='product_list'),
]