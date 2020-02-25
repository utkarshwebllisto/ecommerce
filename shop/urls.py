from django.urls import include, path
from django.contrib import admin
from shop import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([  
    path('', views.homepage),
    path('productlist/', views.ProductList.as_view()),
    path('User/',views.UserProduct.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('productlist/<int:pk>', views.ProductDetail.as_view()),    
    path('productlist/<int:pk>/destroy', views.ProductDelete.as_view()),
    path('create/', views.ProductCreate.as_view()),
    path('update/<int:pk>', views.ProductUpdate.as_view())
    
    ])
    