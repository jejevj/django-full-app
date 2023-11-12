# dashboard/decorators.py
from django.shortcuts import redirect

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('oks')  # Redirect ke halaman login jika pengguna belum login
        return view_func(request, *args, **kwargs)

    return wrapper
