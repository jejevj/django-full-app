
from django.shortcuts import render, redirect
from dashboard.decorators import login_required
from .models import UserDriver

from rest_framework import generics
from .serializers import DriverSerializer

@login_required
def dashboard(request):
    # Logika tampilan dashboard
    return render(request, 'dashboard.html')

@login_required
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

def user_list(request):
    users = UserDriver.objects.all()
    return render(request, 'driver.html', {'users': users})

# views.py

class DriverListApiView(generics.ListAPIView):
    queryset = UserDriver.objects.all()
    serializer_class = DriverSerializer
