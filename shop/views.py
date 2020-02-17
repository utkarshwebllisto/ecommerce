from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from shop.serializers import (ProductSerializers,
                              AddcartSerializers,
                              OrderSerializers,
                              UserSerializers)
from shop.models import(Product,
	                    Addcart,
	                    Order)	
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

class ProductList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]#,IsOwnerOrReadOnly]


    def get(self, request):
        product = Product.objects.all()
        serialized = ProductSerializers(product, many=True)
        return Response(serialized.data)
        #return self.list(request, *args, **kwargs)

   
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    def perform_create(self, serializer):
    	serializer.save(owner=self.request.user)

# class ProductDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

   
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

   
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


class UserList(APIView):
	
	def get(self, request, format= None):
		queryset = User.objects.all()
		serializer= UserSerializers(queryset, many=True)
		return Response(serializer.data)


def homepage(request):
	return render(request, 'index.html')


class ProductDetail(APIView):
	def get(self, request, pk, format=None):
		product = Product.objects.get(pk=pk)
		serializer = ProductSerializers(product)
		return Response(serializer.data)


# def cart(request,pk,format=None):
# 	product = Product.objects.get(pk=pk)
# 	product = product.id
	
# #	print(product)
# 	return render(request, 'cart.html', {'product':product})



    





@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format),
        # 'carts': reverse('cart-list', request=request, format=format),
        # 'orders': reverse('order-list', request=request, format=format)
    
    })
