from builtins import object

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from Manage.models import Customer, Supplier
from Account.models import Account, Employee, Owner

from Manage.forms import addCustomerForm, addSupplierForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse



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
    context = {'all_employee': []}
    employees = Employee.objects.all()
    for employee in employees:
        user = User.objects.get(id=employee.user_id)
        account = Account.objects.get(user_id=employee.user_id)
        info = {
            'id': employee.id,
            'fname': user.first_name,
            'lname': user.last_name,
            'email': user.email,
            'phone': account.phone,
            'department': employee.get_department_display
        }
        context['all_employee'].append(info)

    return render(request, template_name='Manage/manage_employee.html', context=context)

@login_required
def manage_customer(request):
    context = {'all_customer': []}
    customers = Customer.objects.all()
    for customer in customers:
        info = {
            'id': customer.id,
            'fname': customer.fname,
            'lname': customer.lname,
            'email': customer.email,
            'phone': customer.phone
        }
        context['all_customer'].append(info)

    return render(request, template_name='Manage/manage_customer.html', context=context)

@login_required
def manage_supplier(request):
    context = {'all_supplier': []}
    suppliers = Supplier.objects.all()
    for supplier in suppliers:
        info = {
            'id': supplier.id,
            'name': supplier.name,
            'address': supplier.address,
            'email': supplier.email,
            'phone': supplier.phone
        }
        context['all_supplier'].append(info)

    return render(request, template_name='Manage/manage_supplier.html', context=context)

@login_required
@csrf_exempt
def delete_employee_api(request, emp_id):
    if request.method == 'DELETE':
        employee = Employee.objects.get(id=emp_id)
        user = User.objects.get(id=employee.user_id)
        user.delete()
        return HttpResponse(status=200)
    return HttpResponse(status=405)

@login_required
@csrf_exempt
def delete_customer_api(request, cus_id):
    if request.method == 'DELETE':
        customer = Customer.objects.get(id=cus_id)
        customer.delete()
        return HttpResponse(status=200)
    return HttpResponse(status=405)

@login_required
@csrf_exempt
def delete_supplier_api(request, sup_id):
    if request.method == 'DELETE':
        supplier = Supplier.objects.get(id=sup_id)
        supplier.delete()
        return HttpResponse(status=200)
    return HttpResponse(status=405)