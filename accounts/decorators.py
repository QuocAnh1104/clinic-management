from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages


def role_required(*allowed_roles):
    """
    Decorator chặn user truy cập view nếu role không thuộc danh sách cho phép.
    Cách dùng: @role_required('PHARMACIST', 'ADMIN')
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            if request.user.role not in allowed_roles:
                messages.error(request, 'Bạn không có quyền truy cập chức năng này.')
                return redirect('home')
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator