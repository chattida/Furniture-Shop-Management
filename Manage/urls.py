from django.urls import path

from . import views

urlpatterns = [
    path('customer/', views.manage_customer, name='manage_customer'),
    path('customer/add/', views.add_customer, name='add_customer'),
    path('supplier/', views.manage_supplier, name='manage_supplier'),
    path('supplier/add/', views.add_supplier, name='add_supplier')
]
