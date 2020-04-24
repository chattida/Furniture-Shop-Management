from django.urls import path

from . import views

urlpatterns = [
    path('supplier/', views.api_supplier.as_view(),
         name='api_supplier'),
    path('stock/', views.api_stock.as_view(),
         name='api_stock'),
    path('employee/', views.api_employee.as_view(),
         name='api_employee'),
    path('customer/', views.api_customer.as_view(),
         name='api_customer'),
    path('item/', views.api_item.as_view(),
         name='api_item')
]
