from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from dashboard.decorators import login_required
from .models import UserDriver, UserCustomer, Delivery
from django.contrib.auth.models import User

from rest_framework import generics
from .serializers import *
from django.views.decorators.csrf import *


#@login_required
#@csrf_exempt
def dashboard(request):
    # Logika tampilan dashboard
    return render(request, "dashboard.html")


#@csrf_exempt
def list_admin(request):
    admins = User.objects.all()
    return render(request, "list_admin.html", {"admins": admins})


#@csrf_exempt
def tambah_admin(request):
    if request.method == "POST":
        # Ambil data formulir dari request.POST
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        # Periksa apakah username dan password tidak kosong
        if username and password:
            # Buat objek User dan simpan ke database
            user = User.objects.create_user(
                username=username, password=password, email=email
            )
            redirect_url = '/popup/?message=Successfully%20added%20admin&status=success&redirect_url=list-admin'
            return redirect(redirect_url)
        else:
            return HttpResponse("Username and password cannot be empty.")
    else:
        return render(request, "tambah_admin.html")


#@csrf_exempt
def edit_admin(request, admin_id):
    admin = get_object_or_404(User, pk=admin_id)

    if request.method == "POST":
        # Ambil data formulir dari request.POST
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        # Periksa apakah username dan password tidak kosong
        if username and password:
            # Perbarui data admin dan simpan ke database
            admin.username = username
            admin.email = email
            admin.set_password(password)
            admin.save()

            redirect_url = '/popup/?message=Successfully%20edited%20admin&status=success&redirect_url=list-admin'
            return redirect(redirect_url)
        else:
            return HttpResponse("Username and password cannot be empty.")
    else:
        return render(request, "edit_admin.html", {"admin": admin})


#@csrf_exempt
def hapus_admin(request, admin_id):
    admin = get_object_or_404(User, pk=admin_id)

    if request.method == "POST":
        confirmation = request.POST.get("confirmation", "").lower()

        if confirmation == "ya":
            # Hapus data admin dari database
            admin.delete()
            redirect_url = '/popup/?message=Successfully%20deleted%20admin&status=success&redirect_url=list-admin'
            return redirect(redirect_url)
        else:
            return HttpResponse(
                "Data Deletion Cancelled."
            )  # Berikan respon jika konfirmasi tidak sesuai
    else:
        return render(request, "hapus_admin.html", {"admin": admin})


#@csrf_exempt
def user_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        hp = request.POST.get("hp")
        photo = request.FILES.get("photo")

        # Validasi bahwa username belum digunakan
        if UserDriver.objects.filter(username=username).exists():
            error_message = "Username already exists."
        else:
            # Buat objek UserCustom dan simpan ke database
            user = UserDriver(
                username=username, email=email, password=password, hp=hp, photo=photo
            )
            user.save()

            # Redirect ke halaman setelah pendaftaran berhasil
            redirect_url = '/popup/?message=Successfully%20added%20data&status=success&redirect_url=driver'
            return redirect(redirect_url)
    else:
        error_message = None

    return render(request, "add_driver.html", {"error_message": error_message})

#@csrf_exempt
def edit_customer(request, customer_id):
    customer = get_object_or_404(UserCustomer, pk=customer_id)

    if request.method == "POST":
        # Ambil data formulir dari request.POST
        customer_name = request.POST.get("customer_name")
        address = request.POST.get("address")
        cp = request.POST.get("cp")
        hp = request.POST.get("hp")

        # Periksa apakah field utama tidak kosong
        if customer_name and address and cp and hp:
            # Perbarui data customer dan simpan ke database
            customer.customer_name = customer_name
            customer.address = address
            customer.cp = cp
            customer.hp = hp
            customer.save()

            # Jika ingin melakukan pengalihan dengan membawa tiga variabel dalam query string
            redirect_url = '/popup/?message=Successfully%20edited%20&status=success&redirect_url=customer'
            return redirect(redirect_url)
        else:
            return HttpResponse("Main Field cannot be empty.")
    else:
        return render(request, "edit_customer.html", {"customer": customer})
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

