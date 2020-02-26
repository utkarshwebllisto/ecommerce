from django.contrib.auth.models import User
from django.db import models


class Costumer(models.Model):
    c_name= models.CharField(max_length=100)
    c_age = models.IntegerField()
    c_address = models.CharField(max_length=100)

class Product(models.Model):
    pname = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='item_images')
    price = models.IntegerField()
    product_detail = models.TextField(blank=True, null=True)
    owner = models.ForeignKey('auth.User', null=True, blank=True, related_name='owner', on_delete=models.CASCADE)
    costumer = models.ForeignKey(Costumer,on_delete=models.CASCADE, blank=True, null=True)
   # owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE,blank=True, null=True)

class Addcart(models.Model):
    quantity = models.IntegerField(blank=True, null=True)
    pid = models.ForeignKey(Product, on_delete = models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.pid.pname


class Order(models.Model):
    quantity = models.IntegerField(default = 1)  
    owner = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
    grand_total = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    user_phone = models.CharField(max_length=20, blank=True, null=True)
    user_address = models.CharField(max_length=20, blank=True, null=True)
    cart = models.ForeignKey(Product, on_delete = models.CASCADE, blank=True, null=True) 

