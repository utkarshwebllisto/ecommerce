from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from shop.serializers import (ProductSerializers,
                              ProductlistSerializers,
                              ProductCreateSerializers,
                              UpdateSerializers,
                              UserProductSerializers
                             # ProductDetailSerializers,
                              
                              #AddcartSerializers,
                              #OrderSerializers,
                             )
from .models import(Product,
	                   Addcart,
	                   Order
                     )	
from django.views.decorators.csrf import csrf_exempt
from rest_framework import renderers
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from shop.permission import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from django.contrib.auth.decorators import login_required
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class ProductList(APIView):
   def get(self, request, format=None):
        product = Product.objects.filter(owner=request.user)
        serializer = ProductSerializers(product, many=True)
        return Response(serializer.data)

class UserProduct(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = UserProductSerializers

    def get(self, request):
      serializer = self.serializer_class(data=self.queryset.all(), many=True)
      serializer.is_valid()
      data = []
      for product in self.queryset.all():
        data.append({
          "id": product.id,
          "pname":product.pname,
          "user":{'owner_id':product.owner.id,
                  'owner_email':product.owner.email,
                  'owner_name': product.owner.username,
                 } 


          })
      return Response(data)


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductlistSerializers


class ProductDelete(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class= ProductlistSerializers


class ProductCreate(generics.CreateAPIView):
     queryset = Product.objects.all()
     serializer_class= ProductCreateSerializers
     
     def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductUpdate(generics.RetrieveUpdateAPIView):
      queryset = Product.objects.all()
      serializer_class= UpdateSerializers

      def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



@login_required
def homepage(request):
	return render(request, 'index.html')




    





#{% url 'some-url-name' v1 v2 %}