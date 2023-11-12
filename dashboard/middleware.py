# dashboard/middleware.py
from django.shortcuts import redirect

class DashboardMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path.startswith('dashboard/'):
            return redirect('oks')  # Redirect ke halaman login jika pengguna belum login
        return self.get_response(request)
