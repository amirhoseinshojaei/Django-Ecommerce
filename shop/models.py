from django.db import models
from shortuuidfield import ShortUUIDField
from django.utils.html import mark_safe
from django.conf import settings
# Create your models here.


def user_directory_path(instance,filename):

    return 'user {0}/{1}'.format(instance,filename)

class Category(models.Model):

    cid = ShortUUIDField(unique = True , length = 10, max_length=20, prefix='cat',alphabet = "abcdefgh12345")
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    image = models.ImageField(upload_to='shop/category/')

    def category_image(self):

        return mark_safe('<img src="%s" width="50" height="50" />'%(self.image.url))
    
    def __str__(self):

        return self.title
    
class Vendor(models.Model):

    vid = ShortUUIDField(unique = True , lenght = 10, max_length=20, prefix='ven',alphabet="abcdefgh12345")
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
    


