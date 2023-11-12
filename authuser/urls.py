from django.urls import path
from . import views

urlpatterns = [
    # API
    path('get-user',views.UserCustomListCreateView.as_view(),name='getuser'),
    path('api/login/', views.UserLoginAPIView.as_view(), name='api_user_login'),
    path('api/register/', views.UserRegisterAPIView.as_view(), name='api_user_register'),
    
    
    # Test Web
    path('home/',views.home,name='home'),
]
