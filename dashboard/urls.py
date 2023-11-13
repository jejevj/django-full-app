from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('driver/', views.user_list, name='driver'),
    path('tambah_user/', views.user_register, name='user_register'),
    
    # API
    path('api/drivers/', views.DriverListApiView.as_view(), name='driver-list-api'),
]
