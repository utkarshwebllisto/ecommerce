from rest_framework import serializers
from .models import Product,Addcart,Order
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
    #product = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    product = serializers.HyperlinkedRelatedField(many=True, view_name='ProductList', read_only=True)
    class Meta:
        model = User
        fields ='__all__'


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = ['id','pname']


class ProductlistSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=Product
        fields= "__all__"


class ProductCreateSerializers(serializers.ModelSerializer):
   # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=Product
        fields= "__all__"



# class AddcartSerializers(serializers.ModelSerializer):
#     class Meta:
#         model=Addcart
#         fields = '__all__'



# class OrderSerializers(serializers.ModelSerializer):
#     class Meta:
#         model=Order
#         fields = '__all__'
