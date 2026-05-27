from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


@login_required
def dashboard(request):
    """Trang chủ sau khi đăng nhập — điều hướng theo role."""
    role = request.user.role
    if role == 'ADMIN':
        return redirect('/admin/')
    elif role == 'PHARMACIST':
        return redirect('/pharmacy/')
    elif role == 'RECEPTIONIST':
        return redirect('/reception/')
    elif role == 'DOCTOR':
        return redirect('/doctor/')
    else:
        return render(request, 'dashboard.html')
