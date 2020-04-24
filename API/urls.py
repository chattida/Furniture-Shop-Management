from django.urls import path

from . import views

urlpatterns = [
    path('view_supplier/', views.api_view_supplier.as_view(),
         name='api_view_supplier'),
    path('view_stock/', views.api_view_stock.as_view(),
         name='api_view_stock')
]