#@csrf_exempt
def hapus_customer(request, customer_id):
    customer = get_object_or_404(UserCustomer, pk=customer_id)

    if request.method == "POST":
        confirmation = request.POST.get("confirmation", "").lower()

        if confirmation == "ya":
            # Hapus data customer dari database
            customer.delete()
 # Jika ingin melakukan pengalihan dengan membawa tiga variabel dalam query string
            redirect_url = '/popup/?message=Data%20successfully%20deleted&status=success&redirect_url=customer'
            return redirect(redirect_url)
        else:
            return HttpResponse(
                "Data Deletion Cancelled."
            )  # Berikan respon jika konfirmasi tidak sesuai
    else:
        return render(request, "hapus_customer.html", {"customer": customer})

#@csrf_exempt
def hapus_driver(request, driver_id):
    driver = get_object_or_404(UserDriver, pk=driver_id)

    if request.method == "POST":
        confirmation = request.POST.get("confirmation", "").lower()

        if confirmation == "ya":
            # Hapus data admin dari database
            driver.delete()
 # Jika ingin melakukan pengalihan dengan membawa tiga variabel dalam query string
            redirect_url = '/popup/?message=Data%20successfully%20deleted&status=success&redirect_url=driver'

            return redirect(redirect_url)
        else:
            return HttpResponse(
                "Driver Deletion Cancelled."
            )  # Berikan respon jika konfirmasi tidak sesuai
    else:
        return render(request, "hapus_driver.html", {"driver": driver})


#@csrf_exempt
def edit_driver(request, driver_id):
    driver = get_object_or_404(UserDriver, pk=driver_id)

    if request.method == "POST":
        # Ambil data formulir dari request.POST
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        # Periksa apakah username dan password tidak kosong
        if username and password:
            # Perbarui data pengemudi dan simpan ke database
            driver.username = username
            driver.email = email
            driver.password = password  # Gunakan set_password untuk menyimpan kata sandi terenkripsi
            driver.save()
 # Jika ingin melakukan pengalihan dengan membawa tiga variabel dalam query string
            redirect_url = '/popup/?message=Successfully%20edited%20&status=success&redirect_url=driver'
            return redirect(redirect_url)
        else:
            return HttpResponse("Username and password cannot be empty.")
    else:
        return render(request, "edit_driver.html", {"driver": driver})


#@csrf_exempt
def user_list(request):
    users = UserDriver.objects.all()
    return render(request, "driver.html", {"users": users})


# views.py


#@csrf_exempt
def customer_add(request):
    if request.method == "POST":
        customer_name = request.POST.get("customer_name")
        address = request.POST.get("address")
        cp = request.POST.get("cp")
        hp = request.POST.get("hp")
        lat = request.POST.get("lat")
        lon = request.POST.get("lon")
        photo = request.FILES.get("photo")

        # Validasi bahwa username belum digunakan
        if UserCustomer.objects.filter(customer_name=customer_name).exists():
            error_message = "Nama Customer Sudah Ada."
        else:
            # Buat objek UserCustom dan simpan ke database
            user = UserCustomer(
                customer_name=customer_name,
                address=address,
                cp=cp,
                hp=hp,
                photo=photo,
                lat=lat,
                lon=lon,
            )
            user.save()

            # Redirect ke halaman setelah pendaftaran berhasil
            redirect_url = '/popup/?message=Successfully%20added%20customer&status=success&redirect_url=customer'
            return redirect(redirect_url)
    else:
        error_message = None

    return render(request, "add_customer.html", {"error_message": error_message})


