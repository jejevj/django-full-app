from django.shortcuts import render,HttpResponse
from rest_framework import generics
from django.shortcuts import render, redirect
from .models import UserCustom
from .serializers import UserCustomSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def getUser(request):
    return HttpResponse('Fetch User Belum')

class UserCustomListCreateView(generics.ListCreateAPIView):
    queryset = UserCustom.objects.all()
    serializer_class = UserCustomSerializer
    
def home(request):
    return render(request, 'home.html')


# Login Berhasil
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = UserCustom.objects.filter(username=username).first()

        if user and user.check_password(password):
            # Password sesuai, lakukan login manual
            request.session['user_id'] = user.id
            # Redirect ke halaman setelah login berhasil
            return redirect('home')  # Ganti 'home' dengan nama URL halaman setelah login
        else:
            # Menampilkan pesan error jika login gagal
            error_message = "Invalid username or password."
    else:
        error_message = None

    return render(request, 'login.html', {'error_message': error_message})


# Register User
def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Validasi bahwa username belum digunakan
        if UserCustom.objects.filter(username=username).exists():
            error_message = "Username already exists."
        else:
            # Buat objek UserCustom dan simpan ke database
            user = UserCustom(username=username, email=email, password=password)
            user.save()
            # Redirect ke halaman setelah pendaftaran berhasil
            return redirect('login')  # Ganti 'login' dengan nama URL halaman login
    else:
        error_message = None

    return render(request, 'register.html', {'error_message': error_message})


# API USER
## USER LOGIN API

class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = UserCustom.objects.filter(username=username).first()

        if user and user.check_password(password):
            # Password sesuai, kirim response sukses
            serializer = UserCustomSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Kirim response gagal
            return Response({'error': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)
        
class UserRegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        # Validasi bahwa username belum digunakan
        if UserCustom.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        # Buat objek UserCustom dan simpan ke database
        user = UserCustom(username=username, email=email, password=password, level="user")
        user.save()

        serializer = UserCustomSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
