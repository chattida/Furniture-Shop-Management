from builtins import object

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from Manage.models import Customer, Supplier
from Manage.forms import addCustomerForm, addSupplierForm


# Create your views here.


@login_required
def manage_customer(request):
    return render(request, template_name='Manage/manage_customer.html')


@login_required
def add_customer(request):
    context = {}
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        employee_id = request.user.id
        employee = User.objects.get(pk=employee_id)
        form = addCustomerForm(request.POST)
        if form.is_valid():
            customer = Customer.objects.create(
                fname=fname,
                lname=lname,
                email=email,
                phone=phone,
                address=address,
                account_id=employee
            )
            return redirect('manage_customer')
        else:
            context['form'] = form

    elif request.method == 'GET':
        form = addCustomerForm()
        context['form'] = form

    return render(request, template_name='Add/add_customer.html', context=context)

@login_required
def manage_supplier(request):
    return render(request, template_name='Manage/manage_supplier.html')


@login_required
def add_supplier(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        employee_id = request.user.id
        employee = User.objects.get(pk=employee_id)
        form = addSupplierForm(request.POST)
        if form.is_valid():
            supplier = Supplier.objects.create(
                name=name,
                email=email,
                phone=phone,
                address=address,
                account_id=employee
            )
            return redirect('manage_supplier')
        else:
            context['form'] = form

    elif request.method == 'GET':
        form = addSupplierForm()
        context['form'] = form

    return render(request, template_name='Add/add_supplier.html', context={'form': form})

@login_required
def manage_employee(request):
    return render(request, template_name='Manage/manage_employee.html')