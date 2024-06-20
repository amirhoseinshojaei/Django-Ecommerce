from django.db import models
from shortuuidfield import ShortUUIDField
from django.utils.html import mark_safe
from django.conf import settings
from taggit.managers import TaggableManager
# Create your models here.



STATUS_CHOICE = [
    
    ('process','Processing'),
    ('shipped','Shipped'),
    ('delivered','Delivered'),
    ('process','Processing'),
    ('process','Processing'),
]



STATUS = [

    ('draft','Draft'),
    ('disabled','Disabled'),
    ('rjected','Regected'),
    ('in_review','In Review'),
    ('published','Published'),
]




RATING = [

    (1,'⭐☆☆☆☆'),
    (2,'⭐⭐☆☆☆'),
    (3,'⭐⭐⭐☆☆'),
    (4,'⭐⭐⭐⭐☆'),
    (5,'⭐⭐⭐⭐⭐')
]


def user_directory_path(instance,filename):

    return 'user {0}/{1}'.format(instance,filename)

class Category(models.Model):

    cid = ShortUUIDField(unique = True , max_length=20)
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    image = models.ImageField(upload_to='shop/category/')

    def category_image(self):

        return mark_safe('<img src="%s" width="50" height="50" />'%(self.image.url))
    
    def __str__(self):

        return self.title
    
class Vendor(models.Model):

    vid = ShortUUIDField(unique = True , max_length=20)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to=user_directory_path)
    description = models.TextField(null=True,blank=True)
    address= models.TextField(max_length=250,default="123 Main Street")
    contact = models.CharField(max_length=15,default="+123 (456) 400")
    chat_resp_time = models.CharField(max_length=100, default="100s")
    shipping_on_time = models.CharField(max_length=100,default="100s")
    authentic_rating= models.CharField(max_length=100,default="100")
    days_return = models.CharField(max_length=100,default="100")
    warranty_period = models.CharField(max_length=100,default=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)

    class Meta:
        verbose_name_plural = 'vendors'

    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />'%(self.image.url))


    def __str__(self):
        return self.title
    


class Product(models.Model):

    pid = ShortUUIDField(unique = True, max_length=20)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name='category')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    vendor = models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True,related_name='products')

    title = models.CharField(max_length=100,default="Fresh Pear")
    image = models.ImageField(upload_to=user_directory_path,default="product.jpg")
    description = models.TextField(null=True,blank=True,default="this is a product")

    price = models.DecimalField(max_digits=10,decimal_places=2,default="1.99")
    old_price = models.DecimalField(max_digits=10,decimal_places=2,default="2.99")

    specification = models.TextField(null=True,blank=True)
    tags = TaggableManager()
    product_status = models.CharField(choices=STATUS,max_length=20,default="in_review")

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)

    sku = ShortUUIDField(unique=True,max_length = 20)

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name_plural = 'Products'

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />'%(self.image.url))
    

    def get_precentage(self):

        new_price = (self.price / self.old_price)*100
        return new_price
    
    def __str__(self):

        return self.title
    


class ProductImages(models.Model):

    images = models.ImageField(upload_to="product-images",default="product.jpg")
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,related_name="p_images")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name_plural="Product Images"

    


class CartOrder(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE,max_length=30,default='processing')

    class Meta:

        verbose_name_plural = "Cart Orders"



class CartOrderItem(models.Model):

   order = models.ForeignKey(CartOrder,on_delete=models.CASCADE)
   invoice_no = models.CharField(max_length=200)
   item = models.CharField(max_length=200)
   image = models.CharField(max_length=200)
   qty = models.IntegerField(default=0)
   price = models.DecimalField(max_digits=10,decimal_places=2)
   total = models.DecimalField(max_digits=10,decimal_places=2)

   class Meta:
       
       verbose_name_plural = 'Cart Order Items'



class ProductReview(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    review = models.TextField()

    rating = models.IntegerField(choices=RATING,default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name_plural = 'Product Reviews'

    def __str__(self):

        return self.product.title
    
    def get_rating(self):

        return self.rating



class Wishlist(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name_plural = "Wishlists"

    def __str__(self):

        return self.product.title
    


class Address(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    address = models.CharField(max_length=100,null=True)
    status = models.BooleanField(default=False) 

    class Meta:

        verbose_name_plural = "Address" 