from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.dashboard, name='dashboard'),
    path('driver/', views.user_list, name='driver'),
    path('customer/', views.customer_list, name='customer'),
    path('tambah_user/', views.user_register, name='user_register'),
    path('tambah_customer/', views.customer_add, name='customer_add'),
    
    # API
    path('api/drivers/', views.DriverListApiView.as_view(), name='driver-list-api'),
]
