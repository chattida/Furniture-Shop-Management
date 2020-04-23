from django.urls import path

from . import views

urlpatterns = [
    path('supplier/', views.view_supplier, name='view_supplier')
]
