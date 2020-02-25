from rest_framework import serializers
from .models import Product,Addcart,Order
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
  station = serializers.RelatedField(read_only=True)
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
    class Meta:
        model=Product
        fields= "__all__"


class UpdateSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True,required=False)
    class Meta:
        model=Product
        fields= '__all__'


class UserProductSerializers(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields = ('id','pname','owner')
