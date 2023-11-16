from django.urls import path
from .views import *
urlpatterns = [
    
    path('', dashboard, name='dashboard'),
    path('driver/', user_list, name='driver'),
    path('customer/', customer_list, name='customer'),
    path('tambah_user/', user_register, name='user_register'),
    path('tambah_customer/', customer_add, name='customer_add'),
    path('tambah_delivery/', delivery_add, name='delivery_add'),
    
    # API
    # path('api/drivers/', DriverListApiView.as_view(), name='driver-list-api'),
    path('api/driver/', UserDriverListCreateView.as_view(), name='driver-list-create'),
    path('api/driver/<int:pk>/', UserDriverDetailView.as_view(), name='driver-detail'),
    path('api/customer/', UserCustomerListCreateView.as_view(), name='customer-list-create'),
    path('api/customer/<int:pk>/', UserCustomerDetailView.as_view(), name='customer-detail'),
]
