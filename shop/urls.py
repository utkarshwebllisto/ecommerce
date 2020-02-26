from django.urls import include, path
from django.contrib import admin
from shop import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([  
    path('', views.homepage),
    path('productlist/', views.ProductList.as_view(), name='productlist'),
    path('Costumer/', views.Costumer.as_view(), name='Costumer'),
    path('User/',views.UserProduct.as_view()),
    path('User/<int:pk>',views.UserProduct.as_view(), name='UserProduct'),
    path('api-auth/', include('rest_framework.urls')),
    path('productlist/<int:pk>', views.ProductDetail.as_view(), name='productlist_id'),    
    path('productlist/<int:pk>/destroy', views.ProductDelete.as_view(),name='productlist_destroy'),
    path('create/', views.ProductCreate.as_view(), name='create'),
    path('update/<int:pk>', views.ProductUpdate.as_view(), name='update')
    
    ])
    