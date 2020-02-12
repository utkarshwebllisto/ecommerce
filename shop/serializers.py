from rest_framework import serializers
from .models import Product,Addcart,Order
from django.contrib.auth.models import User

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = '__all__'



class AddcartSerializers(serializers.ModelSerializer):
    class Meta:
        model=Addcart
        fields = '__all__'



class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields = '__all__'



class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = '__all__'
