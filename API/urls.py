from django.urls import path

from . import views

urlpatterns = [
    path('supplier/', views.api_supplier.as_view(),
         name='api_supplier'),
    path('view_stock/', views.api_view_stock.as_view(),
         name='api_view_stock')
]
