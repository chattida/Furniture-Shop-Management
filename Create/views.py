from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from Manage.models import Order, Order_Item

# Create your views here.
@login_required
def create_order(request):
    return render(request, template_name='Create/create_order.html')


@login_required
def send_order(request):
    if request.method == 'POST':
        print(request.POST)
        cus_id = request.POST.get('cus-id')
        list_item = request.POST.get('list-item')
        items_value = request.POST.get('items-value')
        total_price = request.POST.get('total-price')
        context = {
            'cus_id': cus_id,
            'list_item': list_item,
            'items_value': items_value,
            'total_price': total_price
        }
        return render(request, template_name='Create/send_order.html', context=context)
    return redirect('index')