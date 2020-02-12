from django.urls import include, path
from django.contrib import admin
from shop import views
from rest_framework.urlpatterns import format_suffix_patterns
user_set = views.UserViewSet.as_view({
    'get': 'list'
})
urlpatterns = format_suffix_patterns([  
    path('', views.api_root),

    path('Product/', views.ProductList.as_view(), name='product-list'),
    path('Product/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),

    path('Addcart/', views.AddcartList.as_view(), name='cart-list'),
    path('Addcart/<int:pk>/', views.AddcartDetail.as_view(),name='cart-detail'),

 
    path('Order/', views.OrderList.as_view(), name='order-list'),
    path('Order/<int:pk>/', views.OrderDetail.as_view(),name='order-detail'),

    path('User/', views.UserList.as_view(),name='user-list'),
    path('User/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

    path('User/<int:pk>/',user_set, name='UserViewSet'),
])