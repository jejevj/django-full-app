from django.urls import path
from . import views
urlpatterns = [
    path('', views.custom_login, name='oks'),
    path('logout/', views.custom_logout, name='custom_logout'),
]
