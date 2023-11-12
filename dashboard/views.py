from django.shortcuts import render

from dashboard.decorators import login_required

@login_required
def dashboard(request):
    # Logika tampilan dashboard
    return render(request, 'dashboard.html')
