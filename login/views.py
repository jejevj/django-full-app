# di dalam file views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import *

#@csrf_exempt
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Validasi username dan password
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('dashboard')
            else:
                # Return an 'invalid login' error message.
                error_message = 'Invalid login credentials'
        else:
            # Return an 'invalid form submission' error message.
            error_message = 'Invalid form submission. Please provide both username and password.'
    else:
        # Form pertama kali diakses (GET request)
        error_message = None

    return render(request, 'masuk.html', {'error_message': error_message})


def custom_logout(request):
    logout(request)
    # Redirect to the home page or any other page you prefer
    return redirect('oks')
