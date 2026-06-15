from django.shortcuts import redirect
from django.urls import reverse, NoReverseMatch


class ForcePasswordChangeMiddleware:
    """
    Middleware ép user đổi mật khẩu nếu must_change_password=True.
    Chặn truy cập mọi trang trừ trang đổi mật khẩu và logout.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Chỉ áp dụng cho user đã đăng nhập và có flag must_change_password
        if request.user.is_authenticated and getattr(request.user, 'must_change_password', False):
            # Các URL được phép truy cập kể cả khi chưa đổi mật khẩu
            try:
                allowed_paths = [
                    reverse('patient_portal:change_password'),
                    reverse('logout'),
                ]
            except NoReverseMatch:
                allowed_paths = ['/logout/']

            # Cho phép truy cập file static (CSS, JS, ảnh)
            if request.path.startswith('/static/') or request.path.startswith('/media/'):
                return self.get_response(request)

            # Nếu không phải URL được phép, redirect về trang đổi mật khẩu
            if request.path not in allowed_paths:
                return redirect('patient_portal:change_password')

        return self.get_response(request)