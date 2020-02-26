from rest_framework import serializers
from .models import Product,Costumer
from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator

class UserSerializers(serializers.ModelSerializer):
   class Meta:
        model = User
        fields =['id','username','email']


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



class CostumerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Costumer
        fields= "__all__"


class UpdateSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True,required=False)
    class Meta:
        model=Product
        fields= '__all__'


class UserProductSerializers(serializers.ModelSerializer):
    owner= UserSerializers()
    costumer = CostumerSerializers()
    class Meta:
       model =Product
       fields = ('id','pname','owner','costumer')