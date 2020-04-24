from django.urls import path

from . import views

urlpatterns = [
    path('customer/', views.manage_customer, name='manage_customer'),
    path('customer/add/', views.add_customer, name='add_customer'),
    path('supplier/', views.manage_supplier, name='manage_supplier'),
    path('supplier/add/', views.add_supplier, name='add_supplier'),
    path('employee/', views.manage_employee, name='manage_employee'),
    path('item/add/', views.add_item, name='add_item'),
    path('item/', views.manage_item, name='manage_item'),
    path('employee/api/delete/<int:emp_id>/', views.delete_employee_api, name='delete_employee_api'),
    path('customer/api/delete/<int:cus_id>/', views.delete_customer_api, name='delete_customer_api'),
    path('supplier/api/delete/<int:sup_id>/', views.delete_supplier_api, name='delete_supplier_api'),
    path('item/api/delete/<int:item_id>/', views.delete_item_api, name='delete_item_api')
]
