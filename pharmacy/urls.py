from django.urls import path
from . import views

app_name = 'pharmacy'

urlpatterns = [
    path('', views.medicine_list, name='medicine_list'),
    path('create/', views.medicine_create, name='medicine_create'),
    path('<int:pk>/edit/', views.medicine_update, name='medicine_update'),
    path('<int:pk>/stock-in/', views.medicine_stock_in, name='medicine_stock_in'),
    path('<int:pk>/delete/', views.medicine_delete, name='medicine_delete'),
]