#@csrf_exempt
def delivery_add(request):
    if request.method == "POST":
        no_delivery = request.POST.get("no_delivery")
        date = request.POST.get("date")
        customer_name = request.POST.get("customer_name2")
        address = request.POST.get("address")
        cust_lat = request.POST.get("cust_lat")
        cust_lon = request.POST.get("cust_lon")
        cp = request.POST.get("cp")
        hp = request.POST.get("hp")
        driver_name = request.POST.get("driver_name2")
        photo = request.FILES.get("photo")

        # Validasi bahwa username belum digunakan
        if Delivery.objects.filter(no_delivery=no_delivery).exists():
            error_message = "Delivery Number Must Be Unique."
        else:
            # Buat objek UserCustom dan simpan ke database
            user = Delivery(
                no_delivery=no_delivery,
                customer_name=customer_name,
                cust_lat=cust_lat,
                cust_lon=cust_lon,
                address=address,
                date=date,
                cp=cp,
                hp=hp,
                driver_name=driver_name,
                photo=photo,
            )
            user.save()
            # Redirect ke halaman setelah pendaftaran berhasil
            redirect_url = '/popup/?message=Successfully%20added%20delivery&status=success&redirect_url=delivery'
            return redirect(redirect_url)
    else:
        error_message = None

    return render(request, "add_delivery.html", {"error_message": error_message})

#@csrf_exempt
def hapus_delivery(request, no_delivery):
    delivery = get_object_or_404(Delivery, pk=no_delivery)

    if request.method == "POST":
        confirmation = request.POST.get("confirmation", "").lower()

        if confirmation == "ya":
            # Hapus data pengiriman dari database
            delivery.delete() # Redirect ke halaman setelah pendaftaran berhasil
            redirect_url = '/popup/?message=Successfully%20deleted%20delivery&status=success&redirect_url=delivery'
            return redirect(redirect_url)
        else:
            return HttpResponse(
                "Delivery Deletion Cancelled."
            )  # Berikan respon jika konfirmasi tidak sesuai
    else:
        return render(request, "hapus_delivery.html", {"delivery": delivery})
    
#@csrf_exempt
def customer_list(request):
    users = UserCustomer.objects.all()
    return render(request, "customer.html", {"users": users})


#@csrf_exempt
def delivery_list(request):
    items = Delivery.objects.all()
    return render(request, "delivery.html", {"items": items})


#@csrf_exempt
def monitoring_list(request):
    items = Delivery.objects.filter(status="Pickup")

    return render(request, "monitoring.html", {"items": items})


#@csrf_exempt
def history(request):
    items = Delivery.objects.all()
    return render(request, "history.html", {"items": items})


#@csrf_exempt
def map(request, pk):
    items = Delivery.objects.get(pk=pk)
    return render(request, "map.html", {"items": items})

def popup(request):
    message = request.GET.get('message', '')
    status = request.GET.get('status', '')
    redirect_url = request.GET.get('redirect_url', '')
    context = {
        'message': message,
        'status': status,
        'redirect_url': redirect_url,
    }

    return render(request, 'popup.html', context)

# API


class DriverListApiView(generics.ListAPIView):
    queryset = UserDriver.objects.all()
    serializer_class = DriverSerializer


# DRIVER API
class UserDriverListCreateView(generics.ListCreateAPIView):
    queryset = UserDriver.objects.all()
    serializer_class = UserDriverSerializer


class UserDriverDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserDriver.objects.all()
    serializer_class = UserDriverSerializer


class UserDriverDetailView2(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDriverSerializer
    lookup_field = "username"

    def get_queryset(self):
        username = self.kwargs["username"]
        return UserDriver.objects.filter(username=username)


# CUSTOMER API
class UserCustomerListCreateView(generics.ListCreateAPIView):
    queryset = UserCustomer.objects.all()
    serializer_class = UserCustomerSerializer


class UserCustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserCustomer.objects.all()
    serializer_class = UserCustomerSerializer


# DELIVERY API
class DeliveryListCreateView(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliveryCustomerSerializer


class DeliveryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliveryCustomerSerializer
