from rest_framework import serializers
from .models import Product,Addcart,Order
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
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


class UpdateSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True,required=False)
    class Meta:
        model=Product
        fields= '__all__'

class UserProductSerializers(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner')
        owner = {'owner_id':owner.id,'owner_name':owner.first_name}
        model=Product
        fields = ['id','pname','owner']


