from django.urls import include, path
from django.contrib import admin
from shop import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([  
    #path('', views.api_root), 
    path('', views.homepage),
    path('productlist/', views.ProductList.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('productlist/<int:pk>', views.ProductDetail.as_view()),    
    path('productlist/<int:pk>/destroy', views.ProductDelete.as_view()),
    path('create/', views.ProductCreate.as_view())
    ])
    #path('create/', views.ProductCreate)])
   # handler400 = 'project.error_handlers.bad_request'

   	# path('Product/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),
    # # path('ProductDetail/',views.ProductDetail.as_view()),
    # path('ProductDetail/<int:pk>',views.ProductDetail.as_view()),
    # path('cart/<int:pk>',views.cart, name='cart')
  #  path('Product/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),

    # path('Addcart/', views.AddcartList.as_view(), name='cart-list'),
    # path('Addcart/<int:pk>/', views.AddcartDetail.as_view(),name='cart-detail'),

 
    # path('Order/', views.OrderList.as_view(), name='order-list'),
    # path('Order/<int:pk>/', views.OrderDetail.as_view(),name='order-detail'),

    # path('User/', views.UserList.as_view(),name='user-list'),
    # path('User/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

    # path('User/<int:pk>/',user_set, name='UserViewSet'),
#return response(status=rest_framework.exceptions.bad_request)