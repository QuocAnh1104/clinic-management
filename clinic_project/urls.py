from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from patient_portal import views as portal_views
from accounts import views as accounts_views

urlpatterns = [
    path('', portal_views.home, name='home'),
    path('dashboard/', accounts_views.dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('pharmacy/', include('pharmacy.urls')),
    path('reception/', include('reception.urls')),
    path('doctor/', include('doctor.urls')),
    path('cashier/', include('cashier.urls')),
    path('portal/', include('patient_portal.urls')),
]