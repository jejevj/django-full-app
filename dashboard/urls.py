from django.urls import path
from .views import *

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("driver/", user_list, name="driver"),
    path("customer/", customer_list, name="customer"),
    path("delivery/", delivery_list, name="delivery"),
    path("list-admin/", list_admin, name="list_admin"),
    path("tambah-admin/", tambah_admin, name="tambah_admin"),
    path("edit-admin/<int:admin_id>/", edit_admin, name="edit_admin"),
    path("hapus-admin/<int:admin_id>/", hapus_admin, name="hapus_admin"),
    path("tambah_user/", user_register, name="user_register"),
    path("tambah_customer/", customer_add, name="customer_add"),
    path("tambah_delivery/", delivery_add, name="delivery_add"),
    path("history/", history, name="history"),
    path("monitoring/<str:pk>", map, name="monitoring"),
    path("monitoring-list/", monitoring_list, name="monitoring1"),
    # API
    # path('api/drivers/', DriverListApiView.as_view(), name='driver-list-api'),
    path("api/driver/", UserDriverListCreateView.as_view(), name="driver-list-create"),
    path("api/driver/<int:pk>/", UserDriverDetailView.as_view(), name="driver-detail"),
    path(
        "api/driver-by-username/<str:username>/",
        UserDriverDetailView2.as_view(),
        name="driver-detail-username",
    ),
    path(
        "api/update-driver/<int:pk>/", DriverUpdateView.as_view(), name="driver-update"
    ),
    path(
        "api/customer/",
        UserCustomerListCreateView.as_view(),
        name="customer-list-create",
    ),
    path(
        "api/customer/<int:pk>/",
        UserCustomerDetailView.as_view(),
        name="customer-detail",
    ),
    path("api/delivery/", DeliveryListCreateView.as_view(), name="delivery-api"),
    path(
        "api/delivery-by-id/<str:pk>",
        DeliveryDetailView.as_view(),
        name="delivery-detail",
    ),
]
