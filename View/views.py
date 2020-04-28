from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('Manage.view_supplier')
def view_supplier(request):
    return render(request, template_name='View/view_supplier.html')


@login_required
@permission_required('Manage.view_stock')
def view_stock(request):
    return render(request, template_name='View/view_stock.html')


@login_required
@permission_required('Manage.view_order')
def view_history(request):
    return render(request, template_name='View/view_history.html')
