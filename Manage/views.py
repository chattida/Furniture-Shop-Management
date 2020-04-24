from builtins import object

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from Manage.models import Customer, Supplier, Item, Stock
from Account.models import Account, Employee, Owner

from Manage.forms import addCustomerForm, addSupplierForm, addItemForm, addStockForm

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


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
            'phone': customer.phone,
            'address': customer.address
        }
        context['all_customer'].append(info)

    return render(request, template_name='Manage/manage_customer.html', context=context)


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
@csrf_exempt
def delete_customer_api(request, cus_id):
    if request.method == 'DELETE':
        customer = Customer.objects.get(id=cus_id)
        customer.delete()
        return HttpResponse(status=200)
    return HttpResponse(status=405)


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
def edit_supplier(request, id):
    context = {}
    context['id'] = id
    return render(request, template_name='Edit/edit_supplier.html', context=context)



@login_required
@csrf_exempt
def delete_supplier_api(request, sup_id):
    if request.method == 'DELETE':
        supplier = Supplier.objects.get(id=sup_id)
        supplier.delete()
        return HttpResponse(status=200)
    return HttpResponse(status=405)


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
@csrf_exempt
def delete_employee_api(request, emp_id):
    if request.method == 'DELETE':
        employee = Employee.objects.get(id=emp_id)
        user = User.objects.get(id=employee.user_id)
        user.delete()
        return HttpResponse(status=200)
    return HttpResponse(status=405)


@login_required
def manage_item(request):
    context = {'all_item': []}
    items = Item.objects.all()
    for item in items:
        info = {
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'item_type': item.item_type,
            'purchase_price': item.purchase_price,
            'sale_price': item.sale_price,
            'supplier_id': item.supplier_id.id
        }
        context['all_item'].append(info)

    return render(request, template_name='Manage/manage_item.html', context=context)


@login_required
def add_item(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        item_type = request.POST.get('item_type')
        purchase_price = request.POST.get('purchase_price')
        sale_price = request.POST.get('sale_price')
        try:
            supplier_id = request.POST.get('supplier_id')
            supplier = Supplier.objects.get(pk=supplier_id)
        except:
            pass
        form = addItemForm(request.POST)
        if form.is_valid():
            item = Item.objects.create(
                name=name,
                description=description,
                item_type=item_type,
                purchase_price=purchase_price,
                sale_price=sale_price,
                supplier_id=supplier
            )
            return redirect('manage_item')
        else:
            context['form'] = form

    elif request.method == 'GET':
        form = addItemForm()
        context['form'] = form

    return render(request, template_name='Add/add_item.html', context={'form': form})


@login_required
@csrf_exempt
def delete_item_api(request, item_id):
    if request.method == 'DELETE':
        item = Item.objects.get(id=item_id)
        item.delete()
        return HttpResponse(status=200)
    return HttpResponse(status=405)


@login_required
def manage_stock(request):
    context = {'all_stock': []}
    stocks = Stock.objects.all()
    for stock in stocks:
        info = {
            'id': stock.id,
            'color': stock.color,
            'amount': stock.amount,
            'item_id': stock.item_id.id
        }
        context['all_stock'].append(info)

    return render(request, template_name='Manage/manage_stock.html', context=context)


@login_required
def add_stock(request):
    context = {}
    if request.method == 'POST':
        color = request.POST.get('color')
        amount = request.POST.get('amount')
        try:
            item_id = request.POST.get('item_id')
            item = Item.objects.get(pk=item_id)
        except:
            pass
        form = addStockForm(request.POST)
        if form.is_valid():
            stock = Stock.objects.create(
                color=color,
                amount=amount,
                item_id=item
            )
            return redirect('manage_stock')
        else:
            context['form'] = form

    elif request.method == 'GET':
        form = addStockForm()
        context['form'] = form

    return render(request, template_name='Add/add_stock.html', context={'form': form})


@login_required
@csrf_exempt
def delete_stock_api(request, stock_id):
    if request.method == 'DELETE':
        stock = Stock.objects.get(id=stock_id)
        stock.delete()
        return HttpResponse(status=200)
    return HttpResponse(status=405)