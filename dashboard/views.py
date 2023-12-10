
from django.shortcuts import render, redirect
from dashboard.decorators import login_required
from .models import UserDriver, UserCustomer, Delivery

from rest_framework import generics
from .serializers import *
from django.views.decorators.csrf import *

@login_required
@csrf_exempt
def dashboard(request):
    # Logika tampilan dashboard
    return render(request, 'dashboard.html')

@csrf_exempt
def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        hp = request.POST.get('hp')
        photo = request.FILES.get('photo')

        # Validasi bahwa username belum digunakan
        if UserDriver.objects.filter(username=username).exists():
            error_message = "Username already exists."
        else:
            # Buat objek UserCustom dan simpan ke database
            user = UserDriver(username=username, email=email, password=password, hp=hp, photo=photo)
            user.save()

            # Redirect ke halaman setelah pendaftaran berhasil
            return redirect('driver')  # Ganti 'login' dengan nama URL halaman login
    else:
        error_message = None

    return render(request, 'add_driver.html', {'error_message': error_message})

@login_required 
@csrf_exempt
def user_list(request):
    users = UserDriver.objects.all()
    return render(request, 'driver.html', {'users': users})

# views.py


@csrf_exempt
def customer_add(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        address = request.POST.get('address')
        cp = request.POST.get('cp')
        hp = request.POST.get('hp')
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')
        photo = request.FILES.get('photo')

        # Validasi bahwa username belum digunakan
        if UserCustomer.objects.filter(customer_name=customer_name).exists():
            error_message = "Nama Customer Sudah Ada."
        else:
            # Buat objek UserCustom dan simpan ke database
            user = UserCustomer(customer_name=customer_name, address=address, cp=cp, hp=hp, photo=photo,lat=lat,lon=lon)
            user.save()

            # Redirect ke halaman setelah pendaftaran berhasil
            return redirect('customer')  # Ganti 'login' dengan nama URL halaman login
    else:
        error_message = None

    return render(request, 'add_customer.html', {'error_message': error_message})

@csrf_exempt
def delivery_add(request):
    if request.method == 'POST':
        no_delivery = request.POST.get('no_delivery')
        date = request.POST.get('date')
        customer_name = request.POST.get('customer_name2')
        address = request.POST.get('address')
        cust_lat = request.POST.get('cust_lat')
        cust_lon = request.POST.get('cust_lon')
        cp = request.POST.get('cp')
        hp = request.POST.get('hp')
        driver_name = request.POST.get('driver_name2')
        photo = request.FILES.get('photo')

        # Validasi bahwa username belum digunakan
        if Delivery.objects.filter(no_delivery=no_delivery).exists():
            error_message = "Nomor Delivery Tidak Boleh Sama"
        else:
            # Buat objek UserCustom dan simpan ke database
            user = Delivery(no_delivery=no_delivery,customer_name=customer_name,cust_lat=cust_lat,cust_lon=cust_lon, address=address, date=date, cp=cp, hp=hp,driver_name=driver_name, photo=photo)
            user.save()

            # Redirect ke halaman setelah pendaftaran berhasil
            return redirect('customer')  # Ganti 'login' dengan nama URL halaman login
    else:
        error_message = None

    return render(request, 'add_delivery.html', {'error_message': error_message})


@login_required
@csrf_exempt
def customer_list(request):
    users = UserCustomer.objects.all()
    return render(request, 'customer.html', {'users': users})

@csrf_exempt
def delivery_list(request):
    items = Delivery.objects.all()
    return render(request, 'delivery.html', {'items': items})


@login_required
@csrf_exempt
def monitoring_list(request):
    items = Delivery.objects.all()
    return render(request, 'monitoring.html', {'items': items})


@login_required
@csrf_exempt
def map(request,pk):
    items = Delivery.objects.get(pk=pk)
    return render(request, 'map.html',{'items':items})





# API

class DriverListApiView(generics.ListAPIView):
    queryset = UserDriver.objects.all()
    serializer_class = DriverSerializer
    
    
class UserDriverListCreateView(generics.ListCreateAPIView):
    queryset = UserDriver.objects.all()
    serializer_class = UserDriverSerializer

class UserDriverDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserDriver.objects.all()
    serializer_class = UserDriverSerializer

class UserCustomerListCreateView(generics.ListCreateAPIView):
    queryset = UserCustomer.objects.all()
    serializer_class = UserCustomerSerializer

class DeliveryListCreateView(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliveryCustomerSerializer

class UserCustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserCustomer.objects.all()
    serializer_class = UserCustomerSerializer
